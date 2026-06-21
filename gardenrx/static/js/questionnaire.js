// GardenRx AI Questionnaire Engine v2 - National Gardens Edition
let currentStep = 1;
const totalSteps = 5;

// User response data
let userData = {
    stress_level: 3,
    mood: 'neutral',
    preference: 'water_garden',
    activity_level: 'moderate',
    pet_friendly: false,
    garden_type: 'water_garden'
};

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    updateProgress();
    updateButtons();
});

function nextStep() {
    if (currentStep < totalSteps) {
        // Validate current step
        if (currentStep === 1) {
            userData.stress_level = parseInt(document.getElementById('stress-level').value);
        }
        
        document.querySelector(`.question-step[data-step="${currentStep}"]`).classList.remove('active');
        currentStep++;
        document.querySelector(`.question-step[data-step="${currentStep}"]`).classList.add('active');
        
        // Update progress
        document.querySelectorAll('.progress-step').forEach(el => {
            el.classList.toggle('active', parseInt(el.dataset.step) <= currentStep);
        });
        
        updateProgress();
        updateButtons();
        
        // Scroll to top of questionnaire
        document.querySelector('.questionnaire-container').scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
}

function prevStep() {
    if (currentStep > 1) {
        document.querySelector(`.question-step[data-step="${currentStep}"]`).classList.remove('active');
        currentStep--;
        document.querySelector(`.question-step[data-step="${currentStep}"]`).classList.add('active');
        
        document.querySelectorAll('.progress-step').forEach(el => {
            el.classList.toggle('active', parseInt(el.dataset.step) <= currentStep);
        });
        
        updateProgress();
        updateButtons();
    }
}

function updateProgress() {
    const fill = document.getElementById('progress-fill');
    const percentage = ((currentStep - 1) / (totalSteps - 1)) * 100;
    fill.style.width = `${percentage}%`;
}

function updateButtons() {
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    
    prevBtn.style.display = currentStep === 1 ? 'none' : 'inline-flex';
    
    if (currentStep === totalSteps) {
        nextBtn.style.display = 'none';
    } else {
        nextBtn.style.display = 'inline-flex';
    }
}

function updateStressValue(value) {
    document.getElementById('stress-value').textContent = `${value} / 5`;
    userData.stress_level = parseInt(value);
}

function selectMood(el) {
    document.querySelectorAll('.mood-card').forEach(c => c.classList.remove('selected'));
    el.classList.add('selected');
    userData.mood = el.dataset.value;
}

function selectPreference(el) {
    document.querySelectorAll('.pref-card').forEach(c => c.classList.remove('selected'));
    el.classList.add('selected');
    userData.preference = el.dataset.value;
    userData.garden_type = el.dataset.value;
}

function selectActivity(el) {
    document.querySelectorAll('.activity-card').forEach(c => c.classList.remove('selected'));
    el.classList.add('selected');
    userData.activity_level = el.dataset.value;
}

function updatePetFriendly(checked) {
    userData.pet_friendly = checked;
    const text = document.getElementById('pet-text');
    text.textContent = checked ? '🐾 반려동물과 함께 방문할 예정이에요!' : '반려동물과 함께 방문할 예정이에요 🐾';
}

function submitQuestionnaire() {
    const btn = document.getElementById('submit-btn');
    btn.disabled = true;
    btn.innerHTML = '⏳ 110곳의 데이터를 분석 중...';
    
    // Store data in session for prescription page
    sessionStorage.setItem('gardenrx_user_data', JSON.stringify(userData));
    
    fetch('/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(userData)
    })
    .then(res => res.json())
    .then(data => {
        // Store result in session storage
        sessionStorage.setItem('gardenrx_prescription', JSON.stringify(data));
        // Redirect to prescription page
        window.location.href = '/prescription';
    })
    .catch(err => {
        console.error('Error:', err);
        btn.disabled = false;
        btn.innerHTML = '🌱 AI 처방전 받기';
        alert('분석 중 오류가 발생했습니다. 다시 시도해주세요.');
    });
}

// Load prescription data on prescription page
document.addEventListener('DOMContentLoaded', function() {
    if (window.location.pathname === '/prescription') {
        loadPrescription();
    }
});

function loadPrescription() {
    const stored = sessionStorage.getItem('gardenrx_prescription');
    
    if (!stored) {
        // No data - redirect to questionnaire
        document.getElementById('prescription-loading').style.display = 'none';
        document.getElementById('prescription-result').innerHTML = `
            <div class="prescription-card" style="text-align:center;padding:40px;">
                <p style="margin-bottom:16px;">아직 진단 데이터가 없습니다.</p>
                <a href="/questionnaire" class="btn btn-primary">🌿 AI 진단 시작하기</a>
            </div>
        `;
        document.getElementById('prescription-result').style.display = 'block';
        return;
    }
    
    const data = JSON.parse(stored);
    
    // Simulate loading
    setTimeout(() => {
        displayPrescription(data);
    }, 1500);
}

function displayPrescription(data) {
    const loading = document.getElementById('prescription-loading');
    const result = document.getElementById('prescription-result');
    
    loading.style.display = 'none';
    result.style.display = 'block';
    
    const p = data.prescription;
    const garden = data.garden;
    const route = data.route;
    const folklore = data.folklore;
    const alternatives = data.alternatives || [];
    const totalGardens = data.totalGardens || 110;
    
    // Header
    document.getElementById('prescription-title').textContent = p.title;
    document.getElementById('prescription-meta').textContent = p.patient_summary;
    
    // Garden info
    document.getElementById('garden-name').textContent = garden.name;
    document.getElementById('garden-region').textContent = garden.location || garden.region;
    document.getElementById('garden-description').textContent = garden.description;
    
    // Tags
    document.getElementById('garden-tags').innerHTML = (garden.tags || []).map(t => 
        `<span class="tag-badge">${t}</span>`
    ).join('');
    
    // Mental Fit
    document.getElementById('stress-reduction').innerHTML = `
        <div class="mental-fit-bar">
            <div class="fit-label">스트레스 감소율</div>
            <div class="fit-bar-container">
                <div class="fit-bar fill-green" style="width:${garden.mentalFit.stressReductionRate}%"></div>
            </div>
            <div class="fit-value">${garden.mentalFit.stressReductionRate}%</div>
        </div>
    `;
    document.getElementById('energy-boost').innerHTML = `
        <div class="mental-fit-bar">
            <div class="fit-label">에너지 충전율</div>
            <div class="fit-bar-container">
                <div class="fit-bar fill-blue" style="width:${garden.mentalFit.energyBoostRate}%"></div>
            </div>
            <div class="fit-value">${garden.mentalFit.energyBoostRate}%</div>
        </div>
    `;
    
    // Analysis
    document.getElementById('stress-message').textContent = p.stress_message;
    document.getElementById('mood-message').textContent = p.mood_message;
    
    // Route
    if (route) {
        document.getElementById('route-info').innerHTML = `
            <h5 style="font-size:1rem;font-weight:700;margin-bottom:8px;">${route.name}</h5>
            <p style="color:var(--text-secondary);font-size:0.9rem;">${route.description}</p>
            <div style="display:flex;gap:16px;margin-top:8px;font-size:0.85rem;color:var(--text-muted);">
                <span>📏 ${route.distance_km}km</span>
                <span>⏱️ 약 ${route.duration_minutes}분</span>
                <span>📊 난이도: ${route.difficulty}</span>
            </div>
        `;
    } else {
        document.getElementById('route-info').innerHTML = `<p>경로 정보가 없습니다.</p>`;
    }
    
    // Route spots
    const spotsContainer = document.getElementById('route-spots');
    if (route && route.spots) {
        spotsContainer.innerHTML = '<h5 style="font-weight:600;margin-bottom:8px;">📍 코스 스팟</h5>';
        route.spots.forEach((spot, i) => {
            spotsContainer.innerHTML += `
                <div class="route-spot">
                    <div class="spot-marker">${String.fromCharCode(65 + i)}</div>
                    <div class="spot-detail">
                        <h5>${spot.name}</h5>
                        <p>${spot.description}</p>
                    </div>
                </div>
            `;
        });
    } else {
        spotsContainer.innerHTML = '';
    }
    
    // Folklore
    if (folklore) {
        document.getElementById('folklore-content').innerHTML = `
            <h5 style="font-weight:700;margin-bottom:8px;">📖 ${folklore.title}</h5>
            <p style="color:var(--text-secondary);font-size:0.9rem;line-height:1.7;">${folklore.healing_message}</p>
            <div style="margin-top:12px;padding:12px;background:var(--sage-50);border-radius:var(--radius-sm);font-size:0.85rem;">
                <strong>전통 수행법:</strong> ${folklore.traditional_practice}
            </div>
        `;
    } else {
        document.getElementById('folklore-content').innerHTML = `<p>관련 설화 정보가 없습니다.</p>`;
    }
    
    // Guide
    document.getElementById('guide-content').innerHTML = `
        <div style="line-height:2;">
            ${p.healing_instruction.split('\n').map(line => 
                line ? `<div>${line}</div>` : ''
            ).join('')}
        </div>
    `;
    
    // Seasonal
    document.getElementById('seasonal-content').innerHTML = `
        <p style="font-size:0.95rem;line-height:1.7;">${p.seasonal_tip}</p>
    `;
    
    // ===== ALTERNATIVE HEALING SPOTS GRID =====
    const altContainer = document.getElementById('alternative-spots');
    if (alternatives && alternatives.length > 0) {
        let altHtml = `
            <div class="alt-header">
                <span class="alt-badge">🏆 TOP 3 대체 치유 장소</span>
                <p class="alt-subtitle">110곳의 데이터베이스에서 당신에게 맞춤 추천된 장소들입니다</p>
            </div>
            <div class="alt-grid">
        `;
        alternatives.forEach((alt, idx) => {
            const rankEmojis = ['🥇', '🥈', '🥉'];
            altHtml += `
                <div class="alt-card">
                    <div class="alt-rank">${rankEmojis[idx] || '🏅'}</div>
                    <div class="alt-card-body">
                        <h5 class="alt-name">${alt.name}</h5>
                        <span class="alt-region">📍 ${alt.region}</span>
                        <p class="alt-desc">${alt.description}</p>
                        <div class="alt-tags">
                            ${(alt.tags || []).slice(0, 3).map(t => `<span class="alt-tag">${t}</span>`).join('')}
                        </div>
                        <div class="alt-scores">
                            <span class="alt-score stress">🧘 ${alt.stressReductionRate}%</span>
                            <span class="alt-score energy">⚡ ${alt.energyBoostRate}%</span>
                            ${alt.pet_friendly ? '<span class="alt-score pet">🐾 반려동물</span>' : ''}
                        </div>
                    </div>
                </div>
            `;
        });
        altHtml += '</div>';
        altContainer.innerHTML = altHtml;
    } else {
        altContainer.innerHTML = '';
    }
    
    // Dataset info
    document.getElementById('dataset-info').innerHTML = `
        <div class="dataset-badge">
            📊 <strong>${totalGardens}</strong>곳의 전국 정원 데이터베이스에서 분석 완료
        </div>
    `;
    
    // Store garden data for map
    sessionStorage.setItem('gardenrx_course', JSON.stringify(garden));
    sessionStorage.setItem('gardenrx_route', JSON.stringify(route));
}

// ===== Accordion Toggle Function =====
function toggleAccordion(id) {
  const content = document.getElementById(id);
  const allContents = document.querySelectorAll('.accordion-content');
  const allBtns = document.querySelectorAll('.accordion-btn');
  
  if (!content) return;
  
  // Check if this item is already open
  const isOpen = content.classList.contains('active');
  
  // Close all accordion items
  allContents.forEach(c => {
    c.classList.remove('active');
    c.style.maxHeight = '0';
    c.style.padding = '0 24px';
  });
  allBtns.forEach(b => b.classList.remove('active'));
  
  // If it wasn't open before, open it now
  if (!isOpen) {
    content.classList.add('active');
    content.style.maxHeight = content.scrollHeight + 60 + 'px';
    content.style.padding = '0 24px 24px';
    
    // Find the parent button and mark it active
    const parentBtn = content.closest('.accordion-item')?.querySelector('.accordion-btn');
    if (parentBtn) parentBtn.classList.add('active');
  }
}
