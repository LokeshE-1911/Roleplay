# app/stage_scorer.py
sales_stages = {
    "greeting": ["hi", "hello"],
    "discovery": ["need", "looking for", "want"],
    "presentation": ["feature", "benefit", "includes"],
    "objection": ["but", "too expensive", "not sure"],
    "closing": ["buy", "order", "deal"]
}

stage_scores = {
    "greeting": 10,
    "discovery": 20,
    "presentation": 20,
    "objection": 25,
    "closing": 25
}

def detect_stage_and_score(text: str, role: str):
    text = text.lower()
    for stage, keywords in sales_stages.items():
        if any(k in text for k in keywords):
            return stage, stage_scores[stage]
    return "unknown", 0