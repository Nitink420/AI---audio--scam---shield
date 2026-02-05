SCAM_KEYWORDS = {
    "english": {
        "otp": 3,
        "urgent": 2,
        "bank": 2,
        "account blocked": 3,
        "verify": 1,
        "upi": 3,
        "password": 3,
        "refund": 2,
        "suspended": 2
    },

    "hindi": {
        "otp": 3,
        "turant": 2,
        "bank": 2,
        "account band": 3,
        "verify": 1,
        "upi": 3,
        "password": 3,
        "paise wapas": 2,
        "khata band": 2
    },

    "tamil": {
        "otp": 3,
        "udane": 2,
        "bank": 2,
        "account mudakkappattullathu": 3,
        "verify": 1,
        "upi": 3,
        "password": 3,
        "refund": 2
    },

    "telugu": {
        "otp": 3,
        "twaraga": 2,
        "bank": 2,
        "account block": 3,
        "verify": 1,
        "upi": 3,
        "password": 3,
        "refund": 2
    },

    "malayalam": {
        "otp": 3,
        "udane": 2,
        "bank": 2,
        "account block": 3,
        "verify": 1,
        "upi": 3,
        "password": 3,
        "refund": 2
    }
}


def analyze_text(text: str):
    text = text.lower()
    score = 0
    flags = []
    detected_languages = set()

    for language, keywords in SCAM_KEYWORDS.items():
        for word, weight in keywords.items():
            if word in text:
                score += weight
                flags.append(word)
                detected_languages.add(language)

    if score >= 6:
        risk = "HIGH"
    elif score >= 3:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "risk_level": risk,
        "score": score,
        "flags": list(set(flags)),
        "languages_detected": list(detected_languages)
    }
