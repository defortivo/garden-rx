from flask import Flask, render_template, request, jsonify, session
import json
import os
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'gardenrx-secret-key-hackathon-2026'

# Load mock data
def load_json(filename):
    path = os.path.join(os.path.dirname(__file__), 'data', filename)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Load all data sources
patterns = load_json('traditional_patterns.json')
courses = load_json('golf_course_trees.json')
pet_places = load_json('pet_friendly.json')
folklore = load_json('folklore_data.json')
national_gardens = load_json('nationalGardens.json')

def get_season():
    month = datetime.now().month
    if 3 <= month <= 5: return "봄"
    elif 6 <= month <= 8: return "여름"
    elif 9 <= month <= 11: return "가을"
    else: return "겨울"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questionnaire')
def questionnaire():
    return render_template('questionnaire.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    
    # Extract user responses
    stress_level = int(data.get('stress_level', 3))
    mood = data.get('mood', 'neutral')
    preference = data.get('preference', 'deep_forest')
    pet_friendly = data.get('pet_friendly', False)
    activity_level = data.get('activity_level', 'moderate')
    garden_type = data.get('garden_type', 'deep_forest')
    
    current_season = get_season()
    
    # ===== WELLNESS PERSONA SCORING ENGINE =====
    # Calculate user's Wellness Persona from their answers
    # Score each national garden based on how well it matches the user
    
    def calculate_persona_score(garden, user):
        score = 0
        
        # 1. Stress Reduction Match (weight: 40%)
        # High stress users need high stressReductionRate
        stress_weight = user['stress_level'] / 5.0  # 0.2 to 1.0
        stress_score = garden['mentalFit']['stressReductionRate'] * stress_weight
        score += stress_score * 0.4
        
        # 2. Energy Boost Match (weight: 20%)
        # Low mood users need energy boost
        mood_energy_map = {
            'very_sad': 1.0, 'sad': 0.8, 'neutral': 0.5,
            'happy': 0.3, 'very_happy': 0.1
        }
        energy_weight = mood_energy_map.get(user['mood'], 0.5)
        energy_score = garden['mentalFit']['energyBoostRate'] * energy_weight
        score += energy_score * 0.2
        
        # 3. Tag Matching (weight: 25%)
        user_tags = []
        # Map preference to tag
        pref_to_tag = {
            'deep_forest': 'Forest', 'water_garden': 'Water',
            'zen_garden': 'Traditional-Pattern', 'mountain_garden': 'High-Activity',
            'meditation_garden': 'Low-Activity'
        }
        user_tags.append(pref_to_tag.get(user['preference'], 'Forest'))
        
        # Activity level tag
        if user['activity_level'] == 'low':
            user_tags.append('Low-Activity')
        elif user['activity_level'] == 'high':
            user_tags.append('High-Activity')
        else:
            user_tags.extend(['Low-Activity', 'High-Activity'])
        
        # Pet-friendly tag
        if user.get('pet_friendly'):
            user_tags.append('Pet-Friendly')
        
        # Count matching tags
        matching_tags = sum(1 for tag in user_tags if tag in garden.get('tags', []))
        tag_score = (matching_tags / len(user_tags)) * 100 if user_tags else 50
        score += tag_score * 0.25
        
        # 4. Pet-friendly bonus (weight: 15%)
        if user.get('pet_friendly') and garden.get('pet_friendly'):
            score += 100 * 0.15
        elif not user.get('pet_friendly'):
            score += 50 * 0.15  # Neutral if no pet
        
        return score
    
    user_profile = {
        'stress_level': stress_level,
        'mood': mood,
        'preference': preference,
        'activity_level': activity_level,
        'pet_friendly': pet_friendly
    }
    
    # Score all 110+ gardens
    scored_gardens = []
    for garden in national_gardens:
        persona_score = calculate_persona_score(garden, user_profile)
        scored_gardens.append((persona_score, garden))
    
    # Sort by score descending
    scored_gardens.sort(key=lambda x: x[0], reverse=True)
    
    # TOP 1 recommendation
    top_garden = scored_gardens[0][1]
    
    # TOP 3 alternatives (indices 1-4, skipping the top)
    alternatives = [g for s, g in scored_gardens[1:4]]
    
    # Get a matching folklore for the top garden
    matching_folklore = [f for f in folklore if any(tag in ['Traditional-Pattern', 'Forest'] for tag in top_garden.get('tags', []))]
    selected_folklore = matching_folklore[0] if matching_folklore else folklore[0]
    
    # Select a walking route based on activity level
    routes = top_garden.get('walking_routes', [])
    if routes:
        if activity_level == 'low':
            selected_route = routes[-1]  # easier route
        elif activity_level == 'high':
            selected_route = routes[0]  # more challenging
        else:
            selected_route = routes[len(routes) // 2]  # moderate
    else:
        selected_route = None
    
    # Generate AI Prescription using the new dataset
    prescription = generate_prescription_national(
        top_garden, selected_route, selected_folklore,
        stress_level, mood, current_season, alternatives
    )
    
    return jsonify({
        'prescription': prescription,
        'garden': top_garden,
        'route': selected_route,
        'folklore': selected_folklore,
        'season': current_season,
        'alternatives': alternatives,
        'totalGardens': len(national_gardens),
        'userProfile': user_profile
    })


def generate_prescription_national(garden, route, folklore, stress_level, mood, season, alternatives):
    garden_name = garden['name']
    garden_region = garden.get('region', '')
    
    stress_messages = {
        5: f"매우 높은 스트레스 수준을 보이고 계십니다. '{garden_name}'의 치유 에너지가 당신에게 절실히 필요합니다.",
        4: f"스트레스가 상당한 수준입니다. '{garden_name}'에서 마음의 평화를 찾아보세요.",
        3: f"적절한 수준의 스트레스 관리가 필요합니다. '{garden_name}'과 함께하는 시간이 좋습니다.",
        2: f"비교적 안정적인 상태입니다. '{garden_name}'의 에너지로 더욱 충전하세요.",
        1: f"매우 안정적인 상태입니다. '{garden_name}'에서 더 깊은 평화를 경험하세요."
    }
    
    mood_messages = {
        'very_sad': f"당신의 마음에 봄이 필요합니다. '{garden_name}'의 자연이 위로와 치유를 전해줄 것입니다.",
        'sad': f"가벼운 우울감이 느껴집니다. '{garden_name}'의 치유 메시지를 들어보세요.",
        'neutral': f"현재 중립적인 감정 상태입니다. '{garden_name}'에서 새로운 에너지를 얻어보세요.",
        'happy': f"긍정적인 에너지가 느껴집니다! '{garden_name}'에서 더 큰 행복을 누리세요.",
        'very_happy': f"최고의 컨디션입니다! '{garden_name}'의 아름다움을 만끽하며 이 기분을 오래 간직하세요."
    }
    
    return {
        'title': f"🌿 AI 가든 처방전: {garden_name}",
        'patient_summary': f"스트레스 지수: {'🌿' * stress_level} ({stress_level}/5) | 감정 상태: {mood} | 추천 계절: {season} | 매칭 점수: {garden['mentalFit']['stressReductionRate']}/100",
        'stress_message': stress_messages.get(stress_level, ""),
        'mood_message': mood_messages.get(mood, ""),
        'garden_recommendation': f"**{garden_name}** ({garden_region}) - {garden['description']}",
        'mental_fit': f"스트레스 감소율: {garden['mentalFit']['stressReductionRate']}% | 에너지 충전율: {garden['mentalFit']['energyBoostRate']}%",
        'tags': ', '.join(garden.get('tags', [])),
        'route_recommendation': f"**{route['name']}** ({route['distance_km']}km, 약 {route['duration_minutes']}분 소요)" if route else "추천 경로 정보가 없습니다.",
        'route_description': route['description'] if route else "",
        'folklore_message': f"**전통 이야기**: {folklore['title']} - {folklore['healing_message']}" if folklore else "",
        'seasonal_tip': f"**계절 추천**: {garden['seasonal_highlights'].get(season, '지금이 방문하기 좋은 계절입니다!')}",
        'healing_instruction': f"【치유 가이드】\n① {garden_name}에 도착하면 5분간 깊은 호흡을 해보세요.\n② 추천 코스를 따라 천천히 걸으며 자연의 소리에 귀를 기울이세요.\n③ 각 스팟에서 2분간 멈춰 주변의 풍경을 온전히 느껴보세요.\n④ 코스 종료 후, 느낀 점을 기록해보세요.",
        'alternative_spots': [
            {
                'name': alt['name'],
                'region': alt.get('region', ''),
                'tags': alt.get('tags', []),
                'stressReductionRate': alt['mentalFit']['stressReductionRate'],
                'energyBoostRate': alt['mentalFit']['energyBoostRate'],
                'description': alt['description'][:80] + '...',
                'pet_friendly': alt.get('pet_friendly', False)
            }
            for alt in alternatives
        ]
    }


@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    
    # Mock AI Docent response based on folklore data
    plant_keywords = {
        '대나무': 'plant_001', 'bamboo': 'plant_001',
        '연꽃': 'plant_002', 'lotus': 'plant_002',
        '소나무': 'plant_003', 'pine': 'plant_003',
        '국화': 'plant_004', 'chrysanthemum': 'plant_004',
        '매화': 'plant_005', 'plum': 'plant_005',
        '난초': 'plant_006', 'orchid': 'plant_006'
    }
    
    # Find relevant folklore
    matched_plant_id = None
    for keyword, plant_id in plant_keywords.items():
        if keyword in user_message.lower():
            matched_plant_id = plant_id
            break
    
    if matched_plant_id:
        relevant_folklore = [f for f in folklore if f['related_plant_id'] == matched_plant_id]
        if relevant_folklore:
            f = relevant_folklore[0]
            bot_response = f"🌿 **{f['title']}**에 대해 알려드리겠습니다.\n\n{f['full_story'][:300]}...\n\n💡 **교훈**: {f['moral']}\n\n🌱 **치유 메시지**: {f['healing_message']}\n\n무엇을 더 알고 싶으신가요?"
        else:
            bot_response = "아직 이 식물에 대한 설화가 준비되지 않았습니다. 다른 식물에 대해 물어봐 주세요."
    else:
        # Check if user is asking about a garden
        garden_keywords = [g['name'] for g in national_gardens[:20]]
        matched_garden = None
        for gname in garden_keywords:
            if gname[:2] in user_message:
                matched_garden = gname
                break
        
        if matched_garden:
            garden_info = next((g for g in national_gardens if g['name'] == matched_garden), None)
            if garden_info:
                bot_response = f"🌳 **{garden_info['name']}**에 대해 알려드리겠습니다!\n\n📍 위치: {garden_info['location']}\n📝 설명: {garden_info['description']}\n🧘 스트레스 감소율: {garden_info['mentalFit']['stressReductionRate']}%\n⚡ 에너지 충전율: {garden_info['mentalFit']['energyBoostRate']}%\n🏷️ 태그: {', '.join(garden_info.get('tags', []))}\n\n이 장소에 대해 더 알고 싶으신가요?"
            else:
                bot_response = random.choice([
                    "🌿 안녕하세요, AI 가든 도슨트입니다. 원하시는 정원이나 식물에 대해 알려드릴 수 있습니다.",
                    "🌸 110여 개의 전국 정원 데이터에서 맞춤 추천이 가능합니다. 설문을 먼저 진행해보세요!",
                    "🍃 특정 정원의 이름을 말씀해 주시면 상세 정보를 알려드립니다."
                ])
        else:
            general_response = [
                "🌿 안녕하세요, AI 가든 도슨트입니다! 110여 개의 전국 정원과 치유 공간 중에서 맞춤 추천이 가능합니다. 설문을 먼저 진행해보세요!",
                "🌸 한국 전통 정원의 아름다움을 경험해보세요. 순천만국가정원, 창덕궁 후원, 아침고요수목원 등이 인기입니다.",
                "🍃 특정 식물(대나무, 연꽃, 소나무, 국화, 매화, 난초)이나 정원의 이름을 말씀해 주시면 자세히 알려드립니다.",
                "🌲 전국 110곳의 치유 공간 데이터가 준비되어 있습니다. 당신에게 딱 맞는 정원을 찾아보세요!"
            ]
            bot_response = random.choice(general_response)
    
    return jsonify({
        'response': bot_response,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/gardens', methods=['GET'])
def get_gardens():
    """Return filtered gardens list for map view"""
    # Get query params
    region = request.args.get('region', '')
    tag = request.args.get('tag', '')
    pet = request.args.get('pet_friendly', '')
    
    filtered = national_gardens
    
    if region:
        filtered = [g for g in filtered if g.get('region', '').lower() == region.lower()]
    if tag:
        filtered = [g for g in filtered if tag in g.get('tags', [])]
    if pet == 'true':
        filtered = [g for g in filtered if g.get('pet_friendly', False)]
    
    return jsonify({
        'count': len(filtered),
        'gardens': filtered
    })

@app.route('/prescription')
def prescription():
    return render_template('prescription.html')

@app.route('/map')
def map_view():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)