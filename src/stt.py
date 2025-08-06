from google.cloud import speech
from nlp_classifier import train_emergency_classifier, predict_emergency
from ner import train_ner_model, extract_location
from clustering import detect_clusters

def transcribe_audio(audio_file_path):
    client = speech.SpeechClient()
    with open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000,
        language_code="id-ID",
    )
    response = client.recognize(config=config, audio=audio)
    transcription = ""
    for result in response.results:
        transcription += result.alternatives[0].transcript
    return transcription

if __name__ == "__main__":
    audio_path = "data/sample_call_1.wav"  # Ubah sesuai audio yang diuji
    text = transcribe_audio(audio_path)
    print("Transkripsi:", text)

    classifier, vectorizer = train_emergency_classifier("data/emergency_data.txt")
    emergency_type = predict_emergency(classifier, vectorizer, text)
    print("Jenis darurat:", emergency_type)

    nlp_ner = train_ner_model("data/ner_data.txt")
    location = extract_location(nlp_ner, text)
    print("Lokasi:", location)

    lat, lon = 0.0, 0.0
    if location:
        if "flyover Cawang" in location:
            lat, lon = 6.25, 106.85
        elif "Jalan Sudirman" in location:
            lat, lon = 6.20, 106.82
        elif "daerah Senen" in location:
            lat, lon = 6.18, 106.84
        elif "Jalan Margonda" in location or "kampus UI" in location:
            lat, lon = 6.36, 106.83
    if lat == 0.0 and lon == 0.0:
        print("Peringatan: Koordinat tidak ditemukan untuk:", location)
        lat, lon = 6.36, 106.83  # Default jika gagal

    with open("data/cluster_data.txt", "a") as f:
        f.write(f"\n{text},{lat},{lon}")
    clusters = detect_clusters("data/cluster_data.txt")
    print("Klaster insiden:")
    for cluster_id, texts in clusters.items():
        print(f"Klaster {cluster_id}: {len(texts)} laporan")
        for text in texts:
            print(f"  - {text}")