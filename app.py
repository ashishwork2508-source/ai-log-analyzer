import streamlit as st

st.title("🔐 AI Log Analyzer (Cyber Security Demo)")

log = st.text_area("📄 Paste your logs here")

def analyze(log):
    alerts = []
    score = 0

    if "failed" in log.lower():
        alerts.append("⚠️ Multiple failed login attempts (Brute Force)")
        score += 40

    if "192.168" in log:
        alerts.append("⚠️ Suspicious IP activity detected")
        score += 30

    if "error" in log.lower():
        alerts.append("⚠️ System errors detected")
        score += 20

    if score == 0:
        alerts.append("✅ No major threats detected")

    return alerts, score

if st.button("Analyze Logs"):
    alerts, score = analyze(log)

    st.subheader("🚨 Analysis Report")

    for a in alerts:
        st.write(a)

    st.write(f"🔥 Risk Score: {score}/100")
