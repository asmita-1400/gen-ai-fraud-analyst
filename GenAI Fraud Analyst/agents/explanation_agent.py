def generate_explanation(score, issues):
    if score > 0.7:
        level = "HIGH RISK"
    elif score > 0.4:
        level = "MEDIUM RISK"
    else:
        level = "LOW RISK"

    if issues:
        reason = ", ".join(issues)
    else:
        reason = "No major issues detected"

    return f"Transaction is {level} due to: {reason}"