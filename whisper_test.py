print("=== FILE STARTED ===")
input("Press Enter to continue")

import whisper

print("Whisper model load ho raha hai...")
model = whisper.load_model("base")

print("Audio transcribe ho raha hai...")
result = model.transcribe("test_audio.wav")

print("TRANSCRIPTION:")
print(result["text"])