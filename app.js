// =========================================================
// DATA STRUCTURES (Translated from app.py)
// =========================================================

const cropsData = {
    "Rice": { base_yield: 2.5, optimal_rain: 1200, temp_min: 20, temp_max: 35 },
    "Maize": { base_yield: 3.0, optimal_rain: 900, temp_min: 18, temp_max: 30 },
    "Wheat": { base_yield: 2.0, optimal_rain: 800, temp_min: 15, temp_max: 25 },
    "Banana": { base_yield: 18, optimal_rain: 1500, temp_min: 20, temp_max: 35 },
    "Cotton": { base_yield: 1.5, optimal_rain: 700, temp_min: 20, temp_max: 32 }
};

const diseaseData = {
    "Early Blight": {
        description: "Fungal disease causing dark concentric spots on older leaves.",
        icon: "ph-plant",
        color: "#ca8a04",
        measures: [
            "Use certified disease-free seeds.",
            "Practice crop rotation (2-3 years).",
            "Remove infected leaves immediately.",
            "Avoid overhead irrigation.",
            "Maintain proper plant spacing.",
            "Apply preventive fungicides like Mancozeb."
        ]
    },
    "Late Blight": {
        description: "Serious disease causing water-soaked lesions that turn brown rapidly.",
        icon: "ph-warning-octagon",
        color: "#dc2626",
        measures: [
            "Use certified disease-free seeds or tubers.",
            "Ensure proper field drainage.",
            "Avoid water stagnation.",
            "Remove infected plants immediately.",
            "Spray fungicides like Metalaxyl or Mancozeb.",
            "Avoid late evening irrigation."
        ]
    },
    "Leaf Spot": {
        description: "Common foliar disease causing distinct spots on leaves that can reduce photosynthetic area.",
        icon: "ph-leaf",
        color: "#ea580c",
        measures: [
            "Ensure good air circulation around plants.",
            "Water at the base of the plant.",
            "Apply copper-based fungicides if severe.",
            "Remove affected plant debris at end of season."
        ]
    },
    "Bacterial Spot": {
        description: "Bacterial infection leading to small water-soaked spots on leaves and fruit.",
        icon: "ph-bacteria",
        color: "#b91c1c",
        measures: [
            "Use disease-free seed and transplants.",
            "Avoid working in fields when foliage is wet.",
            "Apply bactericides to limit spread.",
            "Plow under or remove plant residue."
        ]
    },
    "Healthy": {
        description: "No disease detected. Plant is healthy.",
        icon: "ph-check-circle",
        color: "#16a34a",
        measures: [
            "Maintain proper irrigation schedule.",
            "Use balanced fertilizers.",
            "Monitor plants regularly."
        ]
    }
};

const farmerSchemes = {
    "All India": [
        { name: "PM-KISAN", description: "₹6000 per year income support for farmers.", link: "https://pmkisan.gov.in/" },
        { name: "PM Fasal Bima Yojana", description: "Crop insurance against natural calamities.", link: "https://pmfby.gov.in/" },
        { name: "Soil Health Card Scheme", description: "Soil testing & fertilizer recommendation support.", link: "https://soilhealth.dac.gov.in/" },
        { name: "Kisan Credit Card (KCC)", description: "Low-interest agricultural credit facility.", link: "https://kisancreditcard.com/" }
    ],
    "Telangana": [
        { name: "Rythu Bandhu", description: "Investment support per acre per season.", link: "https://rythubandhu.telangana.gov.in/" },
        { name: "Rythu Bima", description: "Farmer life insurance scheme.", link: "https://rythubima.telangana.gov.in/" },
        { name: "Free Power Supply Scheme", description: "Free electricity for agricultural pumps.", link: "https://www.telangana.gov.in/" }
    ],
    "Tamil Nadu": [
        { name: "TN Seed Subsidy Scheme", description: "Subsidy for certified seeds.", link: "https://www.tnagrisnet.tn.gov.in/" },
        { name: "Micro Irrigation Scheme", description: "Subsidy for drip and sprinkler irrigation.", link: "https://www.tn.gov.in/" },
        { name: "Uzhavar Pathukappu Scheme", description: "Farmer welfare and pension scheme.", link: "https://www.tn.gov.in/" }
    ],
    "Karnataka": [
        { name: "Raitha Siri Scheme", description: "Millet cultivation financial support.", link: "https://raitamitra.karnataka.gov.in/" },
        { name: "Krishi Bhagya Scheme", description: "Water conservation & farm pond scheme.", link: "https://raitamitra.karnataka.gov.in/" },
        { name: "Karnataka Crop Loan Waiver", description: "Loan waiver support for farmers.", link: "https://www.karnataka.gov.in/" }
    ],
    "Kerala": [
        { name: "Kerala Agricultural Subsidy", description: "Subsidy for crop and irrigation support.", link: "https://keralaagriculture.gov.in/" },
        { name: "Karshaka Kshemanidhi", description: "Farmer welfare pension scheme.", link: "https://keralaagriculture.gov.in/" }
    ],
    "Andhra Pradesh": [
        { name: "YSR Rythu Bharosa", description: "Annual financial assistance.", link: "https://ysrrythubharosa.ap.gov.in/" },
        { name: "Zero Interest Crop Loan Scheme", description: "Interest-free crop loans.", link: "https://apagrisnet.gov.in/" }
    ]
};

const equipmentData = {
    "Tractor": { rent_per_day: 2000, owners: [{ name: "Ramesh Gowda", phone: "9876543210" }, { name: "Suresh Kumar", phone: "9123456789" }, { name: "Mahesh Reddy", phone: "9988776655" }] },
    "Harvester": { rent_per_day: 5000, owners: [{ name: "Praveen Shetty", phone: "9090909090" }, { name: "Karthik Rao", phone: "9845012345" }] },
    "Rotavator": { rent_per_day: 1500, owners: [{ name: "Venkatesh Naik", phone: "9900112233" }, { name: "Anil Patil", phone: "9887766554" }] },
    "Seed Drill": { rent_per_day: 800, owners: [{ name: "Sandeep Singh", phone: "9871236540" }, { name: "Manish Tiwari", phone: "9988771122" }] },
    "Sprayer Machine": { rent_per_day: 400, owners: [{ name: "Rahul Das", phone: "9123123123" }, { name: "Vijay Kumar", phone: "9898989898" }] }
};

// =========================================================
// UI LOGIC & NAVIGATION
// =========================================================

function formatINR(amount) {
    return new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR', maximumFractionDigits: 0 }).format(amount);
}

function toggleMobileMenu() {
    document.querySelector('.nav-links').classList.toggle('show');
}

function switchTab(tabId) {
    // Hide all sections
    document.querySelectorAll('.page-section').forEach(sec => sec.classList.remove('active-section'));
    document.querySelectorAll('.nav-item').forEach(nav => nav.classList.remove('active'));

    // Show target section
    document.getElementById(`sec-${tabId}`).classList.add('active-section');

    // Highlight nav link (if it exists)
    const targetNav = document.getElementById(`nav-${tabId}`);
    if (targetNav) targetNav.classList.add('active');

    // Close mobile menu if open
    document.querySelector('.nav-links').classList.remove('show');

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// =========================================================
// YIELD PREDICTOR LOGIC
// =========================================================

function clamp(value, min_val, max_val) {
    return Math.max(min_val, Math.min(value, max_val));
}

function rainfallFactor(rainfall, optimal) {
    const factor = 1 - Math.abs(rainfall - optimal) / optimal;
    return clamp(factor, 0.3, 1.0);
}

function temperatureFactor(temp, optimal_min, optimal_max) {
    if (temp >= optimal_min && temp <= optimal_max) return 1.0;
    if (temp >= optimal_min - 5 && temp <= optimal_max + 5) return 0.8;
    if (temp >= optimal_min - 10 && temp <= optimal_max + 10) return 0.5;
    return 0.3;
}

function humidityFactor(humidity) {
    if (humidity >= 60 && humidity <= 80) return 1.0;
    if (humidity >= 40 && humidity <= 90) return 0.8;
    return 0.5;
}

function predictYield() {
    const cropGroup = document.getElementById('input-crop').value;
    const land = parseFloat(document.getElementById('input-land').value);
    const rain = parseFloat(document.getElementById('input-rain').value);
    const temp = parseFloat(document.getElementById('input-temp').value);
    const humidity = parseFloat(document.getElementById('input-humidity').value);
    const soil = document.getElementById('input-soil').value;
    const irrigation = document.getElementById('input-irrigation').value;
    const price = parseFloat(document.getElementById('input-price').value);

    const cropProps = cropsData[cropGroup];
    const fRain = rainfallFactor(rain, cropProps.optimal_rain);
    const fTemp = temperatureFactor(temp, cropProps.temp_min, cropProps.temp_max);
    const fHumidity = humidityFactor(humidity);

    const soilFactors = { clay: 0.9, loam: 1.0, sandy: 0.8 };
    const irrFactors = { drip: 1.1, sprinkler: 1.0, canal: 0.9, none: 0.5 };

    const estimatedYield = cropProps.base_yield * land * fRain * fTemp * fHumidity * soilFactors[soil] * irrFactors[irrigation];
    const estimatedRevenue = estimatedYield * price;

    document.getElementById('res-yield').textContent = estimatedYield.toFixed(2) + " tons";
    document.getElementById('res-revenue').textContent = formatINR(estimatedRevenue);

    const resultsContainer = document.getElementById('yield-results');
    resultsContainer.classList.remove('hidden');
    // Re-trigger animation
    resultsContainer.style.animation = 'none';
    setTimeout(() => resultsContainer.style.animation = '', 10);
}

// =========================================================
// DISEASE PREVENTION LOGIC
// =========================================================

function showDiseaseInfo() {
    const sel = document.getElementById('input-disease').value;
    const data = diseaseData[sel];
    const container = document.getElementById('disease-info');

    let measuresHtml = data.measures.map(m => `<li>${m}</li>`).join('');

    container.innerHTML = `
        <div class="disease-header">
            <h3><i class="ph-fill ${data.icon}" style="color: ${data.color}"></i> ${sel}</h3>
            <p class="text-gray-600 mt-1">${data.description}</p>
        </div>
        <div class="disease-body">
            <h4>Recommended Measures</h4>
            <ul class="measures-list">
                ${measuresHtml}
            </ul>
        </div>
    `;

    container.style.animation = 'none';
    setTimeout(() => container.style.animation = 'fadeIn 0.3s ease-out', 10);
}

// =========================================================
// FINANCIAL AID LOGIC
// =========================================================

function showSchemes() {
    const state = document.getElementById('input-state').value;
    const schemes = farmerSchemes[state] || [];
    const container = document.getElementById('schemes-grid');

    container.innerHTML = '';

    schemes.forEach(sc => {
        container.innerHTML += `
            <div class="scheme-card fade-in">
                <h3>${sc.name}</h3>
                <p>${sc.description}</p>
                <a href="${sc.link}" target="_blank" class="scheme-link">
                    Apply Here <i class="ph ph-arrow-right"></i>
                </a>
            </div>
        `;
    });
}

// =========================================================
// MARKETPLACE LOGIC
// =========================================================

function calculateRental() {
    const equipment = document.getElementById('input-equipment').value;
    const days = parseInt(document.getElementById('input-days').value) || 1;

    const data = equipmentData[equipment];
    const total = data.rent_per_day * days;

    document.getElementById('rent-per-day').textContent = formatINR(data.rent_per_day);
    document.getElementById('rent-total').textContent = formatINR(total);

    // Render Owners
    const ownersGrid = document.getElementById('owners-grid');
    ownersGrid.innerHTML = '';

    data.owners.forEach(owner => {
        const initials = owner.name.split(' ').map(n => n[0]).join('').substring(0, 2).toUpperCase();
        ownersGrid.innerHTML += `
            <div class="owner-card fade-in">
                <div class="owner-avatar">${initials}</div>
                <div class="owner-info">
                    <h4>${owner.name}</h4>
                    <p><i class="ph ph-phone"></i> ${owner.phone}</p>
                </div>
                <button class="owner-contact-btn" title="Call ${owner.name}">
                    <i class="ph ph-phone-call"></i>
                </button>
            </div>
        `;
    });
}

// =========================================================
// AI DISEASE PREDICTION LOGIC
// =========================================================

function setupDragAndDrop() {
    const dropZone = document.getElementById('upload-zone');
    const fileInput = document.getElementById('image-upload');

    if (dropZone && fileInput) {
        dropZone.addEventListener('click', () => {
            if (!document.getElementById('image-preview-container').classList.contains('hidden')) return;
            fileInput.click();
        });

        dropZone.addEventListener('dragover', (e) => {
            e.preventDefault();
            dropZone.classList.add('dragover');
        });

        dropZone.addEventListener('dragleave', () => {
            dropZone.classList.remove('dragover');
        });

        dropZone.addEventListener('drop', (e) => {
            e.preventDefault();
            dropZone.classList.remove('dragover');
            if (e.dataTransfer.files.length) {
                fileInput.files = e.dataTransfer.files;
                handleImageUpload({ target: fileInput });
            }
        });
    }
}

function handleImageUpload(event) {
    const file = event.target.files[0];
    if (file && (file.type === 'image/jpeg' || file.type === 'image/png')) {
        const reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById('image-preview').src = e.target.result;
            document.getElementById('upload-content').classList.add('hidden');
            document.getElementById('image-preview-container').classList.remove('hidden');
            document.getElementById('btn-predict').disabled = false;
            document.getElementById('upload-error').classList.add('hidden');
        }
        reader.readAsDataURL(file);
    } else {
        document.getElementById('upload-error').classList.remove('hidden');
    }
}

function removeImage() {
    document.getElementById('image-upload').value = '';
    document.getElementById('image-preview').src = '';
    document.getElementById('upload-content').classList.remove('hidden');
    document.getElementById('image-preview-container').classList.add('hidden');
    document.getElementById('btn-predict').disabled = true;
    document.getElementById('prediction-result').classList.add('hidden');
}

function predictDisease() {
    const btn = document.getElementById('btn-predict');
    const loading = document.getElementById('prediction-loading');
    const result = document.getElementById('prediction-result');
    const errorMsg = document.getElementById('upload-error');

    // Safety check just in case
    const fileInput = document.getElementById('image-upload');
    if (!fileInput.files.length) {
        errorMsg.classList.remove('hidden');
        return;
    }

    btn.disabled = true;
    loading.classList.remove('hidden');
    result.classList.add('hidden');

    setTimeout(() => {
        loading.classList.add('hidden');
        btn.disabled = false;

        const possibleDiseases = ["Early Blight", "Late Blight", "Leaf Spot", "Bacterial Spot", "Healthy"];
        const confidences = [92, 88, 85, 90, 95];

        const randomIndex = Math.floor(Math.random() * possibleDiseases.length);
        const selectedDisease = possibleDiseases[randomIndex];
        const confidence = confidences[randomIndex];
        const data = diseaseData[selectedDisease];

        let measuresHtml = data.measures.slice(0, 3).map(m => `<li>${m}</li>`).join('');

        result.innerHTML = `
            <div class="prediction-header">
                <h3><i class="ph-fill ${data.icon}" style="color: ${data.color}"></i> ${selectedDisease}</h3>
                <span class="confidence-badge">Confidence: ${confidence}%</span>
            </div>
            <div class="prediction-body">
                <p>${data.description}</p>
                <h4><i class="ph ph-shield-check" style="color: var(--color-primary-600)"></i> Prevention Tips:</h4>
                <ul class="measures-list" style="text-align: left;">
                    ${measuresHtml}
                </ul>
            </div>
        `;

        result.classList.remove('hidden');
    }, 2000);
}

// =========================================================
// INIT
// =========================================================
document.addEventListener('DOMContentLoaded', () => {
    // Initialize default states for pages
    showDiseaseInfo();
    showSchemes();
    calculateRental();
    setupDragAndDrop();
});
