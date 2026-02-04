import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

print("🔍 Checking audio devices...")
devices = sd.query_devices()
print(devices)

input_devices = [
    i for i, d in enumerate(devices)
    if d["max_input_channels"] > 0
]

if not input_devices:
    print("❌ No input microphone found")
    exit()

DEVICE = input_devices[0]
print(f"🎤 Using input device ID: {DEVICE}")

SAMPLE_RATE = 16000
DURATION = 5

print("🎙️ Recording started (5 seconds)...")
audio = sd.rec(
    int(DURATION * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    device=DEVICE,
    dtype=np.int16
)
sd.wait()

wav.write("test_audio.wav", SAMPLE_RATE, audio)

print("✅ Recording finished")
print("📁 File saved as test_audio.wav")
input("Press Enter to exit")