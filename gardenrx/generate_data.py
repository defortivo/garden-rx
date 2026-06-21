#!/usr/bin/env python3
"""Generate 100+ national garden/wellness locations for GardenRx."""
import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

gardens = [
    # ===== 서울 (Seoul) =====
    {
        "id": "garden_001", "name": "서울숲", "region": "Seoul", "location": "서울특별시 성동구",
        "coordinates": {"lat": 37.5443, "lng": 127.0373},
        "tags": ["Forest", "Water", "Pet-Friendly", "Low-Activity"],
        "description": "서울 한가운데 위치한 대규모 도시 숲. 다양한 테마 정원과 생태 연못이 조화를 이루며, 반려동물과 함께 즐길 수 있는 공간.",
        "mentalFit": {"stressReductionRate": 75, "energyBoostRate": 65},
        "pet_friendly": True, "walking_routes": [
            {"name": "숲속 산책로", "distance_km": 2.5, "duration_minutes": 40, "difficulty": "쉬움", "description": "울창한 숲을 따라 걷는 평탄한 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 유채꽃이 만개", "summer": "시원한 그늘의 숲길", "autumn": "단풍이 아름다운 공원", "winter": "설경 속 고요한 숲"}
    },
    {
        "id": "garden_002", "name": "북서울꿈의숲", "region": "Seoul", "location": "서울특별시 강북구",
        "coordinates": {"lat": 37.6200, "lng": 127.0400},
        "tags": ["Forest", "High-Activity", "Traditional-Pattern"],
        "description": "북한산 자락에 위치한 대규모 공원. 전통 정원과 전망대, 산책로가 잘 조성되어 있다.",
        "mentalFit": {"stressReductionRate": 70, "energyBoostRate": 75},
        "pet_friendly": False, "walking_routes": [
            {"name": "북한산 둘레길", "distance_km": 3.8, "duration_minutes": 60, "difficulty": "보통", "description": "북한산 자락을 따라 조성된 산책로"}
        ], "seasonal_highlights": {"spring": "진달래와 벚꽃", "summer": "울창한 숲", "autumn": "단풍 명소", "winter": "설경 전망"}
    },
    {
        "id": "garden_003", "name": "남산공원", "region": "Seoul", "location": "서울특별시 중구",
        "coordinates": {"lat": 37.5512, "lng": 126.9882},
        "tags": ["Forest", "Low-Activity", "Traditional-Pattern"],
        "description": "서울 중심에 위치한 대표적인 도심 공원. 소나무 숲과 전통 정자가 어우러진 치유 공간.",
        "mentalFit": {"stressReductionRate": 72, "energyBoostRate": 60},
        "pet_friendly": True, "walking_routes": [
            {"name": "남산 둘레길", "distance_km": 2.0, "duration_minutes": 35, "difficulty": "쉬움", "description": "남산을 한 바퀴 도는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃 터널", "summer": "녹음이 짙은 숲", "autumn": "단풍과 서울 전망", "winter": "설경과 야경"}
    },
    {
        "id": "garden_004", "name": "경복궁 후원", "region": "Seoul", "location": "서울특별시 종로구",
        "coordinates": {"lat": 37.5796, "lng": 126.9770},
        "tags": ["Traditional-Pattern", "Low-Activity", "Water"],
        "description": "조선 왕조의 대표적인 궁궐 후원. 전통 정원 양식과 연못, 정자가 완벽하게 보존된 역사적 공간.",
        "mentalFit": {"stressReductionRate": 80, "energyBoostRate": 55},
        "pet_friendly": False, "walking_routes": [
            {"name": "궁궐 산책로", "distance_km": 1.5, "duration_minutes": 30, "difficulty": "쉬움", "description": "경복궁 후원을 거닐며 전통 정원을 감상하는 코스"}
        ], "seasonal_highlights": {"spring": "벚꽃과 매화", "summer": "연꽃이 핀 향원정", "autumn": "단풍과 국화", "winter": "설경 속 고궁"}
    },
    {
        "id": "garden_005", "name": "창덕궁 후원 (비원)", "region": "Seoul", "location": "서울특별시 종로구",
        "coordinates": {"lat": 37.5800, "lng": 126.9850},
        "tags": ["Traditional-Pattern", "Forest", "Low-Activity", "Water"],
        "description": "유네스코 세계문화유산으로 등재된 조선 시대 최고의 전통 정원. 자연 지형을 그대로 살린 비원의 아름다움.",
        "mentalFit": {"stressReductionRate": 88, "energyBoostRate": 60},
        "pet_friendly": False, "walking_routes": [
            {"name": "비원 탐방로", "distance_km": 2.0, "duration_minutes": 50, "difficulty": "쉬움", "description": "창덕궁 후원을 둘러보는 전통 정원 탐방 코스"}
        ], "seasonal_highlights": {"spring": "매화와 벚꽃", "summer": "우거진 녹음", "autumn": "단풍 명소", "winter": "설경의 고궁"}
    },
    {
        "id": "garden_006", "name": "올림픽공원", "region": "Seoul", "location": "서울특별시 송파구",
        "coordinates": {"lat": 37.5200, "lng": 127.1200},
        "tags": ["Forest", "High-Activity", "Water", "Pet-Friendly"],
        "description": "1988년 올림픽 개최지로 조성된 대규모 공원. 넓은 잔디밭과 호수, 산책로가 어우러진 도심 속 휴식처.",
        "mentalFit": {"stressReductionRate": 68, "energyBoostRate": 78},
        "pet_friendly": True, "walking_routes": [
            {"name": "올림픽 둘레길", "distance_km": 4.5, "duration_minutes": 70, "difficulty": "보통", "description": "공원 전체를 한 바퀴 도는 코스"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "호숫가 산책", "autumn": "단풍과 억새", "winter": "설경 속 조각 공원"}
    },
    {
        "id": "garden_007", "name": "여의도공원", "region": "Seoul", "location": "서울특별시 영등포구",
        "coordinates": {"lat": 37.5250, "lng": 126.9200},
        "tags": ["Low-Activity", "Water", "Pet-Friendly"],
        "description": "여의도 한가운데 위치한 도심 속 휴식 공간. 전통 정원과 물길이 조화를 이루는 도시 정원.",
        "mentalFit": {"stressReductionRate": 65, "energyBoostRate": 55},
        "pet_friendly": True, "walking_routes": [
            {"name": "공원 산책로", "distance_km": 1.8, "duration_minutes": 30, "difficulty": "쉬움", "description": "공원을 가로지르는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃 축제", "summer": "물놀이장", "autumn": "단풍", "winter": "크리스마스 마켓"}
    },
    {
        "id": "garden_008", "name": "월드컵공원", "region": "Seoul", "location": "서울특별시 마포구",
        "coordinates": {"lat": 37.5700, "lng": 126.8900},
        "tags": ["Forest", "High-Activity", "Water", "Pet-Friendly"],
        "description": "난지도 매립지 위에 조성된 친환경 공원. 하늘공원, 평화의공원 등 다양한 테마 정원으로 구성.",
        "mentalFit": {"stressReductionRate": 72, "energyBoostRate": 70},
        "pet_friendly": True, "walking_routes": [
            {"name": "하늘공원 억새길", "distance_km": 2.2, "duration_minutes": 40, "difficulty": "보통", "description": "하늘공원 정상까지 이어지는 억새밭 산책로"}
        ], "seasonal_highlights": {"spring": "유채꽃밭", "summer": "시원한 강바람", "autumn": "억새 축제", "winter": "설경과 한강 전망"}
    },
    {
        "id": "garden_009", "name": "서울대공원", "region": "Seoul", "location": "서울특별시 과천시",
        "coordinates": {"lat": 37.4300, "lng": 127.0100},
        "tags": ["Forest", "High-Activity", "Pet-Friendly"],
        "description": "청계산 자락에 위치한 대규모 종합 공원. 동물원, 식물원, 산림욕장이 함께 있는 가족형 휴식 공간.",
        "mentalFit": {"stressReductionRate": 70, "energyBoostRate": 72},
        "pet_friendly": True, "walking_routes": [
            {"name": "산림욕장 코스", "distance_km": 3.0, "duration_minutes": 50, "difficulty": "보통", "description": "청계산 자락의 울창한 숲길"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "숲속 산림욕", "autumn": "단풍", "winter": "설경"}
    },
    {
        "id": "garden_010", "name": "뚝섬한강공원", "region": "Seoul", "location": "서울특별시 광진구",
        "coordinates": {"lat": 37.5300, "lng": 127.0700},
        "tags": ["Water", "High-Activity", "Pet-Friendly"],
        "description": "한강변에 위치한 수변 공원. 넓은 잔디밭과 자전거 도로, 수변 산책로가 잘 조성되어 있다.",
        "mentalFit": {"stressReductionRate": 65, "energyBoostRate": 68},
        "pet_friendly": True, "walking_routes": [
            {"name": "한강변 산책로", "distance_km": 3.5, "duration_minutes": 55, "difficulty": "쉬움", "description": "한강을 따라 걷는 수변 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 유채꽃", "summer": "수상 레저", "autumn": "단풍과 강바람", "winter": "한강 설경"}
    },

    # ===== 경기도 (Gyeonggi) =====
    {
        "id": "garden_011", "name": "아침고요수목원", "region": "Gyeonggi", "location": "경기도 가평군",
        "coordinates": {"lat": 37.7500, "lng": 127.3500},
        "tags": ["Forest", "Traditional-Pattern", "Low-Activity", "Water"],
        "description": "한국 전통 정원 양식을 현대적으로 재해석한 아름다운 수목원. 20여 개의 테마 정원이 조성되어 있다.",
        "mentalFit": {"stressReductionRate": 85, "energyBoostRate": 72},
        "pet_friendly": False, "walking_routes": [
            {"name": "수목원 탐방로", "distance_km": 3.0, "duration_minutes": 60, "difficulty": "쉬움", "description": "20여 개의 테마 정원을 둘러보는 코스"}
        ], "seasonal_highlights": {"spring": "튤립과 철쭉", "summer": "수국과 원추리", "autumn": "국화와 단풍", "winter": "오색 별빛 정원"}
    },
    {
        "id": "garden_012", "name": "화담숲", "region": "Gyeonggi", "location": "경기도 광주시",
        "coordinates": {"lat": 37.3800, "lng": 127.2800},
        "tags": ["Forest", "Water", "Low-Activity", "Traditional-Pattern"],
        "description": "LG상록재단이 조성한 한국 최고의 자연 친화 수목원. 17개의 테마원과 4km의 생태 탐방로가 있다.",
        "mentalFit": {"stressReductionRate": 90, "energyBoostRate": 75},
        "pet_friendly": False, "walking_routes": [
            {"name": "생태 탐방로", "distance_km": 4.0, "duration_minutes": 80, "difficulty": "보통", "description": "17개 테마원을 연결하는 생태 탐방로"}
        ], "seasonal_highlights": {"spring": "철쭉과 진달래", "summer": "울창한 녹음", "autumn": "단풍 명소", "winter": "설경과 동백"}
    },
    {
        "id": "garden_013", "name": "두물머리", "region": "Gyeonggi", "location": "경기도 양평군",
        "coordinates": {"lat": 37.5300, "lng": 127.3200},
        "tags": ["Water", "Low-Activity", "Traditional-Pattern"],
        "description": "북한강과 남한강이 만나는 지점에 위치한 명소. 400년 된 느티나무와 수변 풍경이 그림처럼 아름답다.",
        "mentalFit": {"stressReductionRate": 82, "energyBoostRate": 65},
        "pet_friendly": True, "walking_routes": [
            {"name": "두물머리 산책로", "distance_km": 1.5, "duration_minutes": 30, "difficulty": "쉬움", "description": "느티나무와 강변을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 유채꽃", "summer": "시원한 강바람", "autumn": "은행나무 단풍", "winter": "설경과 물안개"}
    },
    {
        "id": "garden_014", "name": "에버랜드 가든", "region": "Gyeonggi", "location": "경기도 용인시",
        "coordinates": {"lat": 37.2900, "lng": 127.2000},
        "tags": ["Forest", "High-Activity", "Water", "Pet-Friendly"],
        "description": "한국 최대 규모의 테마파크 내 조경 정원. 사계절 내내 다양한 꽃과 나무를 감상할 수 있다.",
        "mentalFit": {"stressReductionRate": 65, "energyBoostRate": 80},
        "pet_friendly": True, "walking_routes": [
            {"name": "가든 산책로", "distance_km": 2.5, "duration_minutes": 45, "difficulty": "쉬움", "description": "에버랜드 가든을 둘러보는 코스"}
        ], "seasonal_highlights": {"spring": "튤립 축제", "summer": "장미원", "autumn": "국화와 단풍", "winter": "겨울 정원"}
    },
    {
        "id": "garden_015", "name": "한국민속촌", "region": "Gyeonggi", "location": "경기도 용인시",
        "coordinates": {"lat": 37.2600, "lng": 127.1200},
        "tags": ["Traditional-Pattern", "Low-Activity"],
        "description": "조선 시대 생활상을 재현한 야외 민속 박물관. 전통 정원과 초가집, 옛길이 잘 보존되어 있다.",
        "mentalFit": {"stressReductionRate": 75, "energyBoostRate": 60},
        "pet_friendly": False, "walking_routes": [
            {"name": "민속촌 탐방로", "distance_km": 2.0, "duration_minutes": 50, "difficulty": "쉬움", "description": "전통 가옥과 정원을 둘러보는 코스"}
        ], "seasonal_highlights": {"spring": "벚꽃과 진달래", "summer": "녹음과 연꽃", "autumn": "단풍과 국화", "winter": "설경 속 전통 마을"}
    },
    {
        "id": "garden_016", "name": "수원화성", "region": "Gyeonggi", "location": "경기도 수원시",
        "coordinates": {"lat": 37.2800, "lng": 127.0100},
        "tags": ["Traditional-Pattern", "High-Activity"],
        "description": "유네스코 세계문화유산으로 등재된 조선 시대 성곽. 성곽을 따라 조성된 산책로가 유명하다.",
        "mentalFit": {"stressReductionRate": 70, "energyBoostRate": 75},
        "pet_friendly": True, "walking_routes": [
            {"name": "화성 성곽길", "distance_km": 5.5, "duration_minutes": 90, "difficulty": "보통", "description": "수원화성 성곽을 따라 걷는 코스"}
        ], "seasonal_highlights": {"spring": "벚꽃과 매화", "summer": "녹음과 연꽃", "autumn": "단풍", "winter": "설경 속 성곽"}
    },
    {
        "id": "garden_017", "name": "광릉수목원", "region": "Gyeonggi", "location": "경기도 포천시",
        "coordinates": {"lat": 37.7500, "lng": 127.1800},
        "tags": ["Forest", "Low-Activity", "Traditional-Pattern"],
        "description": "조선 시대 왕릉 숲으로 보호된 울창한 원시림. 500년 이상 된 고목들이 장관을 이룬다.",
        "mentalFit": {"stressReductionRate": 88, "energyBoostRate": 70},
        "pet_friendly": False, "walking_routes": [
            {"name": "광릉 숲길", "distance_km": 3.5, "duration_minutes": 60, "difficulty": "쉬움", "description": "500년 원시림을 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "철쭉과 진달래", "summer": "울창한 원시림", "autumn": "단풍 명소", "winter": "설경의 장엄한 숲"}
    },
    {
        "id": "garden_018", "name": "산정호수", "region": "Gyeonggi", "location": "경기도 포천시",
        "coordinates": {"lat": 38.0700, "lng": 127.3000},
        "tags": ["Water", "Forest", "High-Activity", "Pet-Friendly"],
        "description": "청정 자연에 둘러싸인 산정 호수. 호수를 따라 조성된 데크 산책로가 아름답다.",
        "mentalFit": {"stressReductionRate": 78, "energyBoostRate": 72},
        "pet_friendly": True, "walking_routes": [
            {"name": "호수 둘레길", "distance_km": 3.0, "duration_minutes": 50, "difficulty": "쉬움", "description": "산정호수를 한 바퀴 도는 데크 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "수변 산책", "autumn": "단풍과 호수", "winter": "얼음 호수와 설경"}
    },
    {
        "id": "garden_019", "name": "자연휴양림 (유명산)", "region": "Gyeonggi", "location": "경기도 가평군",
        "coordinates": {"lat": 37.7000, "lng": 127.4500},
        "tags": ["Forest", "High-Activity", "Water"],
        "description": "울창한 자연림 속에 조성된 국립 자연휴양림. 계곡과 숲이 어우러진 치유 공간.",
        "mentalFit": {"stressReductionRate": 82, "energyBoostRate": 78},
        "pet_friendly": False, "walking_routes": [
            {"name": "유명산 등산로", "distance_km": 4.0, "duration_minutes": 90, "difficulty": "보통", "description": "유명산 정상까지 이어지는 숲길"}
        ], "seasonal_highlights": {"spring": "진달래와 철쭉", "summer": "계곡 물놀이", "autumn": "단풍", "winter": "설경"}
    },
    {
        "id": "garden_020", "name": "반월호수공원", "region": "Gyeonggi", "location": "경기도 안산시",
        "coordinates": {"lat": 37.3000, "lng": 126.8300},
        "tags": ["Water", "Low-Activity", "Pet-Friendly"],
        "description": "시화호와 연결된 대규모 호수 공원. 수변 산책로와 자전거 도로가 잘 조성되어 있다.",
        "mentalFit": {"stressReductionRate": 70, "energyBoostRate": 65},
        "pet_friendly": True, "walking_routes": [
            {"name": "호수 산책로", "distance_km": 4.0, "duration_minutes": 60, "difficulty": "쉬움", "description": "반월호수를 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 유채꽃", "summer": "수변 산책", "autumn": "단풍과 갈대", "winter": "호수 설경"}
    },

    # ===== 강원도 (Gangwon) =====
    {
        "id": "garden_021", "name": "남이섬", "region": "Gangwon", "location": "강원특별자치도 춘천시",
        "coordinates": {"lat": 37.7900, "lng": 127.5200},
        "tags": ["Forest", "Water", "Low-Activity", "Pet-Friendly"],
        "description": "북한강에 떠 있는 섬 형태의 관광지. 아름다운 수변 산책로와 숲길이 조성되어 있다.",
        "mentalFit": {"stressReductionRate": 80, "energyBoostRate": 72},
        "pet_friendly": True, "walking_routes": [
            {"name": "섬 둘레길", "distance_km": 3.0, "duration_minutes": 50, "difficulty": "쉬움", "description": "남이섬을 한 바퀴 도는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 수선화", "summer": "시원한 숲길", "autumn": "단풍 명소", "winter": "눈꽃과 겨울 풍경"}
    },
    {
        "id": "garden_022", "name": "설악산국립공원", "region": "Gangwon", "location": "강원특별자치도 속초시",
        "coordinates": {"lat": 38.1200, "lng": 128.4700},
        "tags": ["Forest", "High-Activity", "Water"],
        "description": "한국에서 가장 아름다운 산악 풍경을 자랑하는 국립공원. 울창한 숲과 계곡, 기암괴석이 장관.",
        "mentalFit": {"stressReductionRate": 85, "energyBoostRate": 90},
        "pet_friendly": False, "walking_routes": [
            {"name": "천불동 계곡 코스", "distance_km": 5.0, "duration_minutes": 120, "difficulty": "어려움", "description": "설악산 대표 계곡 탐방 코스"}
        ], "seasonal_highlights": {"spring": "진달래와 산목련", "summer": "계곡과 폭포", "autumn": "단풍 절경", "winter": "설경과 상고대"}
    },
    {
        "id": "garden_023", "name": "오대산국립공원", "region": "Gangwon", "location": "강원특별자치도 평창군",
        "coordinates": {"lat": 37.7900, "lng": 128.5400},
        "tags": ["Forest", "High-Activity", "Traditional-Pattern"],
        "description": "한국 불교의 성지이자 울창한 원시림이 보존된 국립공원. 월정사와 전나무 숲이 유명하다.",
        "mentalFit": {"stressReductionRate": 88, "energyBoostRate": 82},
        "pet_friendly": False, "walking_routes": [
            {"name": "전나무 숲길", "distance_km": 2.5, "duration_minutes": 40, "difficulty": "쉬움", "description": "월정사에서 시작되는 장엄한 전나무 숲길"}
        ], "seasonal_highlights": {"spring": "철쭉과 진달래", "summer": "울창한 원시림", "autumn": "단풍과 억새", "winter": "설경과 상고대"}
    },
    {
        "id": "garden_024", "name": "치악산국립공원", "region": "Gangwon", "location": "강원특별자치도 원주시",
        "coordinates": {"lat": 37.3700, "lng": 128.0500},
        "tags": ["Forest", "High-Activity", "Water"],
        "description": "울창한 숲과 맑은 계곡이 어우러진 국립공원. 구룡사와 상원사 등 전통 사찰이 자리잡고 있다.",
        "mentalFit": {"stressReductionRate": 80, "energyBoostRate": 78},
        "pet_friendly": False, "walking_routes": [
            {"name": "구룡사 계곡길", "distance_km": 3.0, "duration_minutes": 60, "difficulty": "보통", "description": "구룡사까지 이어지는 계곡 산책로"}
        ], "seasonal_highlights": {"spring": "진달래와 벚꽃", "summer": "계곡 물놀이", "autumn": "단풍", "winter": "설경"}
    },
    {
        "id": "garden_025", "name": "태백산국립공원", "region": "Gangwon", "location": "강원특별자치도 태백시",
        "coordinates": {"lat": 37.1200, "lng": 128.9200},
        "tags": ["Forest", "High-Activity", "Traditional-Pattern"],
        "description": "한민족의 영산으로 여겨지는 태백산. 천제단과 철쭉 군락지가 유명한 고산 정원.",
        "mentalFit": {"stressReductionRate": 82, "energyBoostRate": 85},
        "pet_friendly": False, "walking_routes": [
            {"name": "태백산 등산로", "distance_km": 4.5, "duration_minutes": 100, "difficulty": "보통", "description": "태백산 정상까지 이어지는 철쭉길"}
        ], "seasonal_highlights": {"spring": "철쭉 군락", "summer": "고원의 시원함", "autumn": "단풍과 억새", "winter": "눈꽃과 설경"}
    },
    {
        "id": "garden_026", "name": "소금강", "region": "Gangwon", "location": "강원특별자치도 영월군",
        "coordinates": {"lat": 37.2000, "lng": 128.4500},
        "tags": ["Forest", "Water", "Low-Activity"],
        "description": "작은 금강산이라는 뜻의 이름처럼 아름다운 계곡과 기암괴석이 어우러진 명소.",
        "mentalFit": {"stressReductionRate": 78, "energyBoostRate": 70},
        "pet_friendly": True, "walking_routes": [
            {"name": "소금강 계곡길", "distance_km": 2.0, "duration_minutes": 40, "difficulty": "쉬움", "description": "계곡을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "진달래와 벚꽃", "summer": "계곡 물놀이", "autumn": "단풍", "winter": "설경"}
    },
    {
        "id": "garden_027", "name": "정동진 해안숲", "region": "Gangwon", "location": "강원특별자치도 강릉시",
        "coordinates": {"lat": 37.6900, "lng": 129.0300},
        "tags": ["Forest", "Water", "Low-Activity"],
        "description": "동해안을 따라 조성된 해안 숲길. 소나무 숲과 바다가 어우러진 독특한 풍경.",
        "mentalFit": {"stressReductionRate": 75, "energyBoostRate": 72},
        "pet_friendly": True, "walking_routes": [
            {"name": "해안 산책로", "distance_km": 2.5, "duration_minutes": 40, "difficulty": "쉬움", "description": "동해안을 따라 걷는 해안 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 유채꽃", "summer": "해수욕과 숲", "autumn": "단풍과 동해", "winter": "일출과 설경"}
    },
    {
        "id": "garden_028", "name": "대관령 양떼목장", "region": "Gangwon", "location": "강원특별자치도 평창군",
        "coordinates": {"lat": 37.6800, "lng": 128.7200},
        "tags": ["Forest", "High-Activity", "Pet-Friendly"],
        "description": "대관령 고원에 위치한 목장. 드넓은 초원과 양떼, 풍력발전기가 어우러진 이국적인 풍경.",
        "mentalFit": {"stressReductionRate": 78, "energyBoostRate": 80},
        "pet_friendly": True, "walking_routes": [
            {"name": "목장 산책로", "distance_km": 2.0, "duration_minutes": 35, "difficulty": "쉬움", "description": "드넓은 초원을 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "푸른 초원", "summer": "시원한 고원", "autumn": "황금빛 억새", "winter": "설경과 겨울 목장"}
    },
    {
        "id": "garden_029", "name": "고석정", "region": "Gangwon", "location": "강원특별자치도 철원군",
        "coordinates": {"lat": 38.2000, "lng": 127.3000},
        "tags": ["Water", "Traditional-Pattern", "Low-Activity"],
        "description": "한탄강 협곡 위에 위치한 전통 정자. 주변의 주상절리와 강물이 어우러진 장관.",
        "mentalFit": {"stressReductionRate": 72, "energyBoostRate": 65},
        "pet_friendly": True, "walking_routes": [
            {"name": "한탄강 산책로", "distance_km": 1.5, "duration_minutes": 30, "difficulty": "쉬움", "description": "한탄강 협곡을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "철쭉과 벚꽃", "summer": "협곡과 강바람", "autumn": "단풍과 주상절리", "winter": "설경과 겨울 협곡"}
    },
    {
        "id": "garden_030", "name": "삼척 해상케이블카", "region": "Gangwon", "location": "강원특별자치도 삼척시",
        "coordinates": {"lat": 37.4500, "lng": 129.1700},
        "tags": ["Water", "Forest", "High-Activity"],
        "description": "동해안의 아름다운 해안선을 따라 조성된 해안 산책로와 케이블카. 용화리 해변과 죽서루가 인근.",
        "mentalFit": {"stressReductionRate": 74, "energyBoostRate": 76},
        "pet_friendly": False, "walking_routes": [
            {"name": "해안 둘레길", "distance_km": 3.0, "duration_minutes": 50, "difficulty": "보통", "description": "삼척 해안을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 동해", "summer": "해수욕", "autumn": "단풍과 바다", "winter": "동해 일출"}
    },

    # ===== 충청북도 (Chungbuk) =====
    {
        "id": "garden_031", "name": "청남대", "region": "Chungbuk", "location": "충청북도 청주시",
        "coordinates": {"lat": 36.6500, "lng": 127.4800},
        "tags": ["Forest", "Water", "Low-Activity", "Traditional-Pattern"],
        "description": "대청호반에 위치한 옛 대통령 별장. 아름다운 정원과 호수 전망이 일품인 명소.",
        "mentalFit": {"stressReductionRate": 82, "energyBoostRate": 70},
        "pet_friendly": False, "walking_routes": [
            {"name": "대청호 산책로", "distance_km": 2.5, "duration_minutes": 45, "difficulty": "쉬움", "description": "대청호를 따라 조성된 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "호수와 숲", "autumn": "단풍 명소", "winter": "설경과 호수"}
    },
    {
        "id": "garden_032", "name": "속리산국립공원", "region": "Chungbuk", "location": "충청북도 보은군",
        "coordinates": {"lat": 36.5400, "lng": 127.8300},
        "tags": ["Forest", "High-Activity", "Traditional-Pattern"],
        "description": "천년 고찰 법주사가 자리한 명산. 울창한 숲과 기암괴석, 전통 사찰이 어우러진 영산.",
        "mentalFit": {"stressReductionRate": 85, "energyBoostRate": 82},
        "pet_friendly": False, "walking_routes": [
            {"name": "법주사 탐방로", "distance_km": 3.0, "duration_minutes": 60, "difficulty": "보통", "description": "법주사와 속리산을 둘러보는 코스"}
        ], "seasonal_highlights": {"spring": "진달래와 벚꽃", "summer": "계곡과 숲", "autumn": "단풍 절경", "winter": "설경과 고찰"}
    },
    {
        "id": "garden_033", "name": "월악산국립공원", "region": "Chungbuk", "location": "충청북도 제천시",
        "coordinates": {"lat": 36.8800, "lng": 128.1000},
        "tags": ["Forest", "High-Activity", "Water"],
        "description": "충주호와 어우러진 산악 국립공원. 물과 숲이 조화를 이루는 아름다운 풍경.",
        "mentalFit": {"stressReductionRate": 80, "energyBoostRate": 80},
        "pet_friendly": False, "walking_routes": [
            {"name": "충주호 산책로", "distance_km": 3.5, "duration_minutes": 60, "difficulty": "보통", "description": "충주호반을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "진달래와 철쭉", "summer": "호수와 숲", "autumn": "단풍", "winter": "설경"}
    },
    {
        "id": "garden_034", "name": "단양팔경", "region": "Chungbuk", "location": "충청북도 단양군",
        "coordinates": {"lat": 36.9800, "lng": 128.3600},
        "tags": ["Water", "High-Activity", "Traditional-Pattern"],
        "description": "남한강 상류의 아름다운 경승지. 도담삼봉, 석문 등 여덟 가지 빼어난 풍경이 펼쳐진다.",
        "mentalFit": {"stressReductionRate": 78, "energyBoostRate": 76},
        "pet_friendly": True, "walking_routes": [
            {"name": "단양강 산책로", "distance_km": 2.0, "duration_minutes": 35, "difficulty": "쉬움", "description": "단양강을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 유채꽃", "summer": "강과 계곡", "autumn": "단풍", "winter": "설경과 겨울 강"}
    },
    {
        "id": "garden_035", "name": "충주호", "region": "Chungbuk", "location": "충청북도 충주시",
        "coordinates": {"lat": 36.9500, "lng": 127.9500},
        "tags": ["Water", "Forest", "High-Activity", "Pet-Friendly"],
        "description": "한국에서 가장 큰 인공 호수. 호수 주변의 산책로와 자전거 도로가 잘 조성되어 있다.",
        "mentalFit": {"stressReductionRate": 75, "energyBoostRate": 72},
        "pet_friendly": True, "walking_routes": [
            {"name": "충주호 둘레길", "distance_km": 4.0, "duration_minutes": 65, "difficulty": "보통", "description": "충주호를 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "수상 레저", "autumn": "단풍과 호수", "winter": "설경과 겨울 호수"}
    },

    # ===== 충청남도 (Chungnam) =====
    {
        "id": "garden_036", "name": "계룡산국립공원", "region": "Chungnam", "location": "충청남도 공주시",
        "coordinates": {"lat": 36.3600, "lng": 127.2000},
        "tags": ["Forest", "High-Activity", "Traditional-Pattern"],
        "description": "용이 하늘로 승천하는 형상의 명산. 갑사와 동학사 등 전통 사찰과 울창한 숲이 어우러진 영산.",
        "mentalFit": {"stressReductionRate": 82, "energyBoostRate": 78},
        "pet_friendly": False, "walking_routes": [
            {"name": "계룡산 탐방로", "distance_km": 4.0, "duration_minutes": 90, "difficulty": "보통", "description": "계룡산 주요 사찰을 연결하는 탐방로"}
        ], "seasonal_highlights": {"spring": "진달래와 철쭉", "summer": "계곡과 숲", "autumn": "단풍 명소", "winter": "설경과 산사"}
    },
    {
        "id": "garden_037", "name": "태안해안국립공원", "region": "Chungnam", "location": "충청남도 태안군",
        "coordinates": {"lat": 36.7500, "lng": 126.3000},
        "tags": ["Water", "High-Activity", "Pet-Friendly"],
        "description": "서해안의 아름다운 해안선을 따라 조성된 국립공원. 기암괴석과 해변, 소나무 숲이 어우러진 명소.",
        "mentalFit": {"stressReductionRate": 76, "energyBoostRate": 78},
        "pet_friendly": True, "walking_routes": [
            {"name": "해안 산책로", "distance_km": 3.0, "duration_minutes": 50, "difficulty": "쉬움", "description": "태안 해안을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "유채꽃과 벚꽃", "summer": "해수욕", "autumn": "단풍과 서해", "winter": "일몰과 설경"}
    },
    {
        "id": "garden_038", "name": "공주 무령왕릉", "region": "Chungnam", "location": "충청남도 공주시",
        "coordinates": {"lat": 36.4600, "lng": 127.1200},
        "tags": ["Traditional-Pattern", "Low-Activity", "Forest"],
        "description": "백제 시대 왕릉이 모여 있는 역사적 공간. 소나무 숲과 고분이 어우러진 고요한 치유 공간.",
        "mentalFit": {"stressReductionRate": 74, "energyBoostRate": 55},
        "pet_friendly": False, "walking_routes": [
            {"name": "왕릉 산책로", "distance_km": 1.5, "duration_minutes": 30, "difficulty": "쉬움", "description": "무령왕릉 일대를 둘러보는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 매화", "summer": "녹음", "autumn": "단풍", "winter": "설경"}
    },
    {
        "id": "garden_039", "name": "부여 백제문화단지", "region": "Chungnam", "location": "충청남도 부여군",
        "coordinates": {"lat": 36.2800, "lng": 126.9200},
        "tags": ["Traditional-Pattern", "Low-Activity", "Water"],
        "description": "백제 시대 문화를 재현한 대규모 역사 테마파크. 전통 정원과 연못이 아름답게 조성되어 있다.",
        "mentalFit": {"stressReductionRate": 76, "energyBoostRate": 62},
        "pet_friendly": False, "walking_routes": [
            {"name": "백제 정원길", "distance_km": 2.0, "duration_minutes": 40, "difficulty": "쉬움", "description": "백제 문화단지를 둘러보는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "연꽃", "autumn": "국화와 단풍", "winter": "설경"}
    },
    {
        "id": "garden_040", "name": "서산 해미읍성", "region": "Chungnam", "location": "충청남도 서산시",
        "coordinates": {"lat": 36.7000, "lng": 126.5500},
        "tags": ["Traditional-Pattern", "Low-Activity"],
        "description": "조선 시대 읍성이 잘 보존된 역사 유적지. 성곽을 따라 걷는 산책로가 운치 있다.",
        "mentalFit": {"stressReductionRate": 70, "energyBoostRate": 60},
        "pet_friendly": True, "walking_routes": [
            {"name": "성곽 산책로", "distance_km": 1.8, "duration_minutes": 35, "difficulty": "쉬움", "description": "해미읍성 성곽을 따라 걷는 코스"}
        ], "seasonal_highlights": {"spring": "벚꽃과 유채꽃", "summer": "녹음", "autumn": "단풍", "winter": "설경"}
    },

    # ===== 전라북도 (Jeonbuk) =====
    {
        "id": "garden_041", "name": "내장산국립공원", "region": "Jeonbuk", "location": "전라북도 정읍시",
        "coordinates": {"lat": 35.5000, "lng": 126.9000},
        "tags": ["Forest", "High-Activity", "Water", "Traditional-Pattern"],
        "description": "한국 단풍의 대명사로 불리는 국립공원. 울창한 숲과 계곡, 전통 사찰이 어우러진 명소.",
        "mentalFit": {"stressReductionRate": 86, "energyBoostRate": 82},
        "pet_friendly": False, "walking_routes": [
            {"name": "내장사 탐방로", "distance_km": 3.0, "duration_minutes": 60, "difficulty": "보통", "description": "내장사까지 이어지는 단풍 명소 코스"}
        ], "seasonal_highlights": {"spring": "진달래와 벚꽃", "summer": "계곡과 숲", "autumn": "단풍 절경", "winter": "설경"}
    },
    {
        "id": "garden_042", "name": "지리산국립공원 (전북)", "region": "Jeonbuk", "location": "전라북도 남원시",
        "coordinates": {"lat": 35.3500, "lng": 127.6000},
        "tags": ["Forest", "High-Activity", "Water", "Traditional-Pattern"],
        "description": "한국 최초의 국립공원이자 영산. 천년 고찰과 울창한 원시림, 계곡이 어우러진 치유의 공간.",
        "mentalFit": {"stressReductionRate": 90, "energyBoostRate": 88},
        "pet_friendly": False, "walking_routes": [
            {"name": "피아골 탐방로", "distance_km": 4.0, "duration_minutes": 90, "difficulty": "보통", "description": "지리산 피아골 계곡을 따라 걷는 코스"}
        ], "seasonal_highlights": {"spring": "진달래와 철쭉", "summer": "원시림과 계곡", "autumn": "단풍 절경", "winter": "설경과 상고대"}
    },
    {
        "id": "garden_043", "name": "전주 한옥마을", "region": "Jeonbuk", "location": "전라북도 전주시",
        "coordinates": {"lat": 35.8100, "lng": 127.1500},
        "tags": ["Traditional-Pattern", "Low-Activity", "Pet-Friendly"],
        "description": "800여 채의 한옥이 밀집한 국내 최대 한옥 마을. 전통 정원과 골목길이 정겨운 공간.",
        "mentalFit": {"stressReductionRate": 72, "energyBoostRate": 68},
        "pet_friendly": True, "walking_routes": [
            {"name": "한옥마을 골목길", "distance_km": 2.0, "duration_minutes": 50, "difficulty": "쉬움", "description": "한옥마을을 둘러보는 골목길 산책"}
        ], "seasonal_highlights": {"spring": "벚꽃과 매화", "summer": "녹음과 전통 정원", "autumn": "단풍과 한옥", "winter": "설경 속 한옥 마을"}
    },
    {
        "id": "garden_044", "name": "변산반도국립공원", "region": "Jeonbuk", "location": "전라북도 부안군",
        "coordinates": {"lat": 35.6000, "lng": 126.6000},
        "tags": ["Forest", "Water", "High-Activity"],
        "description": "서해안의 아름다운 해안선과 울창한 숲이 어우러진 국립공원. 내소사와 채석강이 유명하다.",
        "mentalFit": {"stressReductionRate": 80, "energyBoostRate": 78},
        "pet_friendly": False, "walking_routes": [
            {"name": "내소사 숲길", "distance_km": 2.5, "duration_minutes": 45, "difficulty": "쉬움", "description": "내소사까지 이어지는 울창한 숲길"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "해변과 숲", "autumn": "단풍과 서해", "winter": "설경과 겨울 바다"}
    },
    {
        "id": "garden_045", "name": "무주구천동", "region": "Jeonbuk", "location": "전라북도 무주군",
        "coordinates": {"lat": 35.9500, "lng": 127.7000},
        "tags": ["Forest", "Water", "High-Activity"],
        "description": "덕유산 자락의 아름다운 계곡. 맑은 물과 울창한 숲이 어우러진 치유 공간.",
        "mentalFit": {"stressReductionRate": 82, "energyBoostRate": 80},
        "pet_friendly": False, "walking_routes": [
            {"name": "구천동 계곡길", "distance_km": 3.5, "duration_minutes": 70, "difficulty": "보통", "description": "구천동 계곡을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "진달래와 철쭉", "summer": "계곡 물놀이", "autumn": "단풍", "winter": "설경과 스키"}
    },

    # ===== 전라남도 (Jeonnam) =====
    {
        "id": "garden_046", "name": "순천만국가정원", "region": "Jeonnam", "location": "전라남도 순천시",
        "coordinates": {"lat": 34.9267, "lng": 127.5025},
        "tags": ["Forest", "Water", "Low-Activity", "Traditional-Pattern", "Pet-Friendly"],
        "description": "한국 최초의 국가정원. 세계 각국의 정원과 전통 정원, 순천만 갯벌이 어우러진 세계적인 명소.",
        "mentalFit": {"stressReductionRate": 90, "energyBoostRate": 78},
        "pet_friendly": True, "walking_routes": [
            {"name": "국가정원 탐방로", "distance_km": 4.0, "duration_minutes": 80, "difficulty": "쉬움", "description": "순천만국가정원을 둘러보는 메인 코스"}
        ], "seasonal_highlights": {"spring": "튤립과 벚꽃", "summer": "수국과 연꽃", "autumn": "국화와 단풍", "winter": "겨울 정원과 갈대"}
    },
    {
        "id": "garden_047", "name": "태화강국가정원", "region": "Jeonnam", "location": "울산광역시 중구",
        "coordinates": {"lat": 35.5500, "lng": 129.3100},
        "tags": ["Water", "Forest", "Low-Activity", "Pet-Friendly"],
        "description": "태화강변에 조성된 국가정원. 십리대숲과 수변 정원이 아름다운 도심 속 치유 공간.",
        "mentalFit": {"stressReductionRate": 85, "energyBoostRate": 72},
        "pet_friendly": True, "walking_routes": [
            {"name": "십리대숲길", "distance_km": 3.0, "duration_minutes": 50, "difficulty": "쉬움", "description": "태화강변 대나무 숲을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 유채꽃", "summer": "대숲 그늘", "autumn": "단풍과 갈대", "winter": "설경과 대숲"}
    },
    {
        "id": "garden_048", "name": "다도해해상국립공원", "region": "Jeonnam", "location": "전라남도 여수시",
        "coordinates": {"lat": 34.6000, "lng": 127.6000},
        "tags": ["Water", "High-Activity", "Forest"],
        "description": "한국에서 가장 아름다운 해상 국립공원. 수많은 섬과 해안선, 울창한 숲이 어우러진 절경.",
        "mentalFit": {"stressReductionRate": 85, "energyBoostRate": 85},
        "pet_friendly": False, "walking_routes": [
            {"name": "해안 탐방로", "distance_km": 3.0, "duration_minutes": 60, "difficulty": "보통", "description": "다도해 해안을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "유채꽃과 동백", "summer": "해수욕과 섬 여행", "autumn": "단풍과 다도해", "winter": "겨울 바다와 일출"}
    },
    {
        "id": "garden_049", "name": "여수 오동도", "region": "Jeonnam", "location": "전라남도 여수시",
        "coordinates": {"lat": 34.7400, "lng": 127.7500},
        "tags": ["Forest", "Water", "Low-Activity", "Traditional-Pattern"],
        "description": "여수 앞바다의 작은 섬. 동백나무 숲과 해안 산책로가 아름다운 명소.",
        "mentalFit": {"stressReductionRate": 78, "energyBoostRate": 70},
        "pet_friendly": True, "walking_routes": [
            {"name": "오동도 둘레길", "distance_km": 1.8, "duration_minutes": 35, "difficulty": "쉬움", "description": "오동도를 한 바퀴 도는 해안 산책로"}
        ], "seasonal_highlights": {"spring": "동백꽃과 벚꽃", "summer": "해안 산책", "autumn": "단풍과 바다", "winter": "동백꽃 절정"}
    },
    {
        "id": "garden_050", "name": "보성 녹차밭", "region": "Jeonnam", "location": "전라남도 보성군",
        "coordinates": {"lat": 34.7700, "lng": 127.0800},
        "tags": ["Forest", "Low-Activity", "Traditional-Pattern"],
        "description": "한국 최대의 녹차 재배지. 끝없이 펼쳐진 녹차밭이 장관을 이루는 치유 공간.",
        "mentalFit": {"stressReductionRate": 82, "energyBoostRate": 72},
        "pet_friendly": True, "walking_routes": [
            {"name": "녹차밭 산책로", "distance_km": 2.0, "duration_minutes": 40, "difficulty": "쉬움", "description": "녹차밭 사이를 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "새순이 돋는 녹차밭", "summer": "푸른 녹차밭", "autumn": "황금빛 녹차밭", "winter": "설경 속 녹차밭"}
    },
    {
        "id": "garden_051", "name": "담양 죽녹원", "region": "Jeonnam", "location": "전라남도 담양군",
        "coordinates": {"lat": 35.3200, "lng": 126.9800},
        "tags": ["Forest", "Low-Activity", "Traditional-Pattern"],
        "description": "울창한 대나무 숲이 조성된 치유 공간. 대나무 사이로 걷는 산책로가 피톤치드 가득한 명소.",
        "mentalFit": {"stressReductionRate": 88, "energyBoostRate": 70},
        "pet_friendly": False, "walking_routes": [
            {"name": "죽녹원 탐방로", "distance_km": 2.0, "duration_minutes": 40, "difficulty": "쉬움", "description": "대나무 숲을 거니는 산책로"}
        ], "seasonal_highlights": {"spring": "죽순과 벚꽃", "summer": "시원한 대숲", "autumn": "대숲과 단풍", "winter": "설경 속 대나무"}
    },
    {
        "id": "garden_052", "name": "해남 두륜산", "region": "Jeonnam", "location": "전라남도 해남군",
        "coordinates": {"lat": 34.5500, "lng": 126.6000},
        "tags": ["Forest", "High-Activity", "Traditional-Pattern"],
        "description": "천년 고찰 대흥사가 자리한 명산. 동백나무 숲과 울창한 원시림이 아름다운 영산.",
        "mentalFit": {"stressReductionRate": 82, "energyBoostRate": 80},
        "pet_friendly": False, "walking_routes": [
            {"name": "대흥사 탐방로", "distance_km": 3.0, "duration_minutes": 60, "difficulty": "보통", "description": "대흥사와 두륜산을 둘러보는 코스"}
        ], "seasonal_highlights": {"spring": "동백꽃과 진달래", "summer": "울창한 숲", "autumn": "단풍", "winter": "동백꽃 절정"}
    },
    {
        "id": "garden_053", "name": "완도 청해진", "region": "Jeonnam", "location": "전라남도 완도군",
        "coordinates": {"lat": 34.3200, "lng": 126.7500},
        "tags": ["Water", "Forest", "High-Activity"],
        "description": "장보고 대사가 세운 해양 기지. 아름다운 해안선과 동백나무 숲이 어우러진 명소.",
        "mentalFit": {"stressReductionRate": 76, "energyBoostRate": 74},
        "pet_friendly": True, "walking_routes": [
            {"name": "해안 산책로", "distance_km": 2.5, "duration_minutes": 45, "difficulty": "쉬움", "description": "완도 해안을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "동백꽃과 유채꽃", "summer": "해수욕", "autumn": "단풍과 바다", "winter": "겨울 바다"}
    },
    {
        "id": "garden_054", "name": "목포 유달산", "region": "Jeonnam", "location": "전라남도 목포시",
        "coordinates": {"lat": 34.7900, "lng": 126.3800},
        "tags": ["Forest", "Water", "High-Activity", "Traditional-Pattern"],
        "description": "목포의 상징이자 다도해가 한눈에 보이는 명산. 동백나무 숲과 기암괴석이 어우러진 명소.",
        "mentalFit": {"stressReductionRate": 74, "energyBoostRate": 76},
        "pet_friendly": True, "walking_routes": [
            {"name": "유달산 산책로", "distance_km": 2.5, "duration_minutes": 50, "difficulty": "보통", "description": "유달산 정상까지 이어지는 산책로"}
        ], "seasonal_highlights": {"spring": "동백꽃과 벚꽃", "summer": "해안 산책", "autumn": "단풍과 다도해", "winter": "겨울 바다 전망"}
    },
    {
        "id": "garden_055", "name": "영암 월출산", "region": "Jeonnam", "location": "전라남도 영암군",
        "coordinates": {"lat": 34.7700, "lng": 126.7000},
        "tags": ["Forest", "High-Activity", "Traditional-Pattern"],
        "description": "달이 뜨는 산이라는 뜻의 이름처럼 아름다운 영산. 도갑사와 기암괴석이 유명하다.",
        "mentalFit": {"stressReductionRate": 80, "energyBoostRate": 78},
        "pet_friendly": False, "walking_routes": [
            {"name": "월출산 탐방로", "distance_km": 3.5, "duration_minutes": 80, "difficulty": "보통", "description": "월출산 주요 명소를 둘러보는 코스"}
        ], "seasonal_highlights": {"spring": "진달래와 철쭉", "summer": "계곡과 숲", "autumn": "단풍", "winter": "설경"}
    },

    # ===== 경상북도 (Gyeongbuk) =====
    {
        "id": "garden_056", "name": "경주국립공원", "region": "Gyeongbuk", "location": "경상북도 경주시",
        "coordinates": {"lat": 35.8400, "lng": 129.2100},
        "tags": ["Traditional-Pattern", "Forest", "Low-Activity", "Water"],
        "description": "천년 고도 경주의 역사 유적과 자연이 어우러진 국립공원. 불국사, 석굴암, 보문호 등 명소.",
        "mentalFit": {"stressReductionRate": 82, "energyBoostRate": 72},
        "pet_friendly": True, "walking_routes": [
            {"name": "보문호 산책로", "distance_km": 3.0, "duration_minutes": 50, "difficulty": "쉬움", "description": "보문호를 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃 명소", "summer": "녹음과 호수", "autumn": "단풍과 유적", "winter": "설경 속 천년 고도"}
    },
    {
        "id": "garden_057", "name": "불국사", "region": "Gyeongbuk", "location": "경상북도 경주시",
        "coordinates": {"lat": 35.7900, "lng": 129.3300},
        "tags": ["Traditional-Pattern", "Low-Activity", "Forest"],
        "description": "유네스코 세계문화유산으로 등재된 천년 고찰. 아름다운 정원과 석조 문화재가 조화를 이루는 공간.",
        "mentalFit": {"stressReductionRate": 85, "energyBoostRate": 65},
        "pet_friendly": False, "walking_routes": [
            {"name": "불국사 탐방로", "distance_km": 1.5, "duration_minutes": 40, "difficulty": "쉬움", "description": "불국사 경내를 둘러보는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 진달래", "summer": "녹음과 연꽃", "autumn": "단풍 명소", "winter": "설경 속 고찰"}
    },
    {
        "id": "garden_058", "name": "주왕산국립공원", "region": "Gyeongbuk", "location": "경상북도 청송군",
        "coordinates": {"lat": 36.3800, "lng": 129.1500},
        "tags": ["Forest", "High-Activity", "Water"],
        "description": "기암괴석과 울창한 숲, 맑은 계곡이 어우러진 국립공원. 주왕계곡의 절경이 유명하다.",
        "mentalFit": {"stressReductionRate": 84, "energyBoostRate": 82},
        "pet_friendly": False, "walking_routes": [
            {"name": "주왕계곡 탐방로", "distance_km": 3.5, "duration_minutes": 70, "difficulty": "보통", "description": "주왕계곡을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "진달래와 벚꽃", "summer": "계곡 물놀이", "autumn": "단풍 절경", "winter": "설경과 겨울 계곡"}
    },
    {
        "id": "garden_059", "name": "소백산국립공원", "region": "Gyeongbuk", "location": "경상북도 영주시",
        "coordinates": {"lat": 36.9500, "lng": 128.4500},
        "tags": ["Forest", "High-Activity", "Traditional-Pattern"],
        "description": "부석사와 초암사 등 전통 사찰이 자리한 명산. 철쭉 군락지와 울창한 숲이 아름답다.",
        "mentalFit": {"stressReductionRate": 82, "energyBoostRate": 80},
        "pet_friendly": False, "walking_routes": [
            {"name": "소백산 철쭉길", "distance_km": 4.0, "duration_minutes": 90, "difficulty": "보통", "description": "소백산 정상까지 이어지는 철쭉 군락길"}
        ], "seasonal_highlights": {"spring": "철쭉과 진달래", "summer": "고원의 시원함", "autumn": "단풍과 억새", "winter": "설경과 상고대"}
    },
    {
        "id": "garden_060", "name": "안동 하회마을", "region": "Gyeongbuk", "location": "경상북도 안동시",
        "coordinates": {"lat": 36.5400, "lng": 128.5200},
        "tags": ["Traditional-Pattern", "Low-Activity", "Water"],
        "description": "유네스코 세계문화유산으로 등재된 전통 마을. 낙동강이 휘감아 도는 아름다운 풍경 속의 고택.",
        "mentalFit": {"stressReductionRate": 80, "energyBoostRate": 62},
        "pet_friendly": True, "walking_routes": [
            {"name": "하회마을 산책로", "distance_km": 2.0, "duration_minutes": 45, "difficulty": "쉬움", "description": "하회마을과 낙동강변을 걷는 코스"}
        ], "seasonal_highlights": {"spring": "벚꽃과 매화", "summer": "녹음과 강", "autumn": "단풍과 고택", "winter": "설경 속 전통 마을"}
    },
    {
        "id": "garden_061", "name": "문경새재", "region": "Gyeongbuk", "location": "경상북도 문경시",
        "coordinates": {"lat": 36.7600, "lng": 128.0800},
        "tags": ["Forest", "High-Activity", "Traditional-Pattern"],
        "description": "조선 시대 영남대로의 험준한 고개. 울창한 숲과 계곡, 옛길이 잘 보존된 역사 탐방로.",
        "mentalFit": {"stressReductionRate": 78, "energyBoostRate": 80},
        "pet_friendly": True, "walking_routes": [
            {"name": "새재 옛길", "distance_km": 3.5, "duration_minutes": 60, "difficulty": "보통", "description": "문경새재 옛길을 따라 걷는 역사 탐방로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "계곡과 숲", "autumn": "단풍 명소", "winter": "설경과 옛길"}
    },
    {
        "id": "garden_062", "name": "울진 금강소나무숲", "region": "Gyeongbuk", "location": "경상북도 울진군",
        "coordinates": {"lat": 36.9900, "lng": 129.4000},
        "tags": ["Forest", "Low-Activity", "Traditional-Pattern"],
        "description": "천년의 세월을 자랑하는 금강소나무 원시림. 피톤치드 가득한 한국 최고의 치유의 숲.",
        "mentalFit": {"stressReductionRate": 92, "energyBoostRate": 75},
        "pet_friendly": False, "walking_routes": [
            {"name": "금강소나무 숲길", "distance_km": 2.5, "duration_minutes": 45, "difficulty": "쉬움", "description": "천년 금강소나무 숲을 거니는 산책로"}
        ], "seasonal_highlights": {"spring": "소나무 새순", "summer": "울창한 송림", "autumn": "소나무와 단풍", "winter": "설경 속 소나무"}
    },
    {
        "id": "garden_063", "name": "포항 호미곶", "region": "Gyeongbuk", "location": "경상북도 포항시",
        "coordinates": {"lat": 36.0800, "lng": 129.5700},
        "tags": ["Water", "High-Activity", "Pet-Friendly"],
        "description": "한반도에서 가장 동쪽에 위치한 해안 명소. 해안 산책로와 등대, 일출이 아름다운 공간.",
        "mentalFit": {"stressReductionRate": 72, "energyBoostRate": 78},
        "pet_friendly": True, "walking_routes": [
            {"name": "해안 둘레길", "distance_km": 2.5, "duration_minutes": 40, "difficulty": "쉬움", "description": "호미곶 해안을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "유채꽃과 벚꽃", "summer": "해수욕과 일출", "autumn": "단풍과 동해", "winter": "일출과 설경"}
    },
    {
        "id": "garden_064", "name": "봉화 국립백두대간수목원", "region": "Gyeongbuk", "location": "경상북도 봉화군",
        "coordinates": {"lat": 36.9000, "lng": 128.8000},
        "tags": ["Forest", "High-Activity", "Water", "Traditional-Pattern"],
        "description": "백두대간의 생태계를 보존한 대규모 수목원. 다양한 테마 정원과 치유 프로그램이 운영된다.",
        "mentalFit": {"stressReductionRate": 88, "energyBoostRate": 80},
        "pet_friendly": False, "walking_routes": [
            {"name": "수목원 탐방로", "distance_km": 4.5, "duration_minutes": 90, "difficulty": "보통", "description": "백두대간수목원을 둘러보는 메인 코스"}
        ], "seasonal_highlights": {"spring": "철쭉과 진달래", "summer": "울창한 숲", "autumn": "단풍 명소", "winter": "설경과 겨울 정원"}
    },
    {
        "id": "garden_065", "name": "영덕 블루로드", "region": "Gyeongbuk", "location": "경상북도 영덕군",
        "coordinates": {"lat": 36.4100, "lng": 129.3800},
        "tags": ["Water", "High-Activity", "Pet-Friendly"],
        "description": "동해안을 따라 조성된 해안 산책로. 소나무 숲과 바다가 어우러진 아름다운 해안 길.",
        "mentalFit": {"stressReductionRate": 76, "energyBoostRate": 76},
        "pet_friendly": True, "walking_routes": [
            {"name": "블루로드 산책로", "distance_km": 3.0, "duration_minutes": 50, "difficulty": "쉬움", "description": "영덕 해안을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 유채꽃", "summer": "해수욕", "autumn": "단풍과 동해", "winter": "일출과 설경"}
    },

    # ===== 경상남도 (Gyeongnam) =====
    {
        "id": "garden_066", "name": "가야산국립공원", "region": "Gyeongnam", "location": "경상남도 합천군",
        "coordinates": {"lat": 35.8000, "lng": 128.1200},
        "tags": ["Forest", "High-Activity", "Traditional-Pattern"],
        "description": "천년 고찰 해인사와 팔만대장경이 자리한 영산. 울창한 숲과 계곡이 아름다운 명산.",
        "mentalFit": {"stressReductionRate": 85, "energyBoostRate": 82},
        "pet_friendly": False, "walking_routes": [
            {"name": "해인사 탐방로", "distance_km": 3.0, "duration_minutes": 60, "difficulty": "보통", "description": "해인사와 가야산을 둘러보는 코스"}
        ], "seasonal_highlights": {"spring": "진달래와 철쭉", "summer": "계곡과 숲", "autumn": "단풍 명소", "winter": "설경과 고찰"}
    },
    {
        "id": "garden_067", "name": "한려해상국립공원", "region": "Gyeongnam", "location": "경상남도 통영시",
        "coordinates": {"lat": 34.8500, "lng": 128.4300},
        "tags": ["Water", "High-Activity", "Forest"],
        "description": "한려수도의 아름다운 해안선과 섬들이 어우러진 해상 국립공원. 통영과 거제의 해안 절경.",
        "mentalFit": {"stressReductionRate": 82, "energyBoostRate": 82},
        "pet_friendly": False, "walking_routes": [
            {"name": "해안 탐방로", "distance_km": 3.5, "duration_minutes": 60, "difficulty": "보통", "description": "한려해안을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "유채꽃과 동백", "summer": "해수욕과 섬 여행", "autumn": "단풍과 바다", "winter": "겨울 바다와 일출"}
    },
    {
        "id": "garden_068", "name": "지리산국립공원 (경남)", "region": "Gyeongnam", "location": "경상남도 산청군",
        "coordinates": {"lat": 35.3000, "lng": 127.7000},
        "tags": ["Forest", "High-Activity", "Water", "Traditional-Pattern"],
        "description": "한국 최초의 국립공원. 천왕봉, 반야봉, 노고단 등 장엄한 산세와 원시림이 펼쳐진 영산.",
        "mentalFit": {"stressReductionRate": 92, "energyBoostRate": 90},
        "pet_friendly": False, "walking_routes": [
            {"name": "천왕봉 등산로", "distance_km": 5.0, "duration_minutes": 150, "difficulty": "어려움", "description": "지리산 최고봉 천왕봉까지 이어지는 코스"}
        ], "seasonal_highlights": {"spring": "진달래와 철쭉", "summer": "원시림과 계곡", "autumn": "단풍 절경", "winter": "설경과 상고대"}
    },
    {
        "id": "garden_069", "name": "통영 케이블카", "region": "Gyeongnam", "location": "경상남도 통영시",
        "coordinates": {"lat": 34.8200, "lng": 128.4200},
        "tags": ["Water", "Forest", "High-Activity"],
        "description": "한려수도를 한눈에 내려다보는 케이블카와 미륵산 자연휴양림. 해안과 숲이 어우러진 명소.",
        "mentalFit": {"stressReductionRate": 78, "energyBoostRate": 80},
        "pet_friendly": False, "walking_routes": [
            {"name": "미륵산 산책로", "distance_km": 2.5, "duration_minutes": 50, "difficulty": "보통", "description": "미륵산 정상까지 이어지는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 유채꽃", "summer": "해안 산책", "autumn": "단풍과 다도해", "winter": "겨울 바다 전망"}
    },
    {
        "id": "garden_070", "name": "거제 외도", "region": "Gyeongnam", "location": "경상남도 거제시",
        "coordinates": {"lat": 34.7800, "lng": 128.6500},
        "tags": ["Water", "Forest", "Low-Activity", "Traditional-Pattern"],
        "description": "동백나무와 다양한 열대 식물이 자라는 아름다운 섬 정원. 해상 국립공원의 보석.",
        "mentalFit": {"stressReductionRate": 85, "energyBoostRate": 75},
        "pet_friendly": False, "walking_routes": [
            {"name": "외도 탐방로", "distance_km": 1.5, "duration_minutes": 40, "difficulty": "쉬움", "description": "외도 정원을 둘러보는 산책로"}
        ], "seasonal_highlights": {"spring": "동백꽃과 유채꽃", "summer": "열대 정원", "autumn": "단풍과 바다", "winter": "동백꽃 절정"}
    },
    {
        "id": "garden_071", "name": "진주 남강", "region": "Gyeongnam", "location": "경상남도 진주시",
        "coordinates": {"lat": 35.1800, "lng": 128.0800},
        "tags": ["Water", "Low-Activity", "Traditional-Pattern", "Pet-Friendly"],
        "description": "진주성과 남강이 어우러진 도심 속 수변 공간. 축제와 전통 정원이 아름다운 명소.",
        "mentalFit": {"stressReductionRate": 72, "energyBoostRate": 65},
        "pet_friendly": True, "walking_routes": [
            {"name": "남강 산책로", "distance_km": 2.5, "duration_minutes": 40, "difficulty": "쉬움", "description": "남강변을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃 명소", "summer": "수변 산책", "autumn": "단풍과 축제", "winter": "설경과 성곽"}
    },
    {
        "id": "garden_072", "name": "함양 상림", "region": "Gyeongnam", "location": "경상남도 함양군",
        "coordinates": {"lat": 35.5200, "lng": 127.7200},
        "tags": ["Forest", "Low-Activity", "Traditional-Pattern"],
        "description": "천년의 역사를 가진 인공 숲. 고려 시대 조성된 숲이 지금까지 보존된 귀중한 자연 유산.",
        "mentalFit": {"stressReductionRate": 86, "energyBoostRate": 68},
        "pet_friendly": True, "walking_routes": [
            {"name": "상림 숲길", "distance_km": 2.0, "duration_minutes": 35, "difficulty": "쉬움", "description": "천년 숲을 거니는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "울창한 숲", "autumn": "단풍 명소", "winter": "설경 속 고목"}
    },
    {
        "id": "garden_073", "name": "밀양 얼음골", "region": "Gyeongnam", "location": "경상남도 밀양시",
        "coordinates": {"lat": 35.5000, "lng": 128.7500},
        "tags": ["Forest", "High-Activity", "Water"],
        "description": "여름에도 얼음이 어는 신비한 계곡. 울창한 숲과 기암괴석이 어우러진 명소.",
        "mentalFit": {"stressReductionRate": 78, "energyBoostRate": 76},
        "pet_friendly": False, "walking_routes": [
            {"name": "얼음골 계곡길", "distance_km": 2.0, "duration_minutes": 45, "difficulty": "보통", "description": "얼음골 계곡을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "진달래와 벚꽃", "summer": "시원한 계곡", "autumn": "단풍", "winter": "설경과 얼음"}
    },
    {
        "id": "garden_074", "name": "창원 주남저수지", "region": "Gyeongnam", "location": "경상남도 창원시",
        "coordinates": {"lat": 35.2500, "lng": 128.6500},
        "tags": ["Water", "Low-Activity", "Pet-Friendly"],
        "description": "철새 도래지로 유명한 대규모 저수지. 갈대밭과 수변 산책로가 아름다운 생태 공간.",
        "mentalFit": {"stressReductionRate": 76, "energyBoostRate": 65},
        "pet_friendly": True, "walking_routes": [
            {"name": "주남저수지 산책로", "distance_km": 3.0, "duration_minutes": 50, "difficulty": "쉬움", "description": "저수지와 갈대밭을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "철새와 유채꽃", "summer": "녹음과 수변", "autumn": "갈대와 철새", "winter": "겨울 철새와 설경"}
    },
    {
        "id": "garden_075", "name": "사천 비토섬", "region": "Gyeongnam", "location": "경상남도 사천시",
        "coordinates": {"lat": 34.9200, "lng": 128.0500},
        "tags": ["Water", "Low-Activity", "Pet-Friendly"],
        "description": "바다와 섬이 어우러진 아름다운 해안 마을. 동백나무 숲과 해안 산책로가 정겹다.",
        "mentalFit": {"stressReductionRate": 74, "energyBoostRate": 68},
        "pet_friendly": True, "walking_routes": [
            {"name": "비토섬 산책로", "distance_km": 1.8, "duration_minutes": 30, "difficulty": "쉬움", "description": "비토섬 해안을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "동백꽃과 유채꽃", "summer": "해안 산책", "autumn": "단풍과 바다", "winter": "겨울 바다"}
    },

    # ===== 제주도 (Jeju) =====
    {
        "id": "garden_076", "name": "한라산국립공원", "region": "Jeju", "location": "제주특별자치도 제주시",
        "coordinates": {"lat": 33.3600, "lng": 126.5300},
        "tags": ["Forest", "High-Activity", "Traditional-Pattern"],
        "description": "한국 최고봉이자 제주의 상징. 다양한 고산 식물과 울창한 원시림이 펼쳐진 영산.",
        "mentalFit": {"stressReductionRate": 90, "energyBoostRate": 92},
        "pet_friendly": False, "walking_routes": [
            {"name": "성판악 코스", "distance_km": 4.5, "duration_minutes": 120, "difficulty": "어려움", "description": "한라산 정상까지 이어지는 대표 등산로"}
        ], "seasonal_highlights": {"spring": "진달래와 철쭉", "summer": "고산 식물", "autumn": "단풍과 억새", "winter": "설경과 상고대"}
    },
    {
        "id": "garden_077", "name": "제주 올레길", "region": "Jeju", "location": "제주특별자치도 제주시",
        "coordinates": {"lat": 33.5000, "lng": 126.5200},
        "tags": ["Water", "Forest", "High-Activity", "Pet-Friendly"],
        "description": "제주 해안을 따라 조성된 대표적인 트레킹 코스. 오름, 바다, 숲이 어우러진 치유의 길.",
        "mentalFit": {"stressReductionRate": 85, "energyBoostRate": 85},
        "pet_friendly": True, "walking_routes": [
            {"name": "올레 7코스", "distance_km": 4.0, "duration_minutes": 70, "difficulty": "보통", "description": "제주 해안을 따라 걷는 올레길"}
        ], "seasonal_highlights": {"spring": "유채꽃과 벚꽃", "summer": "푸른 바다", "autumn": "억새와 단풍", "winter": "겨울 바다와 일출"}
    },
    {
        "id": "garden_078", "name": "성산일출봉", "region": "Jeju", "location": "제주특별자치도 서귀포시",
        "coordinates": {"lat": 33.4600, "lng": 126.9400},
        "tags": ["Water", "High-Activity", "Traditional-Pattern"],
        "description": "유네스코 세계자연유산으로 등재된 거대한 분화구. 일출과 해안 풍경이 장관인 명소.",
        "mentalFit": {"stressReductionRate": 80, "energyBoostRate": 85},
        "pet_friendly": False, "walking_routes": [
            {"name": "일출봉 등산로", "distance_km": 1.5, "duration_minutes": 35, "difficulty": "보통", "description": "성산일출봉 정상까지 이어지는 코스"}
        ], "seasonal_highlights": {"spring": "유채꽃과 벚꽃", "summer": "푸른 바다", "autumn": "억새와 일출", "winter": "일출과 겨울 바다"}
    },
    {
        "id": "garden_079", "name": "천지연폭포", "region": "Jeju", "location": "제주특별자치도 서귀포시",
        "coordinates": {"lat": 33.2500, "lng": 126.4200},
        "tags": ["Water", "Forest", "Low-Activity"],
        "description": "제주에서 가장 아름다운 폭포 중 하나. 울창한 아열대 숲과 폭포가 어우러진 치유 공간.",
        "mentalFit": {"stressReductionRate": 82, "energyBoostRate": 72},
        "pet_friendly": False, "walking_routes": [
            {"name": "폭포 산책로", "distance_km": 1.0, "duration_minutes": 25, "difficulty": "쉬움", "description": "천지연폭포를 둘러보는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "시원한 폭포", "autumn": "단풍", "winter": "겨울 폭포"}
    },
    {
        "id": "garden_080", "name": "비자림", "region": "Jeju", "location": "제주특별자치도 제주시",
        "coordinates": {"lat": 33.4800, "lng": 126.8000},
        "tags": ["Forest", "Low-Activity", "Traditional-Pattern"],
        "description": "500년 이상 된 비자나무 숲이 울창하게 우거진 천연 기념물. 피톤치드 가득한 치유의 숲.",
        "mentalFit": {"stressReductionRate": 88, "energyBoostRate": 70},
        "pet_friendly": False, "walking_routes": [
            {"name": "비자림 숲길", "distance_km": 1.5, "duration_minutes": 30, "difficulty": "쉬움", "description": "500년 비자나무 숲을 거니는 산책로"}
        ], "seasonal_highlights": {"spring": "새순과 꽃", "summer": "울창한 숲", "autumn": "비자 열매", "winter": "설경 속 상록수림"}
    },
    {
        "id": "garden_081", "name": "용두암", "region": "Jeju", "location": "제주특별자치도 제주시",
        "coordinates": {"lat": 33.5200, "lng": 126.5100},
        "tags": ["Water", "Low-Activity", "Pet-Friendly"],
        "description": "용이 승천하는 형상의 기암괴석. 제주 해안의 절경과 함께 걷는 산책로가 아름답다.",
        "mentalFit": {"stressReductionRate": 70, "energyBoostRate": 68},
        "pet_friendly": True, "walking_routes": [
            {"name": "용두암 해안길", "distance_km": 1.2, "duration_minutes": 25, "difficulty": "쉬움", "description": "용두암 해안을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "유채꽃과 벚꽃", "summer": "푸른 바다", "autumn": "단풍과 바다", "winter": "겨울 바다와 일몰"}
    },
    {
        "id": "garden_082", "name": "에코랜드", "region": "Jeju", "location": "제주특별자치도 제주시",
        "coordinates": {"lat": 33.4500, "lng": 126.6800},
        "tags": ["Forest", "Low-Activity", "Water", "Pet-Friendly"],
        "description": "곶자왈 숲을 테마로 한 친환경 테마파크. 기차를 타고 숲과 호수를 둘러보는 이색 경험.",
        "mentalFit": {"stressReductionRate": 78, "energyBoostRate": 72},
        "pet_friendly": True, "walking_routes": [
            {"name": "곶자왈 숲길", "distance_km": 2.0, "duration_minutes": 40, "difficulty": "쉬움", "description": "곶자왈 원시림을 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 유채꽃", "summer": "울창한 숲", "autumn": "단풍과 억새", "winter": "설경과 겨울 숲"}
    },
    {
        "id": "garden_083", "name": "휴애리 자연생활공원", "region": "Jeju", "location": "제주특별자치도 서귀포시",
        "coordinates": {"lat": 33.3000, "lng": 126.6000},
        "tags": ["Forest", "Water", "Low-Activity", "Traditional-Pattern"],
        "description": "제주의 자연을 그대로 살린 생태 공원. 동백꽃, 수국, 억새 등 사계절 꽃이 아름다운 정원.",
        "mentalFit": {"stressReductionRate": 80, "energyBoostRate": 72},
        "pet_friendly": False, "walking_routes": [
            {"name": "생태 공원길", "distance_km": 2.0, "duration_minutes": 40, "difficulty": "쉬움", "description": "휴애리 공원을 둘러보는 산책로"}
        ], "seasonal_highlights": {"spring": "동백꽃과 유채꽃", "summer": "수국 정원", "autumn": "억새와 단풍", "winter": "동백꽃 절정"}
    },
    {
        "id": "garden_084", "name": "마노르블랑", "region": "Jeju", "location": "제주특별자치도 서귀포시",
        "coordinates": {"lat": 33.2800, "lng": 126.3800},
        "tags": ["Forest", "Low-Activity", "Traditional-Pattern"],
        "description": "유럽풍 정원과 제주의 자연이 어우러진 아름다운 수목원. 다양한 테마 정원이 조성되어 있다.",
        "mentalFit": {"stressReductionRate": 82, "energyBoostRate": 70},
        "pet_friendly": False, "walking_routes": [
            {"name": "수목원 탐방로", "distance_km": 2.5, "duration_minutes": 50, "difficulty": "쉬움", "description": "마노르블랑 정원을 둘러보는 코스"}
        ], "seasonal_highlights": {"spring": "튤립과 벚꽃", "summer": "장미와 수국", "autumn": "국화와 단풍", "winter": "겨울 정원"}
    },
    {
        "id": "garden_085", "name": "사려니숲길", "region": "Jeju", "location": "제주특별자치도 제주시",
        "coordinates": {"lat": 33.4200, "lng": 126.6500},
        "tags": ["Forest", "Low-Activity", "Traditional-Pattern"],
        "description": "제주 곶자왈의 대표적인 숲길. 울창한 삼나무 숲과 다양한 식물이 어우러진 치유 공간.",
        "mentalFit": {"stressReductionRate": 86, "energyBoostRate": 72},
        "pet_friendly": False, "walking_routes": [
            {"name": "사려니 숲길", "distance_km": 3.0, "duration_minutes": 50, "difficulty": "쉬움", "description": "삼나무 숲을 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "새순과 꽃", "summer": "울창한 숲", "autumn": "단풍과 삼나무", "winter": "설경 속 숲"}
    },

    # ===== 골프 코스 / 스포츠 랜드스케이프 =====
    {
        "id": "garden_086", "name": "뉴서울컨트리클럽", "region": "Gyeonggi", "location": "경기도 가평군",
        "coordinates": {"lat": 37.8314, "lng": 127.5090},
        "tags": ["Forest", "High-Activity", "Pet-Friendly", "Traditional-Pattern"],
        "description": "48,500그루의 나무가 우거진 명문 골프장. 전통 한국 정원 양식의 조경과 산림욕이 결합된 치유 공간.",
        "mentalFit": {"stressReductionRate": 78, "energyBoostRate": 82},
        "pet_friendly": True, "walking_routes": [
            {"name": "숲속 치유 코스", "distance_km": 3.2, "duration_minutes": 50, "difficulty": "쉬움", "description": "소나무 숲을 따라 조성된 평탄한 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "울창한 숲 그늘", "autumn": "단풍 장관", "winter": "설경 속 소나무 숲"}
    },
    {
        "id": "garden_087", "name": "남서울컨트리클럽", "region": "Gyeonggi", "location": "경기도 용인시",
        "coordinates": {"lat": 37.2411, "lng": 127.1775},
        "tags": ["Forest", "High-Activity", "Pet-Friendly", "Traditional-Pattern"],
        "description": "36,200그루의 나무가 우거진 명문 골프장. 전통 약초 정원과 허브 아로마 테라피 프로그램 운영.",
        "mentalFit": {"stressReductionRate": 76, "energyBoostRate": 80},
        "pet_friendly": True, "walking_routes": [
            {"name": "약초 치유 산책로", "distance_km": 2.8, "duration_minutes": 45, "difficulty": "쉬움", "description": "약초 정원을 중심으로 조성된 치유 산책로"}
        ], "seasonal_highlights": {"spring": "목련과 산수유", "summer": "배롱나무 꽃", "autumn": "단풍과 국화", "winter": "설경 속 정원"}
    },
    {
        "id": "garden_088", "name": "베어크리크CC", "region": "Gyeonggi", "location": "경기도 가평군",
        "coordinates": {"lat": 37.7800, "lng": 127.4500},
        "tags": ["Forest", "High-Activity", "Water"],
        "description": "북한강을 조망하는 명문 골프장. 울창한 숲과 호수가 어우러진 품격 있는 공간.",
        "mentalFit": {"stressReductionRate": 75, "energyBoostRate": 80},
        "pet_friendly": False, "walking_routes": [
            {"name": "호수 산책로", "distance_km": 2.5, "duration_minutes": 40, "difficulty": "쉬움", "description": "북한강변을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "시원한 강바람", "autumn": "단풍 명소", "winter": "설경과 강"}
    },
    {
        "id": "garden_089", "name": "아시아나CC", "region": "Gyeonggi", "location": "경기도 양평군",
        "coordinates": {"lat": 37.5000, "lng": 127.5000},
        "tags": ["Forest", "High-Activity", "Water"],
        "description": "남한강변에 위치한 명문 골프장. 전통 정원 양식의 조경과 수변 산책로가 인상적인 공간.",
        "mentalFit": {"stressReductionRate": 74, "energyBoostRate": 78},
        "pet_friendly": False, "walking_routes": [
            {"name": "강변 산책로", "distance_km": 2.0, "duration_minutes": 35, "difficulty": "쉬움", "description": "남한강변을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 유채꽃", "summer": "강변 산책", "autumn": "단풍", "winter": "설경"}
    },
    {
        "id": "garden_090", "name": "블루원CC", "region": "Gyeonggi", "location": "경기도 용인시",
        "coordinates": {"lat": 37.2200, "lng": 127.2000},
        "tags": ["Forest", "High-Activity", "Water"],
        "description": "용인에 위치한 명문 골프장. 호수와 숲이 어우러진 아름다운 조경이 특징.",
        "mentalFit": {"stressReductionRate": 72, "energyBoostRate": 78},
        "pet_friendly": False, "walking_routes": [
            {"name": "호수 둘레길", "distance_km": 2.2, "duration_minutes": 35, "difficulty": "쉬움", "description": "클럽하우스 주변 호수를 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "호수와 숲", "autumn": "단풍", "winter": "설경"}
    },
    {
        "id": "garden_091", "name": "여주CC", "region": "Gyeonggi", "location": "경기도 여주시",
        "coordinates": {"lat": 37.3000, "lng": 127.6500},
        "tags": ["Forest", "High-Activity", "Traditional-Pattern"],
        "description": "남한강변에 위치한 전통 양식의 골프장. 소나무 숲과 전통 정원이 어우러진 품격 있는 공간.",
        "mentalFit": {"stressReductionRate": 74, "energyBoostRate": 76},
        "pet_friendly": False, "walking_routes": [
            {"name": "소나무 숲길", "distance_km": 2.0, "duration_minutes": 35, "difficulty": "쉬움", "description": "소나무 숲을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "소나무 그늘", "autumn": "단풍", "winter": "설경"}
    },
    {
        "id": "garden_092", "name": "골드CC", "region": "Gyeonggi", "location": "경기도 파주시",
        "coordinates": {"lat": 37.8000, "lng": 126.7800},
        "tags": ["Forest", "High-Activity", "Water"],
        "description": "임진강변에 위치한 골프장. 넓은 페어웨이와 울창한 숲이 어우러진 공간.",
        "mentalFit": {"stressReductionRate": 70, "energyBoostRate": 76},
        "pet_friendly": False, "walking_routes": [
            {"name": "임진강 산책로", "distance_km": 2.5, "duration_minutes": 40, "difficulty": "쉬움", "description": "임진강변을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "강변 산책", "autumn": "단풍", "winter": "설경"}
    },
    {
        "id": "garden_093", "name": "대구CC", "region": "Gyeongbuk", "location": "경상북도 경산시",
        "coordinates": {"lat": 35.8200, "lng": 128.7500},
        "tags": ["Forest", "High-Activity", "Traditional-Pattern"],
        "description": "팔공산 자락에 위치한 골프장. 소나무 숲과 암석이 어우러진 한국적 조경이 돋보인다.",
        "mentalFit": {"stressReductionRate": 72, "energyBoostRate": 76},
        "pet_friendly": False, "walking_routes": [
            {"name": "팔공산 숲길", "distance_km": 2.0, "duration_minutes": 35, "difficulty": "쉬움", "description": "팔공산 자락을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "울창한 숲", "autumn": "단풍", "winter": "설경"}
    },
    {
        "id": "garden_094", "name": "부산CC", "region": "Gyeongnam", "location": "경상남도 김해시",
        "coordinates": {"lat": 35.2300, "lng": 128.8800},
        "tags": ["Forest", "High-Activity", "Water"],
        "description": "낙동강 하구를 조망하는 골프장. 해안과 숲이 어우러진 독특한 조경이 특징.",
        "mentalFit": {"stressReductionRate": 72, "energyBoostRate": 78},
        "pet_friendly": False, "walking_routes": [
            {"name": "낙동강 산책로", "distance_km": 2.5, "duration_minutes": 40, "difficulty": "쉬움", "description": "낙동강변을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 유채꽃", "summer": "강변 산책", "autumn": "단풍", "winter": "설경"}
    },
    {
        "id": "garden_095", "name": "광주CC", "region": "Jeonnam", "location": "광주광역시 북구",
        "coordinates": {"lat": 35.1700, "lng": 126.9000},
        "tags": ["Forest", "High-Activity", "Traditional-Pattern"],
        "description": "무등산 자락에 위치한 골프장. 울창한 숲과 전통 양식의 조경이 어우러진 공간.",
        "mentalFit": {"stressReductionRate": 72, "energyBoostRate": 76},
        "pet_friendly": False, "walking_routes": [
            {"name": "무등산 숲길", "distance_km": 2.0, "duration_minutes": 35, "difficulty": "쉬움", "description": "무등산 자락을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "울창한 숲", "autumn": "단풍", "winter": "설경"}
    },

    # ===== 추가 도시 공원 및 명소 =====
    {
        "id": "garden_096", "name": "인천 송도센트럴파크", "region": "Incheon", "location": "인천광역시 연수구",
        "coordinates": {"lat": 37.3900, "lng": 126.6400},
        "tags": ["Water", "Low-Activity", "Pet-Friendly"],
        "description": "송도 국제도시의 중심에 위치한 대규모 수변 공원. 바닷물을 끌어들인 운하와 다양한 테마 정원.",
        "mentalFit": {"stressReductionRate": 72, "energyBoostRate": 68},
        "pet_friendly": True, "walking_routes": [
            {"name": "센트럴파크 산책로", "distance_km": 3.0, "duration_minutes": 50, "difficulty": "쉬움", "description": "운하와 정원을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 유채꽃", "summer": "수변 산책", "autumn": "단풍", "winter": "설경과 겨울 정원"}
    },
    {
        "id": "garden_097", "name": "대전 엑스포공원", "region": "Daejeon", "location": "대전광역시 유성구",
        "coordinates": {"lat": 36.3800, "lng": 127.3800},
        "tags": ["Forest", "Water", "Low-Activity", "Pet-Friendly"],
        "description": "1993년 대전 엑스포 개최지에 조성된 대규모 공원. 다양한 테마 정원과 호수가 어우러진 공간.",
        "mentalFit": {"stressReductionRate": 74, "energyBoostRate": 70},
        "pet_friendly": True, "walking_routes": [
            {"name": "엑스포 공원길", "distance_km": 2.5, "duration_minutes": 45, "difficulty": "쉬움", "description": "엑스포공원을 둘러보는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "호수와 숲", "autumn": "단풍", "winter": "설경"}
    },
    {
        "id": "garden_098", "name": "울산 대왕암공원", "region": "Ulsan", "location": "울산광역시 동구",
        "coordinates": {"lat": 35.5000, "lng": 129.4300},
        "tags": ["Water", "Forest", "High-Activity", "Pet-Friendly"],
        "description": "동해안의 아름다운 해안선과 소나무 숲이 어우러진 공원. 해안 산책로와 기암괴석이 장관.",
        "mentalFit": {"stressReductionRate": 76, "energyBoostRate": 78},
        "pet_friendly": True, "walking_routes": [
            {"name": "대왕암 해안길", "distance_km": 2.5, "duration_minutes": 45, "difficulty": "쉬움", "description": "대왕암 해안을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 유채꽃", "summer": "해안 산책", "autumn": "단풍과 동해", "winter": "일출과 설경"}
    },
    {
        "id": "garden_099", "name": "세종 호수공원", "region": "Sejong", "location": "세종특별자치시",
        "coordinates": {"lat": 36.5000, "lng": 127.2500},
        "tags": ["Water", "Low-Activity", "Pet-Friendly"],
        "description": "세종시의 중심에 위치한 대규모 호수 공원. 수변 산책로와 다양한 편의 시설이 잘 갖춰진 도심 속 휴식처.",
        "mentalFit": {"stressReductionRate": 72, "energyBoostRate": 65},
        "pet_friendly": True, "walking_routes": [
            {"name": "호수 둘레길", "distance_km": 3.5, "duration_minutes": 55, "difficulty": "쉬움", "description": "세종호수를 한 바퀴 도는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 유채꽃", "summer": "수변 산책", "autumn": "단풍", "winter": "설경과 겨울 호수"}
    },
    {
        "id": "garden_100", "name": "부산 용두산공원", "region": "Busan", "location": "부산광역시 중구",
        "coordinates": {"lat": 35.1000, "lng": 129.0300},
        "tags": ["Traditional-Pattern", "Low-Activity", "Water"],
        "description": "부산 원도심의 중심에 위치한 공원. 부산타워와 전통 정원, 해안 전망이 어우러진 명소.",
        "mentalFit": {"stressReductionRate": 70, "energyBoostRate": 68},
        "pet_friendly": True, "walking_routes": [
            {"name": "용두산 산책로", "distance_km": 1.5, "duration_minutes": 30, "difficulty": "쉬움", "description": "용두산공원을 둘러보는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 진달래", "summer": "해안 산책", "autumn": "단풍과 부산항", "winter": "겨울 바다 전망"}
    },
    {
        "id": "garden_101", "name": "부산 해운대해수욕장", "region": "Busan", "location": "부산광역시 해운대구",
        "coordinates": {"lat": 35.1600, "lng": 129.1600},
        "tags": ["Water", "High-Activity", "Pet-Friendly"],
        "description": "한국을 대표하는 해수욕장. 해안 산책로와 동백섬, 달맞이길이 어우러진 명소.",
        "mentalFit": {"stressReductionRate": 74, "energyBoostRate": 80},
        "pet_friendly": True, "walking_routes": [
            {"name": "해운대 해안길", "distance_km": 2.5, "duration_minutes": 40, "difficulty": "쉬움", "description": "해운대 해안을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 유채꽃", "summer": "해수욕", "autumn": "단풍과 바다", "winter": "겨울 바다와 일출"}
    },
    {
        "id": "garden_102", "name": "부산 태종대", "region": "Busan", "location": "부산광역시 영도구",
        "coordinates": {"lat": 35.0500, "lng": 129.0800},
        "tags": ["Water", "Forest", "High-Activity", "Pet-Friendly"],
        "description": "부산 영도의 아름다운 해안 절경. 소나무 숲과 기암괴석, 해안 산책로가 어우러진 명소.",
        "mentalFit": {"stressReductionRate": 78, "energyBoostRate": 80},
        "pet_friendly": True, "walking_routes": [
            {"name": "태종대 해안길", "distance_km": 3.0, "duration_minutes": 50, "difficulty": "보통", "description": "태종대 해안을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 동백", "summer": "해안 산책", "autumn": "단풍과 바다", "winter": "일출과 겨울 바다"}
    },
    {
        "id": "garden_103", "name": "대구 앞산공원", "region": "Daegu", "location": "대구광역시 남구",
        "coordinates": {"lat": 35.8200, "lng": 128.5800},
        "tags": ["Forest", "High-Activity", "Traditional-Pattern"],
        "description": "대구의 진산으로 사랑받는 앞산. 울창한 숲과 계곡, 전통 정자가 어우러진 도심 속 치유 공간.",
        "mentalFit": {"stressReductionRate": 76, "energyBoostRate": 76},
        "pet_friendly": True, "walking_routes": [
            {"name": "앞산 둘레길", "distance_km": 3.5, "duration_minutes": 60, "difficulty": "보통", "description": "앞산을 한 바퀴 도는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 진달래", "summer": "계곡과 숲", "autumn": "단풍", "winter": "설경"}
    },
    {
        "id": "garden_104", "name": "대구 두류공원", "region": "Daegu", "location": "대구광역시 달서구",
        "coordinates": {"lat": 35.8500, "lng": 128.5500},
        "tags": ["Forest", "Water", "Low-Activity", "Pet-Friendly"],
        "description": "대구의 대표적인 도심 공원. 호수와 숲, 다양한 테마 정원이 어우러진 가족형 휴식 공간.",
        "mentalFit": {"stressReductionRate": 72, "energyBoostRate": 68},
        "pet_friendly": True, "walking_routes": [
            {"name": "두류공원 산책로", "distance_km": 2.5, "duration_minutes": 40, "difficulty": "쉬움", "description": "두류공원을 둘러보는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "호수와 숲", "autumn": "단풍", "winter": "설경"}
    },
    {
        "id": "garden_105", "name": "광주 무등산국립공원", "region": "Jeonnam", "location": "광주광역시 북구",
        "coordinates": {"lat": 35.1300, "lng": 126.9800},
        "tags": ["Forest", "High-Activity", "Traditional-Pattern"],
        "description": "광주의 상징이자 영산. 정상의 주상절리와 울창한 숲, 계곡이 어우러진 명산.",
        "mentalFit": {"stressReductionRate": 84, "energyBoostRate": 82},
        "pet_friendly": False, "walking_routes": [
            {"name": "무등산 탐방로", "distance_km": 4.0, "duration_minutes": 90, "difficulty": "보통", "description": "무등산 정상까지 이어지는 탐방로"}
        ], "seasonal_highlights": {"spring": "진달래와 철쭉", "summer": "계곡과 숲", "autumn": "단풍 명소", "winter": "설경과 주상절리"}
    },
    {
        "id": "garden_106", "name": "제주 석부작박물관", "region": "Jeju", "location": "제주특별자치도 서귀포시",
        "coordinates": {"lat": 33.3200, "lng": 126.3500},
        "tags": ["Traditional-Pattern", "Low-Activity", "Forest"],
        "description": "제주 돌문화와 전통 정원이 어우러진 독특한 공간. 돌 위에 핀 꽃과 분재 정원이 아름답다.",
        "mentalFit": {"stressReductionRate": 80, "energyBoostRate": 65},
        "pet_friendly": False, "walking_routes": [
            {"name": "석부작 정원길", "distance_km": 1.5, "duration_minutes": 35, "difficulty": "쉬움", "description": "석부작 정원을 둘러보는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "녹음과 돌 정원", "autumn": "단풍과 국화", "winter": "겨울 정원"}
    },
    {
        "id": "garden_107", "name": "강릉 경포호", "region": "Gangwon", "location": "강원특별자치도 강릉시",
        "coordinates": {"lat": 37.8000, "lng": 128.9000},
        "tags": ["Water", "Forest", "Low-Activity", "Pet-Friendly"],
        "description": "동해안의 대표적인 석호. 호수 주변의 소나무 숲과 해안 산책로가 아름다운 명소.",
        "mentalFit": {"stressReductionRate": 78, "energyBoostRate": 72},
        "pet_friendly": True, "walking_routes": [
            {"name": "경포호 산책로", "distance_km": 3.0, "duration_minutes": 50, "difficulty": "쉬움", "description": "경포호를 한 바퀴 도는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃 명소", "summer": "호수와 바다", "autumn": "단풍과 호수", "winter": "설경과 겨울 호수"}
    },
    {
        "id": "garden_108", "name": "속초 영금정", "region": "Gangwon", "location": "강원특별자치도 속초시",
        "coordinates": {"lat": 38.2000, "lng": 128.5900},
        "tags": ["Water", "Low-Activity", "Traditional-Pattern"],
        "description": "동해안의 아름다운 해안 절경과 전통 정자가 어우러진 명소. 일출이 특히 아름답다.",
        "mentalFit": {"stressReductionRate": 76, "energyBoostRate": 72},
        "pet_friendly": True, "walking_routes": [
            {"name": "영금정 해안길", "distance_km": 1.2, "duration_minutes": 25, "difficulty": "쉬움", "description": "영금정 해안을 따라 걷는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 동해", "summer": "해안 산책", "autumn": "단풍과 바다", "winter": "일출과 설경"}
    },
    {
        "id": "garden_109", "name": "서천 국립생태원", "region": "Chungnam", "location": "충청남도 서천군",
        "coordinates": {"lat": 36.0800, "lng": 126.7000},
        "tags": ["Forest", "Water", "Low-Activity", "Pet-Friendly"],
        "description": "세계 각국의 생태계를 재현한 대규모 생태원. 열대, 사막, 지중해 등 다양한 기후대의 식물을 관찰할 수 있다.",
        "mentalFit": {"stressReductionRate": 82, "energyBoostRate": 72},
        "pet_friendly": True, "walking_routes": [
            {"name": "생태원 탐방로", "distance_km": 3.5, "duration_minutes": 70, "difficulty": "쉬움", "description": "국립생태원을 둘러보는 메인 코스"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "열대 정원", "autumn": "단풍과 국화", "winter": "겨울 정원"}
    },
    {
        "id": "garden_110", "name": "예산 덕산온천", "region": "Chungnam", "location": "충청남도 예산군",
        "coordinates": {"lat": 36.6800, "lng": 126.8000},
        "tags": ["Forest", "Water", "Low-Activity", "Traditional-Pattern"],
        "description": "조선 시대부터 내려온 온천 관광지. 울창한 숲과 온천, 전통 정원이 어우러진 치유 공간.",
        "mentalFit": {"stressReductionRate": 80, "energyBoostRate": 68},
        "pet_friendly": False, "walking_routes": [
            {"name": "온천 공원길", "distance_km": 1.5, "duration_minutes": 30, "difficulty": "쉬움", "description": "덕산온천 공원을 둘러보는 산책로"}
        ], "seasonal_highlights": {"spring": "벚꽃과 철쭉", "summer": "녹음과 온천", "autumn": "단풍", "winter": "겨울 온천과 설경"}
    },
]

def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    output_path = os.path.join(DATA_DIR, 'nationalGardens.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(gardens, f, ensure_ascii=False, indent=2)
    print(f"Generated {len(gardens)} garden locations -> {output_path}")

if __name__ == '__main__':
    main()