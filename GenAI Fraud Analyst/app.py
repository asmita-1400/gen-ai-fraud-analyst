import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

# -------------------------------
# PAGE CONFIG
# -------------------------------

st.set_page_config(
    page_title="GenAI Fraud Detection Agent",
    layout="wide"
)

# -------------------------------
# HEADER
# -------------------------------

st.title("🛡️ GenAI Fraud Detection Agent")

st.success(
"Autonomous AI System | Detect • Explain • Decide • Audit"
)

st.write(
"""
This AI system analyzes financial transaction behavior in real-time  
to detect fraud patterns, explain risk factors, and recommend security actions.
"""
)

st.markdown("---")

# -------------------------------
# DASHBOARD AI AVATAR
# -------------------------------

colA, colB = st.columns([1,4])

with colA:
    st.image("assets/ai_avtaar.gif", width=220)

with colB:

    st.subheader("🤖 AI Fraud Assistant")

    st.write(
    """
Hello! I am your AI fraud analyst.

I monitor financial transactions, detect suspicious behavior,
explain risk factors, and recommend security actions to protect users.
"""
)

st.markdown("---")

# -------------------------------
# SIDEBAR
# -------------------------------

st.sidebar.image("assets/ai_avtaar.gif", width=120)

st.sidebar.title("AI Assistant")

st.sidebar.header("💳 Transaction Input")

amount = st.sidebar.number_input(
"Transaction Amount ($)",
min_value=1
)

location = st.sidebar.selectbox(
"Transaction Location",
["Home Country","Foreign Country"]
)

time_of_day = st.sidebar.selectbox(
"Transaction Time",
["Day","Night"]
)

device = st.sidebar.selectbox(
"Device Used",
["Known Device","New Device"]
)

transactions_today = st.sidebar.slider(
"Transactions Today",
1,20
)

# -------------------------------
# FRAUD ATTACK SIMULATION
# -------------------------------

if st.sidebar.button("⚡ Simulate Fraud Attack"):

    amount = 5000
    location = "Foreign Country"
    time_of_day = "Night"
    device = "New Device"
    transactions_today = 10

    st.sidebar.warning("🚨 Fraud Scenario Loaded")

# -------------------------------
# FRAUD RISK ENGINE
# -------------------------------

score = 0
reasons = []

if amount > 2000:
    score += 30
    reasons.append("High transaction amount")

if location == "Foreign Country":
    score += 25
    reasons.append("Transaction from foreign country")

if time_of_day == "Night":
    score += 15
    reasons.append("Unusual transaction time")

if device == "New Device":
    score += 20
    reasons.append("New device detected")

if transactions_today > 5:
    score += 10
    reasons.append("Too many transactions today")

risk_score = min(score,100)

# -------------------------------
# ANALYZE BUTTON
# -------------------------------

if st.button("🚀 Analyze Transaction"):

    with st.spinner("AI Agents analyzing transaction..."):
        time.sleep(2)

    st.markdown("---")

    col1, col2 = st.columns(2)

# -------------------------------
# RISK RESULT
# -------------------------------

    with col1:

        st.subheader("📊 Risk Analysis")

        st.metric("Risk Score", f"{risk_score}/100")

        st.progress(risk_score)

        if risk_score > 70:
            decision = "BLOCK"
            st.error("🚨 HIGH FRAUD RISK")

        elif risk_score > 40:
            decision = "REVIEW"
            st.warning("⚠️ MEDIUM FRAUD RISK")

        else:
            decision = "APPROVE"
            st.success("✅ LOW RISK")

# -------------------------------
# FRAUD PROBABILITY CHART
# -------------------------------

    with col2:

        st.subheader("📉 Fraud Probability")

        fig, ax = plt.subplots()

        ax.bar(["Fraud Probability"], [risk_score])

        ax.set_ylim(0,100)

        ax.set_ylabel("Probability %")

        st.pyplot(fig)

# -------------------------------
# TRANSACTION TABLE
# -------------------------------

    st.subheader("📄 Transaction Details")

    data = {

    "Amount":amount,
    "Location":location,
    "Time":time_of_day,
    "Device":device,
    "Transactions Today":transactions_today,
    "Risk Score":risk_score

    }

    df = pd.DataFrame([data])

    st.table(df)

# -------------------------------
# EXPLAINABLE AI
# -------------------------------

    st.subheader("🧠 AI Explanation")

    if reasons:

        for r in reasons:
            st.write("•", r)

    else:
        st.write("No suspicious patterns detected.")

# -------------------------------
# AI DECISION ENGINE
# -------------------------------

    st.subheader("🤖 AI Decision Engine")

    if decision == "BLOCK":

        st.error(
        "🚫 Transaction Blocked. Identity verification required."
        )

    elif decision == "REVIEW":

        st.warning(
        "📲 OTP verification recommended."
        )

    else:

        st.success(
        "💳 Transaction Approved."
        )

# -------------------------------
# FRAUD TREND GRAPH
# -------------------------------

    st.subheader("📈 Fraud Pattern Trend")

    history = np.random.randint(10,90,15)

    fig2, ax2 = plt.subplots()

    ax2.plot(history, marker="o")

    ax2.set_ylabel("Risk Score")

    ax2.set_title("Recent Transaction Risk Trend")

    st.pyplot(fig2)

# -------------------------------
# AUDIT LOG
# -------------------------------

    st.subheader("📁 Audit Log")

    audit_log = {

    "transaction_amount":amount,
    "risk_score":risk_score,
    "decision":decision,
    "timestamp":time.strftime("%Y-%m-%d %H:%M:%S")

    }

    st.json(audit_log)

    st.markdown("---")

    st.success(
    "💡 This AI system autonomously detects fraud, explains decisions, and recommends real-time financial security actions."
    )