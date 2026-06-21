import streamlit as st
import json
import os
import random
from datetime import datetime

# ── Page config ──
st.set_page_config(page_title="Garden RX - AI 가든 처방전", layout="wide")

# ── Load data ──
def load_json(filename):
    path = os.path.join(os.path.dirname(__file__), 'data', filename)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

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

# ── Session state initialization ──
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'analysis_result' not in st.session_state:
    st.session_state.analysis_result = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'analysis_complete' not in st.session_state:
    st.session_state.analysis_complete = False
if 'show_prescription' not in st.session_state:
    st.session_state.show_prescription = False

# Expander toggles for the 4 wellness cards
if 'expander_traditional_plants' not in st.session_state:
    st.session_state.expander_traditional_plants = False
if 'expander_golf_course' not in st.session_state:
    st.session_state.expander_golf_course = False
if 'expander_pet_friendly' not in st.session_state:
    st.session_state.expander_pet_friendly = False
if 'expander_sagunja' not in st.session_state:
    st.session_state.expander_sagunja = False

def navigate_to(page):
    st.session_state.page = page
    st.session_state.show_prescription = False
    # Reset analysis_complete only when navigating to questionnaire (fresh start)
    if page == 'questionnaire':
        st.session_state.analysis_complete = False
        st.session_state.analysis_result = None
    st.rerun()

# ── Sidebar navigation ──
with st.sidebar:
    st.title("🌿 Garden RX")
    st.caption("AI 기반 맞춤형 정원 처방 서비스")
    st.divider()
    
    if st.button("🏠 홈", use_container_width=True):
        navigate_to('home')
    if st.button("📋 설문하기", use_container_width=True):
        navigate_to('questionnaire')
    if st.button("💊 처방전 보기", use_container_width=True):
        navigate_to('prescription')
    if st.button("🗺️ 지도 보기", use_container_width=True):
        navigate_to('map')
    if st.button("💬 AI 도슨트", use_container_width=True):
        navigate_to('chatbot')
    
    st.divider()
    st.caption(f"🍂 현재 계절: {get_season()}")
    st.caption(f"🏞️ 등록된 정원: {len(national_gardens)}곳")

# ============================================================================
# THE 4 PUBLIC SPOTS for dynamic scoring
# ============================================================================
PUBLIC_SPOTS = [
    {
        "id": "spot_001",
        "name": "뉴서울CC (프리미엄 골프코스)",
        "region": "경기도 가평군",
        "description": "48,500그루의 나무가 우거진 프리미엄 골프장. 소나무 12,000그루, 잣나무 8,500그루, 전나무 6,200그루 등 8종 48,500주의 수목이 조성한 치유의 숲과 18홀 골프코스가 조화를 이룬다. 계절별 꽃길과 약초원, 허브가든이 골퍼와 방문객에게 힐링을 선사한다.",
        "tags": ["Forest", "High-Activity", "Traditional-Pattern"],
        "mentalFit": {"stressReductionRate": 82, "energyBoostRate": 78},
        "pet_friendly": True,
        "folklore_tie": "소나무 숲 — 충절과 장수의 상징인 소나무가 12,000그루 식재되어 전통 정신을 계승",
        "walking_routes": [
            {"name": "숲속 치유 코스", "distance_km": 3.2, "duration_minutes": 50, "difficulty": "쉬움", "description": "소나무 숲을 따라 조성된 평탄한 산책로. 솔향과 피톤치드가 가득한 대표 코스."},
            {"name": "단풍 명상 코스", "distance_km": 2.5, "duration_minutes": 40, "difficulty": "매우 쉬움", "description": "단풍나무 길을 따라 걷는 명상 산책로. 가을에는 장관을 이룬다."}
        ],
        "seasonal_highlights": {"봄": "벚꽃과 철쭉이 만개하는 정원", "여름": "울창한 숲 그늘에서의 산림욕", "가을": "장관을 이루는 단풍과 국화 전시", "겨울": "설경 속 소나무 숲의 장엄한 풍경"},
        "golf_features": ["18홀 각 홀마다 다른 수종 배치", "계절별 꽃길 조성 (벚꽃, 철쭉, 단풍)", "자생식물원 운영", "약초원 및 허브가든"],
        "healing_programs": ["골프와 산림욕 결합 프로그램", "명상 골프 코스", "자연 치유 워킹 코스"],
        "pet_facilities": ["반려동물 전용 산책로 (1.5km)", "펫 케어룸 (에어컨, 물, 간식)", "반려동물 전용 카트", "펫 샤워실", "수의사 상주 (주말)"]
    },
    {
        "id": "spot_002",
        "name": "올림픽공원",
        "region": "서울특별시 송파구",
        "description": "1988년 서울올림픽 개최지로 조성된 대규모 공원. 1,267,000㎡의 드넓은 부지에 잔디밭, 호수, 조각 공원, 산책로가 어우러진 도심 속 대표 휴식처이다. 세계 평화의 상징과 자연이 공존하는 공간으로 시민들에게 사랑받고 있다.",
        "tags": ["Forest", "High-Activity", "Water", "Pet-Friendly"],
        "mentalFit": {"stressReductionRate": 68, "energyBoostRate": 78},
        "pet_friendly": True,
        "folklore_tie": "평화와 조화 — 88올림픽 정신과 전통 소나무 숲이 만나 세계 평화를 기원하는 공간",
        "walking_routes": [
            {"name": "올림픽 둘레길", "distance_km": 4.5, "duration_minutes": 70, "difficulty": "보통", "description": "공원 전체를 한 바퀴 도는 대표 코스. 호수, 조각공원, 잔디광장을 모두 감상할 수 있다."},
            {"name": "호수 산책로", "distance_km": 1.8, "duration_minutes": 30, "difficulty": "쉬움", "description": "88호수를 따라 걷는 여유로운 산책로"}
        ],
        "seasonal_highlights": {"봄": "벚꽃과 철쭉이 아름다운 공원", "여름": "호숫가 산책과 그늘", "가을": "단풍과 억새의 장관", "겨울": "설경 속 조각 공원의 예술"},
        "pet_facilities": ["반려견 놀이터 (대형/소형 분리)", "펫 워터파크", "반려동물 쉼터"]
    },
    {
        "id": "spot_003",
        "name": "국립수목원 전통정원",
        "region": "경기도 포천시",
        "description": "한국 전통 정원 양식을 완벽하게 재현한 국립수목원 내 전통정원. 사군자(매화, 난초, 국화, 대나무)와 소나무, 연꽃 등 한국 전통 식물이 조화를 이루는 치유와 교육의 공간이다. 500년 원시림 광릉숲이 배경을 이루며 전통 정원의 아름다움을 간직하고 있다.",
        "tags": ["Traditional-Pattern", "Low-Activity", "Forest"],
        "mentalFit": {"stressReductionRate": 90, "energyBoostRate": 65},
        "pet_friendly": False,
        "folklore_tie": "사군자의 지혜 — 매화(인내), 난초(우아함), 국화(고귀함), 대나무(절개)가 전하는 군자의 도",
        "walking_routes": [
            {"name": "전통정원 탐방로", "distance_km": 2.0, "duration_minutes": 60, "difficulty": "쉬움", "description": "사군자 정원, 전통 연못, 약초원을 둘러보는 코스. 해설사와 함께하면 더 깊이 있는 탐방이 가능하다."},
            {"name": "광릉 숲길", "distance_km": 3.5, "duration_minutes": 60, "difficulty": "쉬움", "description": "500년 원시림 광릉숲을 걷는 산책로"}
        ],
        "seasonal_highlights": {"봄": "매화와 목련, 산수유가 피는 전통정원", "여름": "연꽃이 만개한 전통 연못", "가을": "국화 전시와 단풍", "겨울": "설경 속 동백과 전통 정원의 아름다움"}
    },
    {
        "id": "spot_004",
        "name": "서울숲 (반려동물 특화공원)",
        "region": "서울특별시 성동구",
        "description": "서울 한가운데 위치한 1,156,000㎡ 규모의 대규모 도시 숲. 반려견 놀이터, 펫 워터파크, 1.5km 반려동물 전용 산책로 등 반려동물 친화적 시설이 완비된 특화 공간이다. 다양한 테마 정원과 생태 연못이 조화를 이룬다.",
        "tags": ["Pet-Friendly", "Low-Activity", "Forest", "Water"],
        "mentalFit": {"stressReductionRate": 75, "energyBoostRate": 70},
        "pet_friendly": True,
        "folklore_tie": "더불어 사는 지혜 — 사람과 자연, 반려동물이 함께하는 조화로운 공동체 정신",
        "walking_routes": [
            {"name": "반려동물 동반 산책로", "distance_km": 1.5, "duration_minutes": 30, "difficulty": "쉬움", "description": "반려동물과 함께 걷는 전용 산책로. 중간중간 음수대와 쉼터가 마련되어 있다."},
            {"name": "숲속 산책로", "distance_km": 2.5, "duration_minutes": 40, "difficulty": "쉬움", "description": "울창한 숲을 따라 걷는 평탄한 산책로"}
        ],
        "seasonal_highlights": {"봄": "벚꽃과 유채꽃이 만개", "여름": "시원한 그늘의 숲길과 펫 워터파크", "가을": "단풍이 아름다운 공원", "겨울": "설경 속 고요한 숲"},
        "pet_facilities": ["반려견 놀이터 (대형/소형 분리)", "펫 워터파크", "반려동물 쉼터 그늘막", "배변봉투 무료 제공", "반려동물 음수대"]
    }
]

# ============================================================================
# DYNAMIC SCORING ALGORITHM
# ============================================================================
def calculate_spot_score(spot, user):
    """
    지능형 점수 매칭 알고리즘 (0~100점)
    - 스트레스 감소 적합도 (30%)
    - 에너지 충전 적합도 (20%)
    - 선호 태그 매칭 (25%)
    - 반려동물 동반 적합도 (15%)
    - 계절 적합도 (10%)
    """
    score = 0.0
    
    # 1. Stress reduction fit (30%)
    stress_weight = user['stress_level'] / 5.0  # 0.2 ~ 1.0
    stress_score = spot['mentalFit']['stressReductionRate'] * stress_weight
    score += stress_score * 0.3
    
    # 2. Energy boost fit (20%)
    mood_energy_map = {
        'very_sad': 1.0, 'sad': 0.8, 'neutral': 0.5,
        'happy': 0.3, 'very_happy': 0.1
    }
    mood_weight = mood_energy_map.get(user['mood'], 0.5)
    # 우울/슬픔 → 높은 에너지 충전 필요, 행복 → 적당한 에너지
    if mood_weight > 0.5:
        energy_score = spot['mentalFit']['energyBoostRate']
    else:
        energy_score = spot['mentalFit']['energyBoostRate'] * (1 + (0.5 - mood_weight))
    score += energy_score * 0.2
    
    # 3. Tag matching (25%)
    user_tags = []
    pref_to_tag = {
        'deep_forest': 'Forest', 'water_garden': 'Water',
        'zen_garden': 'Traditional-Pattern', 'mountain_garden': 'High-Activity',
        'meditation_garden': 'Low-Activity'
    }
    user_tags.append(pref_to_tag.get(user['preference'], 'Forest'))
    
    if user['activity_level'] == 'low':
        user_tags.append('Low-Activity')
    elif user['activity_level'] == 'high':
        user_tags.append('High-Activity')
    else:
        user_tags.extend(['Low-Activity', 'High-Activity'])
    
    if user.get('pet_friendly'):
        user_tags.append('Pet-Friendly')
    
    spot_tags = spot.get('tags', [])
    matching_tags = sum(1 for tag in user_tags if tag in spot_tags)
    tag_score = (matching_tags / len(user_tags)) * 100 if user_tags else 50
    score += tag_score * 0.25
    
    # 4. Pet-friendly match (15%)
    if user.get('pet_friendly') and spot.get('pet_friendly'):
        score += 100 * 0.15
    elif not user.get('pet_friendly'):
        score += 50 * 0.15
    # user wants pet but spot doesn't allow → no points
    
    # 5. Seasonal fit (10%)
    season = get_season()
    season_match = spot.get('seasonal_highlights', {}).get(season, None)
    season_score = 100 if season_match else 50
    score += season_score * 0.1
    
    return round(score, 1)


def generate_prescription(top_spot, user, season, all_scored_spots):
    """Generate full prescription data from the top-scored spot."""
    stress_level = user['stress_level']
    mood = user['mood']
    
    stress_messages = {
        5: f"매우 높은 스트레스 수준을 보이고 계십니다. '{top_spot['name']}'의 치유 에너지가 당신에게 절실히 필요합니다.",
        4: f"스트레스가 상당한 수준입니다. '{top_spot['name']}'에서 마음의 평화를 찾아보세요.",
        3: f"적절한 수준의 스트레스 관리가 필요합니다. '{top_spot['name']}'과 함께하는 시간이 좋습니다.",
        2: f"비교적 안정적인 상태입니다. '{top_spot['name']}'의 에너지로 더욱 충전하세요.",
        1: f"매우 안정적인 상태입니다. '{top_spot['name']}'에서 더 깊은 평화를 경험하세요."
    }
    mood_messages = {
        'very_sad': f"당신의 마음에 봄이 필요합니다. '{top_spot['name']}'의 자연이 위로와 치유를 전해줄 것입니다.",
        'sad': f"가벼운 우울감이 느껴집니다. '{top_spot['name']}'의 치유 메시지를 들어보세요.",
        'neutral': f"현재 중립적인 감정 상태입니다. '{top_spot['name']}'에서 새로운 에너지를 얻어보세요.",
        'happy': f"긍정적인 에너지가 느껴집니다! '{top_spot['name']}'에서 더 큰 행복을 누리세요.",
        'very_happy': f"최고의 컨디션입니다! '{top_spot['name']}'의 아름다움을 만끽하며 이 기분을 오래 간직하세요."
    }
    
    # Route selection based on activity level
    routes = top_spot.get('walking_routes', [])
    if routes:
        if user['activity_level'] == 'low':
            selected_route = routes[-1]
        elif user['activity_level'] == 'high':
            selected_route = routes[0]
        else:
            selected_route = routes[len(routes) // 2] if len(routes) > 1 else routes[0]
    else:
        selected_route = None
    
    # Select relevant folklore (match by tag)
    matching_folklore = [f for f in folklore if any(
        tag in ['Traditional-Pattern', 'Forest'] for tag in top_spot.get('tags', [])
    )]
    selected_folklore = matching_folklore[0] if matching_folklore else folklore[0]
    
    # Select relevant traditional pattern
    garden_types = {
        'Forest': 'deep_forest',
        'Water': 'water_garden',
        'Traditional-Pattern': 'zen_garden',
        'High-Activity': 'mountain_garden',
        'Low-Activity': 'meditation_garden',
        'Pet-Friendly': 'deep_forest'
    }
    preferred_type = None
    for tag in top_spot.get('tags', []):
        if tag in garden_types:
            preferred_type = garden_types[tag]
            break
    relevant_patterns = [p for p in patterns if preferred_type in p.get('recommended_garden_type', [])]
    selected_pattern = relevant_patterns[0] if relevant_patterns else patterns[0]
    
    # Pet-friendly info
    pet_info = None
    if user.get('pet_friendly'):
        for p in pet_places:
            pname = p.get('place_name', '').lower()
            if any(word in pname for word in top_spot['name'].lower().replace('(','').replace(')','').split()):
                pet_info = p
                break
    
    # Build alternatives list
    alternatives = []
    for score, spot in all_scored_spots:
        if len(alternatives) >= 3:
            break
        if spot['id'] != top_spot['id']:
            alt_route = spot.get('walking_routes', [None])[0]
            pet_flag = spot.get('pet_friendly', False)
            alternatives.append({
                'name': spot['name'],
                'region': spot.get('region', ''),
                'tags': spot.get('tags', []),
                'stressReductionRate': spot['mentalFit']['stressReductionRate'],
                'energyBoostRate': spot['mentalFit']['energyBoostRate'],
                'description': spot['description'][:80] + '...' if len(spot['description']) > 80 else spot['description'],
                'pet_friendly': pet_flag,
                'score': score,
                'folklore_tie': spot.get('folklore_tie', ''),
                'route': alt_route
            })
    
    return {
        'title': f"🌿 AI 가든 처방전: {top_spot['name']}",
        'patient_summary': f"스트레스 지수: {'🌿' * stress_level} ({stress_level}/5) | 감정 상태: {mood} | 추천 계절: {season} | 매칭 점수: {dict(all_scored_spots).get(top_spot['id'], {}).get('score', '?')}",
        'stress_message': stress_messages.get(stress_level, ""),
        'mood_message': mood_messages.get(mood, ""),
        'garden_name': top_spot['name'],
        'garden_region': top_spot.get('region', ''),
        'garden_description': top_spot['description'],
        'tags': ', '.join(top_spot.get('tags', [])),
        'stressReductionRate': top_spot['mentalFit']['stressReductionRate'],
        'energyBoostRate': top_spot['mentalFit']['energyBoostRate'],
        'route_recommendation': f"**{selected_route['name']}** ({selected_route['distance_km']}km, 약 {selected_route['duration_minutes']}분 소요)" if selected_route else "추천 경로 정보가 없습니다.",
        'route_description': selected_route['description'] if selected_route else "",
        'folklore_tie': top_spot.get('folklore_tie', ''),
        'season': season,
        'seasonal_tip': top_spot.get('seasonal_highlights', {}).get(season, '지금이 방문하기 좋은 계절입니다!'),
        'healing_instruction': (
            f"【치유 가이드】\n"
            f"① {top_spot['name']}에 도착하면 5분간 깊은 호흡을 해보세요.\n"
            f"② 추천 코스를 따라 천천히 걸으며 자연의 소리에 귀를 기울이세요.\n"
            f"③ 각 스팟에서 2분간 멈춰 주변의 풍경을 온전히 느껴보세요.\n"
            f"④ 코스 종료 후, 느낀 점을 기록해보세요."
        ),
        'selected_folklore': selected_folklore,
        'selected_pattern': selected_pattern,
        'pet_info': pet_info,
        'golf_features': top_spot.get('golf_features', []),
        'healing_programs': top_spot.get('healing_programs', []),
        'pet_facilities': top_spot.get('pet_facilities', []),
        'alternatives': alternatives,
        'scored_spots': [(s, spot) for s, spot in all_scored_spots]
    }


def get_chatbot_response(user_message):
    """Mock AI Docent response based on folklore data"""
    plant_keywords = {
        '대나무': 'plant_001', 'bamboo': 'plant_001',
        '연꽃': 'plant_002', 'lotus': 'plant_002',
        '소나무': 'plant_003', 'pine': 'plant_003',
        '국화': 'plant_004', 'chrysanthemum': 'plant_004',
        '매화': 'plant_005', 'plum': 'plant_005',
        '난초': 'plant_006', 'orchid': 'plant_006'
    }

    matched_plant_id = None
    for keyword, plant_id in plant_keywords.items():
        if keyword in user_message.lower():
            matched_plant_id = plant_id
            break

    if matched_plant_id:
        relevant_folklore = [f for f in folklore if f['related_plant_id'] == matched_plant_id]
        if relevant_folklore:
            f = relevant_folklore[0]
            return f"🌿 **{f['title']}**에 대해 알려드리겠습니다.\n\n{f['full_story'][:300]}...\n\n💡 **교훈**: {f['moral']}\n\n🌱 **치유 메시지**: {f['healing_message']}\n\n무엇을 더 알고 싶으신가요?"
        else:
            return "아직 이 식물에 대한 설화가 준비되지 않았습니다. 다른 식물에 대해 물어봐 주세요."

    garden_keywords = [g['name'] for g in national_gardens[:20]]
    matched_garden = None
    for gname in garden_keywords:
        if gname[:2] in user_message:
            matched_garden = gname
            break

    if matched_garden:
        garden_info = next((g for g in national_gardens if g['name'] == matched_garden), None)
        if garden_info:
            return (f"🌳 **{garden_info['name']}**에 대해 알려드리겠습니다!\n\n"
                    f"📍 위치: {garden_info['location']}\n"
                    f"📝 설명: {garden_info['description']}\n"
                    f"🧘 스트레스 감소율: {garden_info['mentalFit']['stressReductionRate']}%\n"
                    f"⚡ 에너지 충전율: {garden_info['mentalFit']['energyBoostRate']}%\n"
                    f"🏷️ 태그: {', '.join(garden_info.get('tags', []))}\n\n"
                    f"이 장소에 대해 더 알고 싶으신가요?")

    general_response = [
        "🌿 안녕하세요, AI 가든 도슨트입니다! 110여 개의 전국 정원과 치유 공간 중에서 맞춤 추천이 가능합니다. 설문을 먼저 진행해보세요!",
        "🌸 한국 전통 정원의 아름다움을 경험해보세요. 순천만국가정원, 창덕궁 후원, 아침고요수목원 등이 인기입니다.",
        "🍃 특정 식물(대나무, 연꽃, 소나무, 국화, 매화, 난초)이나 정원의 이름을 말씀해 주시면 자세히 알려드립니다.",
        "🌲 전국 110곳의 치유 공간 데이터가 준비되어 있습니다. 당신에게 딱 맞는 정원을 찾아보세요!"
    ]
    return random.choice(general_response)


# ============================================================================
# HOME PAGE
# ============================================================================
def render_home():
    st.title("🌿 Garden RX - AI 가든 처방전")
    st.markdown("---")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        ## 당신만을 위한 맞춤 정원 처방
        
        **Garden RX**는 AI 기반 추천 엔진을 통해 전국 **110여 개의 치유 정원** 중
        당신의 스트레스 수준, 감정 상태, 활동 선호도에 가장 적합한 정원을 추천합니다.
        
        ### 🎯 주요 기능
        - **맞춤형 설문 분석** — 5가지 요소 기반 정원 추천
        - **AI 가든 처방전** — 맞춤형 치유 가이드 제공
        - **AI 도슨트 챗봇** — 식물·정원 정보 검색
        - **전국 정원 지도** — 위치 기반 정원 탐색
        """)
        
        if st.button("📋 지금 설문하러 가기", type="primary", use_container_width=True):
            navigate_to('questionnaire')
    
    with col2:
        st.markdown("### 🌟 오늘의 추천")
        season = get_season()
        seasonal_gardens = [g for g in national_gardens if season in g.get('seasonal_highlights', {})]
        if seasonal_gardens:
            featured = random.choice(seasonal_gardens)
            st.info(f"**{featured['name']}**")
            st.caption(f"📍 {featured.get('region', '')} | 🧘 스트레스 감소율: {featured['mentalFit']['stressReductionRate']}%")
            st.write(featured['description'][:100] + "...")
        else:
            st.info("데이터를 불러오는 중입니다...")
        
        st.markdown("### 🏞️ 탐색하기")
        if st.button("🗺️ 지도로 정원 둘러보기", use_container_width=True):
            navigate_to('map')
        if st.button("💬 AI 도슨트와 대화하기", use_container_width=True):
            navigate_to('chatbot')


# ============================================================================
# QUESTIONNAIRE PAGE
# ============================================================================
def render_questionnaire():
    st.title("📋 맞춤형 가든 설문")
    st.markdown("아래 5가지 질문에 답하면 AI가 당신에게 딱 맞는 정원을 찾아드립니다.")
    st.markdown("---")
    
    with st.form("questionnaire_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            stress_level = st.slider(
                "😰 현재 스트레스 수준",
                min_value=1, max_value=5, value=3,
                help="1 = 매우 낮음, 5 = 매우 높음"
            )
            
            mood = st.selectbox(
                "😊 현재 기분 상태",
                options=['very_sad', 'sad', 'neutral', 'happy', 'very_happy'],
                format_func=lambda x: {
                    'very_sad': '😢 매우 우울함',
                    'sad': '😔 우울함',
                    'neutral': '😐 보통',
                    'happy': '😊 행복함',
                    'very_happy': '🥳 매우 행복함'
                }.get(x, x),
                index=2
            )
            
            preference = st.selectbox(
                "🌳 선호하는 정원 스타일",
                options=['deep_forest', 'water_garden', 'zen_garden', 'mountain_garden', 'meditation_garden'],
                format_func=lambda x: {
                    'deep_forest': '🌲 깊은 숲',
                    'water_garden': '💧 물 정원',
                    'zen_garden': '🏯 전통 사찰 정원',
                    'mountain_garden': '⛰️ 산 정원',
                    'meditation_garden': '🧘 명상 정원'
                }.get(x, x)
            )
        
        with col2:
            activity_level = st.radio(
                "🚶 선호하는 활동량",
                options=['low', 'moderate', 'high'],
                format_func=lambda x: {
                    'low': '🐢 여유롭게 (2km 이내)',
                    'moderate': '🚶 적당히 (3~5km)',
                    'high': '🏃 활발하게 (5km 이상)'
                }.get(x, x),
                index=1
            )
            
            pet_friendly = st.checkbox("🐾 반려동물 동반 가능한 곳")
            
            garden_type = st.selectbox(
                "🌿 추가 선호 유형",
                options=['deep_forest', 'water_garden', 'zen_garden', 'mountain_garden', 'meditation_garden'],
                format_func=lambda x: {
                    'deep_forest': '🌲 깊은 숲',
                    'water_garden': '💧 물 정원',
                    'zen_garden': '🏯 전통 사찰 정원',
                    'mountain_garden': '⛰️ 산 정원',
                    'meditation_garden': '🧘 명상 정원'
                }.get(x, x)
            )
        
        st.markdown("---")
        submitted = st.form_submit_button("🔍 분석 시작하기", type="primary", use_container_width=True)
    
    # ---- THIS BLOCK RUNS AFTER FORM SUBMISSION ----
    if submitted:
        current_season = get_season()
        
        user_profile = {
            'stress_level': stress_level,
            'mood': mood,
            'preference': preference,
            'activity_level': activity_level,
            'pet_friendly': pet_friendly
        }
        
        # Dynamic scoring across all 4 public spots
        scored_spots = []
        for spot in PUBLIC_SPOTS:
            spot_score = calculate_spot_score(spot, user_profile)
            scored_spots.append((spot_score, spot))
        
        scored_spots.sort(key=lambda x: x[0], reverse=True)
        top_spot = scored_spots[0][1]
        
        prescription = generate_prescription(top_spot, user_profile, current_season, scored_spots)
        
        st.session_state.analysis_result = {
            'prescription': prescription,
            'garden': top_spot,
            'userProfile': user_profile,
            'season': current_season,
            'scored_spots': scored_spots,
            'totalSpots': len(PUBLIC_SPOTS)
        }
        st.session_state.analysis_complete = True
        
        # Show success outside the form
        # We use st.rerun to exit form context cleanly
        st.rerun()
    
    # Post-submission success UI (outside form)
    if st.session_state.analysis_complete and st.session_state.analysis_result is not None:
        st.success("✅ 분석이 완료되었습니다! 아래 버튼을 눌러 맞춤 처방전을 확인하세요.")
        if st.button("💊 처방전 보기", type="primary", use_container_width=True):
            st.session_state.show_prescription = True
            navigate_to('prescription')


# ============================================================================
# PRESCRIPTION PAGE
# ============================================================================
def render_prescription():
    st.title("💊 AI 가든 처방전")
    st.markdown("---")
    
    if st.session_state.analysis_result is None:
        st.warning("아직 분석 결과가 없습니다. 먼저 설문을 진행해주세요.")
        if st.button("📋 설문하러 가기", type="primary"):
            navigate_to('questionnaire')
        return
    
    result = st.session_state.analysis_result
    p = result['prescription']
    garden = result['garden']
    
    # ── Head section: title & patient summary ──
    st.markdown(f"## {p['title']}")
    
    # Find matching score for display
    top_score = 0
    for score, spot in p.get('scored_spots', []):
        if spot['id'] == garden['id']:
            top_score = score
            break
    
    col_score, col_season, col_mood = st.columns(3)
    with col_score:
        st.metric("🧮 매칭 점수", f"{top_score:.1f}점", delta=None)
    with col_season:
        st.metric("🍂 추천 계절", p['season'])
    with col_mood:
        st.metric("😊 사용자 감정", result['userProfile']['mood'])
    
    st.info(f"스트레스 지수: {'🌿' * result['userProfile']['stress_level']} ({result['userProfile']['stress_level']}/5)")
    
    st.markdown("---")
    
    # ── Main layout: left (analysis) + right (guide & cards) ──
    col_left, col_right = st.columns([3, 2])
    
    with col_left:
        st.markdown("### 😌 스트레스 & 감정 분석")
        st.write(p['stress_message'])
        st.write(p['mood_message'])
        
        st.divider()
        st.markdown("### 🌳 추천 정원")
        st.markdown(f"**{p['garden_name']}** ({p['garden_region']})")
        st.write(p['garden_description'])
        st.caption(f"🏷️ 태그: {p['tags']}")
        
        # Two columns for stress/energy metrics
        met_col1, met_col2 = st.columns(2)
        with met_col1:
            st.metric("🧘 스트레스 감소율", f"{p['stressReductionRate']}%")
        with met_col2:
            st.metric("⚡ 에너지 충전율", f"{p['energyBoostRate']}%")
        
        st.divider()
        st.markdown("### 🚶 추천 코스")
        st.markdown(p['route_recommendation'])
        st.write(p['route_description'])
        
        st.divider()
        st.markdown("### 📖 전통 이야기")
        st.markdown(f"**{p['folklore_tie']}**")
        st.caption(f"🍃 계절 추천: {p['seasonal_tip']}")
        
        # Folklore detail
        if p.get('selected_folklore'):
            f = p['selected_folklore']
            st.markdown(f"#### {f['title']}")
            st.write(f['summary'])
            st.caption(f"💡 {f['moral']}")
    
    with col_right:
        st.markdown("### 🧘 치유 가이드")
        st.success(p['healing_instruction'])
        
        st.divider()
        st.markdown("### 🌟 추천 대안")
        for i, alt in enumerate(p.get('alternatives', []), 1):
            with st.expander(f"{i}. {alt['name']} ({alt.get('region', '')})"):
                st.write(f"🧮 점수: {alt.get('score', '?')}")
                st.write(f"🧘 스트레스 감소율: {alt['stressReductionRate']}%")
                st.write(f"⚡ 에너지 충전율: {alt['energyBoostRate']}%")
                st.write(f"📝 {alt['description']}")
                if alt.get('pet_friendly'):
                    st.write("🐾 반려동물 동반 가능")
                if alt.get('folklore_tie'):
                    st.caption(f"📖 {alt['folklore_tie']}")
                if alt.get('route'):
                    st.caption(f"🚶 추천 코스: {alt['route'].get('name', '')}")
        
        st.divider()
        st.markdown("---")
        st.caption(f"✅ 총 {result['totalSpots']}곳의 대표 치유 공간 데이터를 기반으로 분석되었습니다.")
        
        st.markdown("---")
        if st.button("🔄 다시 분석하기", use_container_width=True):
            navigate_to('questionnaire')
    
    # ========================================================================
    # THE 4 INTERACTIVE WELLNESS CARDS (Expanders with MCST data)
    # ========================================================================
    st.markdown("---")
    st.markdown("## 🌿 스페셜 가든 콘텐츠")
    st.markdown("아래 카드를 클릭하여 전통 식물, 골프 코스, 반려동물 정보, 사군자 치유 지혜를 확인하세요.")
    st.markdown("---")
    
    # ---- CARD 1: 전통식물 도슨트 ----
    folklore_item = p.get('selected_folklore', folklore[0])
    with st.expander("🌸 **전통식물 도슨트 — 한국 전통 식물의 치유 메시지**", expanded=False):
        col_p1, col_p2 = st.columns([1, 2])
        with col_p1:
            st.markdown("### 🌱 식물 정보")
            pattern = p.get('selected_pattern', patterns[0])
            st.markdown(f"**{pattern['korean_name']}** ({pattern['name']})")
            st.markdown(f"**상징**: {pattern['symbolism']}")
            st.markdown(f"**전통적 의미**: {pattern['historical_meaning'][:120]}...")
            st.markdown(f"**치유 속성**: {', '.join(pattern['healing_properties'])}")
            st.markdown(f"**전통 용법**: {pattern['traditional_usage']}")
        with col_p2:
            st.markdown(f"### 📖 {folklore_item['title']}")
            st.write(folklore_item['full_story'][:400] + "...")
            st.info(f"💡 **교훈**: {folklore_item['moral']}")
            st.success(f"🌱 **치유 메시지**: {folklore_item['healing_message']}")
            st.caption(f"🏛️ **전통 수행**: {folklore_item.get('traditional_practice', '')}")
    
    # ---- CARD 2: 프리미엄 골프코스 ----
    with st.expander("🏌️ **프리미엄 골프코스 — 명문 CC의 조경과 치유 프로그램**", expanded=False):
        col_g1, col_g2 = st.columns([1, 1])
        with col_g1:
            st.markdown("### 🌲 수목 현황")
            golf_spot = garden if garden.get('golf_features') else PUBLIC_SPOTS[0]
            course_data = courses[0]  # 뉴서울CC data
            st.markdown(f"**{course_data['name']}**")
            st.markdown(f"📍 위치: {course_data['location']}")
            st.markdown(f"📐 총 면적: {course_data['total_area_sqm']:,}㎡")
            st.markdown(f"🌲 총 수목: {course_data['tree_count']:,}그루")
            st.markdown("#### 주요 수종")
            for sp in course_data['tree_species'][:5]:
                st.markdown(f"- {sp['korean_name']} ({sp['symbolism']}) — {sp['count']:,}그루")
        with col_g2:
            st.markdown("### 🏌️ 골프 & 힐링")
            features = golf_spot.get('golf_features', course_data.get('garden_features', []))
            st.markdown("**조경 특징**")
            for feat in features:
                st.markdown(f"- ✅ {feat}")
            programs = golf_spot.get('healing_programs', course_data.get('healing_programs', []))
            st.markdown("**치유 프로그램**")
            for prog in programs:
                st.markdown(f"- 🧘 {prog}")
            routes = golf_spot.get('walking_routes', [])
            if routes:
                st.markdown("**추천 코스**")
                for r in routes:
                    st.markdown(f"- 🚶 {r['name']} ({r['distance_km']}km / {r['duration_minutes']}분)")
    
    # ---- CARD 3: 반려동물 동반 안내 ----
    with st.expander("🐾 **반려동물 동반 안내 — 펫 프렌들리 정원 가이드**", expanded=False):
        pet_data = p.get('pet_info', None)
        if pet_data:
            st.markdown(f"### 🐕 {pet_data['place_name']} 반려동물 정보")
            st.markdown(f"📍 위치: {pet_data['location']}")
            st.markdown(f"📋 정책: {pet_data['pet_policy']}")
            st.markdown("#### 🏠 시설")
            for fac in pet_data.get('pet_facilities', []):
                st.markdown(f"- ✅ {fac}")
            restr = pet_data.get('restrictions', {})
            st.markdown("#### ⚠️ 제한 사항")
            if restr.get('breed_restriction'):
                st.markdown("- ⛔ 견종 제한 있음")
            if restr.get('size_limit_cm'):
                st.markdown(f"- 📏 크기 제한: {restr['size_limit_cm']}cm 이하")
            if restr.get('leash_required'):
                st.markdown("- 🦮 목줄 필수")
            if restr.get('vaccination_required'):
                st.markdown("- 💉 예방접종 필수")
        else:
            st.markdown("### 🐾 반려동물 동반 가능 정원 정보")
            st.markdown("설문에서 반려동물 동반을 선택하셨습니다. 아래는 대표적인 반려동물 친화 공간입니다.")
            for pet_place in pet_places[:4]:
                with st.container():
                    st.markdown(f"**{pet_place['place_name']}** ({pet_place['location']})")
                    st.markdown(f"- 정책: {pet_place['pet_policy']}")
                    if pet_place.get('pet_facilities'):
                        st.markdown(f"- 시설: {', '.join(pet_place['pet_facilities'][:3])}")
                    st.markdown("---")
    
    # ---- CARD 4: 사군자와 함께하는 치유의 지혜 ----
    with st.expander("🎋 **사군자와 함께하는 치유의 지혜 — 매화·난초·국화·대나무**", expanded=False):
        st.markdown("""
        ### 사군자(四君子) — 한국 전통 정신의 꽃
        
        사군자는 매화(梅花), 난초(蘭草), 국화(菊花), 대나무(竹)를 일컫는 말로,
        선비의 네 가지 덕목을 상징합니다. 각 식물은 독특한 치유 메시지를 전합니다.
        """)
        
        sagunja_items = [
            {
                "name": "🌸 매화 (Plum Blossom)",
                "symbol": "인내, 희망, 고결, 용기",
                "meaning": "사군자의 으뜸. 추운 겨울이 끝날 무렵 가장 먼저 피어나는 꽃으로, 흰 눈 속에서 피는 붉은 매화는 희망과 인내의 상징",
                "healing": "매화가 추운 겨울을 견디고 가장 먼저 피어나듯, 희망은 가장 어두운 순간에도 피어납니다. 항우울 효과와 활력 증진에 도움을 줍니다.",
                "folklore": "매화나무 아래에서 소원을 빌면 이루어진다는 속설이 전해집니다."
            },
            {
                "name": "🌿 난초 (Orchid)",
                "symbol": "우아함, 군자, 고고함, 청아함",
                "meaning": "그윽한 향기와 우아한 자태가 군자의 덕을 닮았다고 여겨졌습니다. 깊은 산골짜기에서도 은은한 향기를 퍼뜨리는 난초는 은둔하는 군자의 상징",
                "healing": "난초가 보이지 않는 곳에서도 향기를 퍼뜨리듯, 당신의 존재 자체가 주변에 선한 영향을 미칩니다. 향기 치료와 정서 안정에 효과적입니다.",
                "folklore": "난초를 키우는 사람의 마음이 청결하면 난초가 더 아름답게 핀다는 이야기가 전해집니다."
            },
            {
                "name": "🌼 국화 (Chrysanthemum)",
                "symbol": "고귀함, 장수, 은둔, 청렴",
                "meaning": "늦가을 서리 속에서도 피어나는 강인함과 은둔자의 청렴함을 상징합니다. 도연명의 '동쪽 울타리 아래 국화를 따며'라는 시구로 유명",
                "healing": "국화가 늦가을 서리를 견디며 피어나듯, 인생의 후반기에도 아름다움과 지혜는 꽃피울 수 있습니다. 두통 완화와 진정 효과가 있습니다.",
                "folklore": "국화를 따서 술을 담그면 장수하고, 국화 이슬을 받아 마시면 눈이 밝아진다는 민간요법이 전해집니다."
            },
            {
                "name": "🎋 대나무 (Bamboo)",
                "symbol": "절개, 충절, 인내, 군자의 덕",
                "meaning": "사계절 푸르름을 유지하며 비바람에도 꺾이지 않는 강인함을 상징합니다. 선비의 곧은 절개를 나타냅니다.",
                "healing": "바람에 휘어져도 부러지지 않는 대나무처럼, 인생의 역경도 유연함과 강인함으로 극복할 수 있습니다. 스트레스 완화와 집중력 향상에 도움을 줍니다.",
                "folklore": "대나무는 바람이 불면 휘어지지만 결코 부러지지 않는다는 이야기가 전해집니다."
            }
        ]
        
        for i, item in enumerate(sagunja_items):
            with st.container():
                st.markdown(f"#### {item['name']}")
                st.markdown(f"**상징**: {item['symbol']}")
                st.markdown(f"**전통적 의미**: {item['meaning']}")
                st.info(f"🌱 **치유 메시지**: {item['healing']}")
                st.caption(f"📖 **설화**: {item['folklore']}")
                if i < len(sagunja_items) - 1:
                    st.markdown("---")
        
        # Sagunja wisdom quote
        st.markdown("---")
        st.success("""
        💫 **사군자의 지혜**
        
        *매화는 추위를 견디며 희망을 피우고,
        난초는 그윽한 향기로 덕을 전하며,
        국화는 서리 속에서 고귀함을 지키고,
        대나무는 바람에 휘어져도 부러지지 않는다.*
        
        — 이 네 가지의 지혜가 당신의 치유를 돕습니다.
        """)
    
    st.markdown("---")
    col_btn1, col_btn2, col_btn3 = st.columns(3)
    with col_btn1:
        if st.button("🏠 홈으로", use_container_width=True):
            navigate_to('home')
    with col_btn2:
        if st.button("📋 다시 설문하기", use_container_width=True):
            navigate_to('questionnaire')
    with col_btn3:
        if st.button("🗺️ 지도 보기", use_container_width=True):
            navigate_to('map')


# ============================================================================
# MAP PAGE
# ============================================================================
def render_map():
    st.title("🗺️ 전국 치유 정원 지도")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        selected_region = st.selectbox(
            "📍 지역 필터",
            options=['전체'] + sorted(set(g.get('region', '') for g in national_gardens if g.get('region')))
        )
    with col2:
        all_tags = set()
        for g in national_gardens:
            for t in g.get('tags', []):
                all_tags.add(t)
        selected_tag = st.selectbox(
            "🏷️ 태그 필터",
            options=['전체'] + sorted(all_tags)
        )
    with col3:
        pet_only = st.checkbox("🐾 반려동물 동반 가능만 보기")
    
    filtered = national_gardens
    if selected_region != '전체':
        filtered = [g for g in filtered if g.get('region') == selected_region]
    if selected_tag != '전체':
        filtered = [g for g in filtered if selected_tag in g.get('tags', [])]
    if pet_only:
        filtered = [g for g in filtered if g.get('pet_friendly', False)]
    
    st.info(f"📊 검색 결과: 총 **{len(filtered)}**곳의 정원이 있습니다.")
    
    for i, g in enumerate(filtered):
        with st.expander(f"{i+1}. {g['name']} ({g.get('region', '')})"):
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.write(g['description'])
                st.caption(f"🧘 스트레스 감소율: {g['mentalFit']['stressReductionRate']}% | ⚡ 에너지 충전율: {g['mentalFit']['energyBoostRate']}%")
                st.caption(f"🏷️ 태그: {', '.join(g.get('tags', []))}")
                if g.get('pet_friendly'):
                    st.caption("🐾 반려동물 동반 가능")
            with col_b:
                if g.get('walking_routes'):
                    route = g['walking_routes'][0]
                    st.metric("추천 코스", route['name'])
                    st.caption(f"{route['distance_km']}km / {route['duration_minutes']}분")
                if st.button(f"추천하기", key=f"pick_{i}"):
                    st.session_state.analysis_result = None
                    st.info(f"'{g['name']}'에 대한 자세한 정보는 AI 도슨트에게 물어보세요!")


# ============================================================================
# CHATBOT PAGE
# ============================================================================
def render_chatbot():
    st.title("💬 AI 가든 도슨트")
    st.markdown("식물이나 정원에 대해 질문해보세요! (예: 대나무, 연꽃, 소나무, 순천만국가정원)")
    st.markdown("---")
    
    # Display chat history
    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"]):
            st.markdown(chat["content"])
    
    # Chat input
    user_message = st.chat_input("질문을 입력하세요...")
    
    if user_message:
        st.session_state.chat_history.append({"role": "user", "content": user_message})
        with st.chat_message("user"):
            st.markdown(user_message)
        
        bot_response = get_chatbot_response(user_message)
        st.session_state.chat_history.append({"role": "assistant", "content": bot_response})
        with st.chat_message("assistant"):
            st.markdown(bot_response)
    
    if st.session_state.chat_history and st.button("대화 초기화", type="secondary"):
        st.session_state.chat_history = []
        st.rerun()


# ============================================================================
# MAIN ROUTER
# ============================================================================
page = st.session_state.page

if page == 'home':
    render_home()
elif page == 'questionnaire':
    render_questionnaire()
elif page == 'prescription':
    render_prescription()
elif page == 'map':
    render_map()
elif page == 'chatbot':
    render_chatbot()