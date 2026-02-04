import streamlit as st
from live_audio import record_and_transcribe
from scam_detector import analyze_text
import time

st.set_page_config(page_title="Suspicias Shield", page_icon="🛡️")

st.title("🛡️ AI Audio Scam Shield")
st.caption("Hindi + Hinglish Scam Detection (Live)")

if "risk_score" not in st.session_state:
    st.session_state.risk_score = 0

st.markdown("### 🎙️ Live Call Monitor")

if st.button("🎧 Listen (3 sec)"):
    with st.spinner("Listening... Speak clearly"):
        text = record_and_transcribe()

    if text == "":
        st.info("Kuch clear sunai nahi diya")
    else:
        st.write("**📝 Heard:**")
        st.write(text)

        result = analyze_text(text)

        if result["risk_level"] == "HIGH":
            st.session_state.risk_score += 3
        elif result["risk_level"] == "MEDIUM":
            st.session_state.risk_score += 2
        else:
            st.session_state.risk_score += 1


st.markdown("### 📊 Risk Level Meter")
progress = min(st.session_state.risk_score / 10, 1.0)
st.progress(progress)

alert_box = st.empty()

if st.session_state.risk_score >= 6:
    for _ in range(3):
        alert_box.error("🚨 FRAUD CALL DETECTED! HANG UP NOW!")
        time.sleep(0.4)
        alert_box.warning("⚠️ High Risk Call")
        time.sleep(0.4)
else:
    alert_box.success("✅ Monitoring... Call seems safe")

st.markdown(f"**Risk Score:** {st.session_state.risk_score}")