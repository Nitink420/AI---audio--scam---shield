# 🛡️ AI Scam Call Shield

AI Scam Call Shield is an AI-powered system designed to detect fraudulent phone calls in real time by analyzing the conversation content and identifying common scam patterns.

---

## 🚨 Problem Statement

Phone call scams are increasing rapidly, especially targeting users through:
- Fake bank calls
- OTP and UPI frauds
- Urgent account suspension threats

These calls often use **psychological pressure**, **multilingual communication**, and **mixed languages**, making them difficult to detect manually.

---

## 💡 Our Solution

AI Scam Call Shield analyzes call conversations and instantly flags:
- Scam-related keywords
- High-risk behavioral patterns
- Multilingual scam indicators (English, Hindi, Tamil, Telugu, Malayalam)

The system provides:
- **Risk Level (LOW / MEDIUM / HIGH)**
- **Detected scam indicators**
- **Languages involved in the call**

---

## 🎙️ Why Audio Is Not Used in This Demo

Originally, the system was designed to work with **live call audio**.  
However, for this cloud-deployed demo, the audio layer has been intentionally removed due to **browser and platform-level limitations**, not due to a limitation in the AI model itself.

### Technical Constraints:
- Modern browsers restrict continuous microphone streaming for security and privacy reasons.
- Cloud platforms (like Streamlit Cloud / Render) do not allow direct device-level microphone access.
- Real-time audio streaming requires telecom or OS-level integration, which is outside the scope of a web demo.

### Engineering Decision:
To ensure:
- ✅ Stable cloud deployment  
- ✅ Smooth demo experience  
- ✅ Focus on core AI logic  

We replaced live audio input with **call transcript input**, which represents the exact same data the AI would receive after speech-to-text processing.

> **Important:**  
> The AI logic is completely audio-agnostic.  
> The audio-to-text (ASR) layer is modular and can be plugged in when integrated with telecom systems, mobile apps, or call center infrastructure.

---

## 🌍 Multilingual Support

The system supports scam detection in:
- English
- Hindi
- Tamil
- Telugu
- Malayalam

It also handles **mixed-language conversations**, which are very common in real-world scam calls.

---

## 🧠 How It Works

1. User pastes a live or recorded call transcript
2. The AI scans the text for scam indicators
3. A weighted risk score is calculated
4. The system instantly shows a fraud alert if detected

---

## 🛠️ Tech Stack

- Python
- Streamlit (UI)
- Rule-based + pattern-based AI logic
- Cloud-deployable architecture

---

## 🚀 Future Scope

- Live audio integration with telecom APIs
- Mobile app integration
- Real-time call interception
- Automatic reporting to cybercrime authorities

---

## ⚠️ Disclaimer

This project is a prototype developed for the **India AI Impact Buildathon** to demonstrate the feasibility of real-time scam detection using AI.
