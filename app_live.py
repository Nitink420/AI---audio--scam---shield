import streamlit as st
from scam_detector import analyze_text

st.set_page_config(
    page_title="AI Scam Call Shield",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ AI Scam Call Shield")
st.caption("Real-time scam detection from call transcripts")

text = st.text_area(
    "📞 Paste call transcript here:",
    height=200,
    placeholder="Hello sir, your bank account is blocked. Share OTP urgently..."
)

if st.button("Analyze Call"):
    if not text.strip():
        st.warning("Please enter call text")
    else:
        result = analyze_text(text)

        if result["risk_level"] == "HIGH":
            st.error("⚠️ HIGH RISK SCAM DETECTED")
        elif result["risk_level"] == "MEDIUM":
            st.warning("⚠️ Possible Scam Detected")
        else:
            st.success("✅ Call appears safe")

        st.subheader("🔍 Detailed Analysis")
        st.json(result)
