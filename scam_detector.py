SCAM_KEYWORDS = {

    "otp": 3,
    "urgent": 2,
    "account blocked": 3,
    "bank": 1,
    "verify": 1,
    "kyc": 2,
    "immediately": 2,
    "click link": 3,

    "turant": 2,
    "abhi": 1,
    "khata band": 3,
    "account band": 3,
    "bank se bol raha": 2,
    "otp batao": 3,
    "link pe click": 3,
    "adhar": 2,
    "pan": 2,
    "verify karo": 2
}

def analyze_text(text: str):
    text = text.lower()
    score = 0
    hits = []

    for word, weight in SCAM_KEYWORDS.items():
        if word in text:
            score += weight
            hits.append(word)

    if score >= 6:
        level = "HIGH"
    elif score >= 3:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "risk_level": level,
        "score": score,
        "flags": hits
    }