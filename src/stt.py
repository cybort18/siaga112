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

from ner import train_ner_model, extract_location
nlp_ner = train_ner_model("data/ner_data.txt")
location = extract_location(nlp_ner, text)
print("Lokasi:", location)

from clustering import detect_clusters
# Simulasi koordinat berdasarkan lokasi yang dikenali
lat, lon = 0.0, 0.0  # Default jika lokasi tidak ditemukan
if location:  # Hanya lanjut jika location bukan None
    if "flyover Cawang" in location:
        lat, lon = 6.25, 106.85
    elif "Jalan Sudirman" in location:
        lat, lon = 6.20, 106.82
    elif "daerah Senen" in location:
        lat, lon = 6.18, 106.84

with open("data/cluster_data.txt", "a") as f:
    f.write(f"\n{text},{lat},{lon}")
clusters = detect_clusters("data/cluster_data.txt")
print("Klaster insiden:")
for cluster_id, texts in clusters.items():
    print(f"Klaster {cluster_id}: {len(texts)} laporan")
    for text in texts:
        print(f"  - {text}")

from nlp_classifier import predict_emergency, train_emergency_classifier
classifier, vectorizer = train_emergency_classifier("data/emergency_data.txt")
emergency_type = predict_emergency(classifier, vectorizer, text)
print("Jenis darurat:", emergency_type)