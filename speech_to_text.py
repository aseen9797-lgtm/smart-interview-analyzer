import whisper
import sounddevice as sd
from scipy.io.wavfile import write

# Load Whisper model once
model = whisper.load_model("base")


def listen():
    duration = 10          # seconds
    sample_rate = 16000

    print("\n🎤 Speak now...")

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    filename = "recording.wav"
    write(filename, sample_rate, recording)

    print("📝 Converting speech to text...")

    result = model.transcribe(filename)

    text = result["text"].strip()

    print(f"\nYou said: {text}")

    return text