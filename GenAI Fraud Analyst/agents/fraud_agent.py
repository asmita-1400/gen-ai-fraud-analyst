def detect_fraud(transaction):
    score = 0

    if transaction["amount"] > 100000:
        score += 0.4
    if transaction["frequency"] > 5:
        score += 0.3
    if transaction["location_change"] == 1:
        score += 0.3

    return min(score, 1.0)