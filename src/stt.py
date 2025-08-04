from google.cloud import speech
import os

def transcribe_audio(audio_file_path):
    # Buat koneksi ke Google Cloud
    client = speech.SpeechClient()

    # Baca file audio
    with open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()

    # Atur pengaturan untuk mengenali suara
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000,  # Frekuensi suara (standar untuk WAV)
        language_code="id-ID",     # Bahasa Indonesia
    )

    # Proses audio jadi teks
    response = client.recognize(config=config, audio=audio)
    transcription = ""
    for result in response.results:
        transcription += result.alternatives[0].transcript
    return transcription

if __name__ == "__main__":
    audio_path = "data/sample_call_mono.wav"  # Lokasi file audio Anda
    text = transcribe_audio(audio_path)
    print("Transkripsi:", text)