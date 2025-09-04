
# mental_wellness/constants.py

DEGREE_CHOICES = [
    ("MBBS", "MBBS"),
    ("MD", "MD"),
    ("DO", "DO"),
    ("DNB", "DNB"),
    ("MS", "MS"),
    ("BDS", "BDS"),
    ("MDS", "MDS"),
    ("PhD", "PhD"),
    ("MPH", "MPH"),
    ("DM", "DM"),
    ("MCh", "MCh"),
    ("BAMS", "BAMS"),
    ("BHMS", "BHMS"),
    ("BPT", "BPT"),
    ("MPT", "MPT"),
    ("BVSc", "BVSc"),
    ("MSc", "MSc"),
    ("DGO", "DGO"),
    ("FRCS", "FRCS"),
    ("MRCP", "MRCP"),
    ("DCH", "DCH"),
    ("DPH", "DPH"),
    ("DDS", "DDS"),
]

DEGREE_SPECIALIZATION_MAPPING = {
    "MBBS": {
        "field": "General Medicine",
        "keywords": ["primary care", "general practitioner", "family physician", "internal medicine"]
    },
    "MD": {
        "field": "Specialized Medicine",
        "keywords": ["physician", "internal medicine", "pediatrics", "cardiology", "neurology", "psychiatry"]
    },
    "DO": {
        "field": "Osteopathic Medicine",
        "keywords": ["holistic", "musculoskeletal", "osteopathy", "manual therapy"]
    },
    "DNB": {
        "field": "Broad Specializations",
        "keywords": ["medical specialties", "diplomate", "national board", "specialist"]
    },
    "MS": {
        "field": "Surgery",
        "keywords": ["general surgery", "orthopedics", "ENT", "laparoscopic", "surgeon"]
    },
    "BDS": {
        "field": "Dental Surgery",
        "keywords": ["dentist", "oral health", "teeth", "dental care", "prosthodontics"]
    },
    "MDS": {
        "field": "Advanced Dental Specialties",
        "keywords": ["orthodontics", "periodontics", "oral surgery", "endodontics", "dental implants"]
    },
    "PhD": {
        "field": "Medical Research / Academics",
        "keywords": ["research", "medical science", "academic", "laboratory", "teaching"]
    },
    "MPH": {
        "field": "Public Health",
        "keywords": ["epidemiology", "health policy", "global health", "community health", "preventive medicine"]
    },
    "DM": {
        "field": "Super Speciality Medicine",
        "keywords": ["cardiology", "neurology", "nephrology", "endocrinology", "gastroenterology"]
    },
    "MCh": {
        "field": "Super Speciality Surgery",
        "keywords": ["cardiothoracic surgery", "neurosurgery", "plastic surgery", "urology"]
    },
    "BAMS": {
        "field": "Ayurvedic Medicine",
        "keywords": ["ayurveda", "herbal medicine", "traditional medicine", "natural healing"]
    },
    "BHMS": {
        "field": "Homeopathic Medicine",
        "keywords": ["homeopathy", "natural treatment", "alternative medicine"]
    },
    "BPT": {
        "field": "Physiotherapy",
        "keywords": ["physical therapy", "rehabilitation", "exercise", "movement", "muscle recovery"]
    },
    "MPT": {
        "field": "Advanced Physiotherapy",
        "keywords": ["neuro physiotherapy", "cardiopulmonary rehab", "sports physiotherapy"]
    },
    "BVSc": {
        "field": "Veterinary Science",
        "keywords": ["animal health", "veterinarian", "pet care", "animal surgery"]
    },
    "MSc": {
        "field": "Medical Sciences / Research",
        "keywords": ["clinical research", "biotechnology", "microbiology", "medical lab"]
    },
    "DGO": {
        "field": "Gynecology & Obstetrics",
        "keywords": ["women's health", "pregnancy", "gynecology", "childbirth"]
    },
    "FRCS": {
        "field": "Surgery (UK/International)",
        "keywords": ["fellowship", "surgeon", "surgical practice", "international qualification"]
    },
    "MRCP": {
        "field": "Internal Medicine (UK/International)",
        "keywords": ["physician", "medical practice", "UK", "fellowship", "diagnostics"]
    },
    "DCH": {
        "field": "Pediatrics",
        "keywords": ["child care", "children’s health", "pediatrics", "infants"]
    },
    "DPH": {
        "field": "Public Health / Preventive Medicine",
        "keywords": ["community health", "vaccination", "health programs", "disease prevention"]
    },
    "DDS": {
        "field": "Dental Surgery (US Equivalent)",
        "keywords": ["dentistry", "oral surgeon", "tooth care", "US dental"]
    },
}


