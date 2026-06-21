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

# ── Page routing via session_state ──
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'analysis_result' not in st.session_state:
    st.session_state.analysis_result = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def navigate_to(page):
    st.session_state.page = page
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

# ── Core logic ──
def calculate_persona_score(garden, user):
    score = 0
    stress_weight = user['stress_level'] / 5.0
    stress_score = garden['mentalFit']['stressReductionRate'] * stress_weight
    score += stress_score * 0.4

    mood_energy_map = {
        'very_sad': 1.0, 'sad': 0.8, 'neutral': 0.5,
        'happy': 0.3, 'very_happy': 0.1
    }
    energy_weight = mood_energy_map.get(user['mood'], 0.5)
    energy_score = garden['mentalFit']['energyBoostRate'] * energy_weight
    score += energy_score * 0.2

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

    matching_tags = sum(1 for tag in user_tags if tag in garden.get('tags', []))
    tag_score = (matching_tags / len(user_tags)) * 100 if user_tags else 50
    score += tag_score * 0.25

    if user.get('pet_friendly') and garden.get('pet_friendly'):
        score += 100 * 0.15
    elif not user.get('pet_friendly'):
        score += 50 * 0.15

    return score

def generate_prescription_national(garden, route, folklore_item, stress_level, mood, season, alternatives):
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
        'folklore_message': f"**전통 이야기**: {folklore_item['title']} - {folklore_item['healing_message']}" if folklore_item else "",
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

# ── HOME PAGE ──
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

# ── QUESTIONNAIRE PAGE ──
def render_questionnaire():
    st.title("📋 맞춤형 가든 설문")
    st.markdown("아래 질문에 답하면 AI가 당신에게 딱 맞는 정원을 찾아드립니다.")
    st.divider()
    
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
        
        st.divider()
        submitted = st.form_submit_button("🔍 분석 시작하기", type="primary", use_container_width=True)
    
    if submitted:
        current_season = get_season()
        
        user_profile = {
            'stress_level': stress_level,
            'mood': mood,
            'preference': preference,
            'activity_level': activity_level,
            'pet_friendly': pet_friendly
        }
        
        scored_gardens = []
        for garden in national_gardens:
            persona_score = calculate_persona_score(garden, user_profile)
            scored_gardens.append((persona_score, garden))
        
        scored_gardens.sort(key=lambda x: x[0], reverse=True)
        top_garden = scored_gardens[0][1]
        alternatives = [g for s, g in scored_gardens[1:4]]
        
        matching_folklore = [f for f in folklore if any(tag in ['Traditional-Pattern', 'Forest'] for tag in top_garden.get('tags', []))]
        selected_folklore = matching_folklore[0] if matching_folklore else folklore[0]
        
        routes = top_garden.get('walking_routes', [])
        if routes:
            if activity_level == 'low':
                selected_route = routes[-1]
            elif activity_level == 'high':
                selected_route = routes[0]
            else:
                selected_route = routes[len(routes) // 2]
        else:
            selected_route = None
        
        prescription = generate_prescription_national(
            top_garden, selected_route, selected_folklore,
            stress_level, mood, current_season, alternatives
        )
        
        st.session_state.analysis_result = {
            'prescription': prescription,
            'garden': top_garden,
            'route': selected_route,
            'folklore': selected_folklore,
            'season': current_season,
            'alternatives': alternatives,
            'totalGardens': len(national_gardens),
            'userProfile': user_profile
        }
        
        st.success("✅ 분석이 완료되었습니다! 처방전을 확인해보세요.")
        if st.button("💊 처방전 보기", type="primary", use_container_width=True):
            navigate_to('prescription')

# ── PRESCRIPTION PAGE ──
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
    route = result['route']
    folklore_item = result['folklore']
    alternatives = result['alternatives']
    season = result['season']
    
    st.markdown(f"## {p['title']}")
    st.info(p['patient_summary'])
    
    st.markdown("---")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("### 😌 스트레스 분석")
        st.write(p['stress_message'])
        st.write(p['mood_message'])
        
        st.divider()
        st.markdown("### 🌳 추천 정원")
        st.markdown(p['garden_recommendation'])
        st.caption(f"🏷️ 태그: {p['tags']}")
        st.info(p['mental_fit'])
        
        st.divider()
        st.markdown("### 🚶 추천 코스")
        st.markdown(p['route_recommendation'])
        st.write(p['route_description'])
        
        st.divider()
        st.markdown("### 📖 전통 이야기")
        st.markdown(p['folklore_message'])
        st.caption(f"계절 추천: {p['seasonal_tip']}")
    
    with col2:
        st.markdown("### 🧘 치유 가이드")
        st.success(p['healing_instruction'])
        
        if folklore_item:
            st.divider()
            st.markdown(f"### 📚 {folklore_item.get('title', '관련 설화')}")
            st.write(folklore_item.get('full_story', '')[:200] + "...")
            st.caption(f"💡 {folklore_item.get('moral', '')}")
        
        st.divider()
        st.markdown("### 🏆 추천 대안")
        for i, alt in enumerate(alternatives, 1):
            with st.expander(f"{i}. {alt['name']} ({alt.get('region', '')})"):
                st.write(f"🧘 스트레스 감소율: {alt['mentalFit']['stressReductionRate']}%")
                st.write(f"⚡ 에너지 충전율: {alt['mentalFit']['energyBoostRate']}%")
                st.write(f"📝 {alt['description'][:100]}...")
                if alt.get('pet_friendly'):
                    st.write("🐾 반려동물 동반 가능")
    
    st.divider()
    st.caption(f"✅ 총 {result['totalGardens']}곳의 정원 데이터를 기반으로 분석되었습니다.")
    
    if st.button("🔄 다시 분석하기", use_container_width=True):
        navigate_to('questionnaire')

# ── MAP PAGE ──
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

# ── CHATBOT PAGE ──
def render_chatbot():
    st.title("💬 AI 가든 도슨트")
    st.markdown("식물이나 정원에 대해 질문해보세요! (예: 대나무, 연꽃, 소나무, 순천만국가정원)")
    st.divider()
    
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

# ── Main Router ──
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
