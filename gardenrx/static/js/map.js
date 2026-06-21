// GardenRx Interactive Map
let map;
let markers = [];
let polylines = [];
let currentFilter = 'all';

// Data from Flask (embedded via JSON)
const COURSES = [
    {
        "id": "golf_001",
        "name": "뉴서울컨트리클럽",
        "type": "course",
        "lat": 37.8314, "lng": 127.5090,
        "description": "경기도 가평군 | 수목 48,500주",
        "details": "프리미엄 골프 코스, 전통 정원 양식 조경",
        "pet_friendly": true,
        "walking_routes": [
            {
                "name": "숲속 치유 코스",
                "distance_km": 3.2,
                "duration_minutes": 50,
                "spots": [
                    {"name": "송림 입구", "lat": 37.8314, "lng": 127.5090, "description": "울창한 소나무 숲이 시작되는 지점"},
                    {"name": "약초원 전망대", "lat": 37.8330, "lng": 127.5110, "description": "다양한 약초를 관찰할 수 있는 전망대"},
                    {"name": "연못 정자", "lat": 37.8320, "lng": 127.5130, "description": "전통 연못과 정자가 있는 휴식 공간"},
                    {"name": "치유의 숲", "lat": 37.8300, "lng": 127.5100, "description": "피톤치드가 가득한 치유 공간"}
                ]
            }
        ]
    },
    {
        "id": "golf_002",
        "name": "남서울컨트리클럽",
        "type": "course",
        "lat": 37.2411, "lng": 127.1775,
        "description": "경기도 용인시 | 수목 36,200주",
        "details": "전통 정원, 약초 정원",
        "pet_friendly": true,
        "walking_routes": [
            {
                "name": "약초 치유 산책로",
                "distance_km": 2.8,
                "duration_minutes": 45,
                "spots": [
                    {"name": "약초 정원 입구", "lat": 37.2411, "lng": 127.1775, "description": "다양한 약초가 식재된 정원 입구"},
                    {"name": "허브 향기 정원", "lat": 37.2420, "lng": 127.1790, "description": "라벤더, 로즈마리 등 향기로운 허브 정원"},
                    {"name": "전통 연못", "lat": 37.2405, "lng": 127.1800, "description": "연꽃이 피는 전통 양식 연못"},
                    {"name": "숲속 쉼터", "lat": 37.2395, "lng": 127.1780, "description": "그늘 아래 벤치가 있는 휴식 공간"}
                ]
            }
        ]
    }
];

const PET_PLACES = [
    {
        "id": "pet_002",
        "name": "서울숲",
        "type": "park",
        "lat": 37.5449, "lng": 127.0392,
        "description": "서울 성동구 | 반려견 놀이터",
        "details": "대형/소형견 분리, 펫 워터파크",
        "pet_friendly": true
    },
    {
        "id": "pet_003",
        "name": "남산공원",
        "type": "park",
        "lat": 37.5512, "lng": 126.9882,
        "description": "서울 중구 | 반려동물 산책로",
        "details": "소형견 동반 가능",
        "pet_friendly": true
    },
    {
        "id": "pet_005",
        "name": "여의도공원",
        "type": "park",
        "lat": 37.5240, "lng": 126.9160,
        "description": "서울 영등포구 | 반려견 놀이터",
        "details": "잔디광장, 반려동물 음수대",
        "pet_friendly": true
    },
    {
        "id": "pet_006",
        "name": "하늘공원",
        "type": "park",
        "lat": 37.5675, "lng": 126.8866,
        "description": "서울 마포구 | 반려동물 탐방로",
        "details": "억새 명소, 전망대 펫 존",
        "pet_friendly": true
    }
];

const ALL_LOCATIONS = [...COURSES, ...PET_PLACES];

function initMap() {
    map = L.map('map', {
        center: [37.56, 127.00],
        zoom: 10,
        zoomControl: true,
        fadeAnimation: true
    });

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        maxZoom: 18
    }).addTo(map);

    addMarkers(ALL_LOCATIONS);

    const group = L.featureGroup(markers);
    if (markers.length > 0) {
        map.fitBounds(group.getBounds().pad(0.1));
    }

    // Load recommended route from session
    const courseData = sessionStorage.getItem('gardenrx_course');
    const routeData = sessionStorage.getItem('gardenrx_route');
    if (courseData && routeData) {
        try {
            const course = JSON.parse(courseData);
            const route = JSON.parse(routeData);
            showRouteOnMap(route, course);
        } catch(e) {}
    }
}

function addMarkers(locations) {
    locations.forEach(loc => {
        const isCourse = loc.type === 'course';
        const iconHtml = isCourse 
            ? '<div style="background:linear-gradient(135deg,#2DA82D,#238A23);width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-size:16px;box-shadow:0 2px 8px rgba(0,0,0,0.3);">🏌️</div>'
            : '<div style="background:linear-gradient(135deg,#4A6B4A,#3D5A3D);width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-size:16px;box-shadow:0 2px 8px rgba(0,0,0,0.3);">🌳</div>';
        
        const marker = L.marker([loc.lat, loc.lng], {
            icon: L.divIcon({
                html: iconHtml,
                className: 'custom-marker',
                iconSize: [32, 32],
                iconAnchor: [16, 16]
            })
        });

        marker.bindPopup(`
            <div style="min-width:200px;">
                <h4>${loc.name}</h4>
                <p>${loc.description}</p>
                ${loc.pet_friendly ? '<p style="color:#2DA82D;font-size:0.8rem;margin-top:4px;">🐾 반려동물 동반 가능</p>' : ''}
            </div>
        `);

        marker.on('click', () => showSidebar(loc));
        
        marker._gardenrx_data = loc;
        marker._gardenrx_filter = loc.type;
        markers.push(marker);
        marker.addTo(map);
    });
}

function showSidebar(loc) {
    const placeholder = document.querySelector('.sidebar-placeholder');
    const content = document.getElementById('sidebar-content');
    const details = document.getElementById('sidebar-details');
    
    placeholder.style.display = 'none';
    content.style.display = 'block';
    
    const isCourse = loc.type === 'course';
    
    let html = `
        <div style="text-align:center;margin-bottom:16px;">
            <div style="font-size:2.5rem;margin-bottom:8px;">${isCourse ? '🏌️' : '🌳'}</div>
            <h3 style="font-size:1.1rem;font-weight:700;">${loc.name}</h3>
            <p style="font-size:0.85rem;color:var(--text-secondary);">${loc.description}</p>
        </div>
        <div style="padding:12px;background:var(--sage-50);border-radius:var(--radius-sm);margin-bottom:12px;">
            <p style="font-size:0.85rem;">${loc.details}</p>
        </div>`;
    
    if (loc.pet_friendly) {
        html += `
            <div style="padding:12px;background:var(--mint-50);border-radius:var(--radius-sm);margin-bottom:12px;">
                <p style="font-size:0.85rem;color:var(--mint-600);">🐾 반려동물 동반 가능 공간</p>
            </div>`;
    }
    
    if (isCourse && loc.walking_routes) {
        html += `<h4 style="font-size:0.9rem;font-weight:700;margin-bottom:8px;">🚶 산책 코스</h4>`;
        loc.walking_routes.forEach((route, idx) => {
            html += `
                <div class="route-select-btn" data-loc-idx="${ALL_LOCATIONS.indexOf(loc)}" data-route-idx="${idx}" style="padding:12px;background:var(--bg-card);border:1px solid var(--sage-100);border-radius:var(--radius-sm);margin-bottom:8px;cursor:pointer;">
                    <h5 style="font-size:0.85rem;font-weight:600;">${route.name}</h5>
                    <p style="font-size:0.78rem;color:var(--text-muted);">📏 ${route.distance_km}km | ${route.spots.length}개 스팟</p>
                </div>`;
        });
    }
    
    details.innerHTML = html;
    
    // Attach click handlers for route buttons
    details.querySelectorAll('.route-select-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const locIdx = parseInt(this.dataset.locIdx);
            const routeIdx = parseInt(this.dataset.routeIdx);
            const location = ALL_LOCATIONS[locIdx];
            if (location && location.walking_routes[routeIdx]) {
                showRouteOnMap(location.walking_routes[routeIdx], location);
            }
        });
    });
    
    document.getElementById('map-info').innerHTML = `<span>📍 ${loc.name} - 상세 정보</span>`;
    document.getElementById('map-sidebar').style.animation = 'fadeIn 0.3s ease';
}

function closeSidebar() {
    document.querySelector('.sidebar-placeholder').style.display = 'flex';
    document.getElementById('sidebar-content').style.display = 'none';
    document.getElementById('map-info').innerHTML = '<span>📍 클릭하여 상세 정보를 확인하세요</span>';
}

function filterMap(filter) {
    currentFilter = filter;
    
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.filter === filter);
    });
    
    markers.forEach(marker => {
        const data = marker._gardenrx_data;
        let visible = false;
        
        if (filter === 'all') visible = true;
        else if (filter === 'course' && data.type === 'course') visible = true;
        else if (filter === 'park' && data.type === 'park') visible = true;
        else if (filter === 'pet' && data.pet_friendly) visible = true;
        
        if (visible) {
            map.addLayer(marker);
        } else {
            map.removeLayer(marker);
        }
    });
    
    clearRoutes();
}

function showRouteOnMap(route, course) {
    clearRoutes();
    
    if (!route.spots || route.spots.length < 2) return;
    
    const coords = route.spots.map(spot => [spot.lat, spot.lng]);
    
    const polyline = L.polyline(coords, {
        color: '#2DA82D',
        weight: 4,
        opacity: 0.8,
        dashArray: '10, 10',
        lineJoin: 'round'
    }).addTo(map);
    
    polylines.push(polyline);
    
    route.spots.forEach((spot, i) => {
        const markerColor = i === 0 ? '#2DA82D' : i === route.spots.length - 1 ? '#4A6B4A' : '#7FD47F';
        const spotIcon = L.divIcon({
            html: `<div style="background:${markerColor};width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-size:12px;font-weight:700;box-shadow:0 2px 8px rgba(0,0,0,0.3);border:3px solid white;">${String.fromCharCode(65 + i)}</div>`,
            className: 'spot-marker-icon',
            iconSize: [28, 28],
            iconAnchor: [14, 14]
        });
        
        const spotMarker = L.marker([spot.lat, spot.lng], { icon: spotIcon }).addTo(map);
        spotMarker.bindPopup(`<h4>${spot.name}</h4><p>${spot.description || ''}</p>`);
        polylines.push(spotMarker);
    });
    
    const bounds = L.latLngBounds(coords);
    map.fitBounds(bounds.pad(0.2));
    
    const preview = document.getElementById('route-preview');
    preview.style.display = 'block';
    document.getElementById('route-preview-title').textContent = `🚶 ${route.name} (${route.distance_km}km)`;
    
    const timeline = document.getElementById('route-timeline');
    timeline.innerHTML = '';
    route.spots.forEach((spot, i) => {
        const isStart = i === 0;
        const isEnd = i === route.spots.length - 1;
        timeline.innerHTML += `
            <div class="route-spot">
                <div class="spot-marker" style="background:${isStart ? 'var(--accent-primary)' : isEnd ? 'var(--sage-600)' : 'var(--mint-300)'};">${String.fromCharCode(65 + i)}</div>
                <div class="spot-detail">
                    <h5>${spot.name}</h5>
                    <p>${spot.description || ''}</p>
                </div>
            </div>`;
    });
    
    closeSidebar();
    document.querySelector('.map-container-wrapper').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function clearRoutes() {
    polylines.forEach(p => map.removeLayer(p));
    polylines = [];
    document.getElementById('route-preview').style.display = 'none';
}

document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('map')) {
        initMap();
    }
});