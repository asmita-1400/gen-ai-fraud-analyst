def log_decision(transaction, score, explanation):
    return {
        "transaction": transaction,
        "risk_score": score,
        "explanation": explanation
    }