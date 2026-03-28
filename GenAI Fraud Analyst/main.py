from fastapi import FastAPI
from agents.fraud_agent import detect_fraud
from agents.compliance_agent import check_compliance
from agents.explanation_agent import generate_explanation
from agents.audit_agent import log_decision

app = FastAPI()

@app.post("/analyze")
def analyze(transaction: dict):
    score = detect_fraud(transaction)
    issues = check_compliance(transaction)
    explanation = generate_explanation(score, issues)
    audit = log_decision(transaction, score, explanation)

    return {
        "risk_score": score,
        "decision": "Fraud" if score > 0.7 else "Safe",
        "explanation": explanation,
        "audit_log": audit
    }