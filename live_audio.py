import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import whisper

MODEL = whisper.load_model("base")

def record_and_transcribe(duration=3, fs=16000):
    print("🎙️ Listening...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    # 🔒 SILENCE CHECK
    if np.max(np.abs(audio)) < 0.01:
        print("❌ Silent audio detected")
        return ""

    wav.write("live.wav", fs, audio)

    result = MODEL.transcribe(
        "live.wav",
        language="en",
        fp16=False
    )

    return result["text"].strip()