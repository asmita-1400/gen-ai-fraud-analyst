def check_compliance(transaction):
    issues = []

    if transaction["amount"] > 100000:
        issues.append("High-value transaction exceeds safe threshold")

    if transaction["frequency"] > 5:
        issues.append("Too many transactions in short time")

    return issues