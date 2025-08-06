from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np

def train_emergency_classifier(data_file):
    # Baca data dari file
    with open(data_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    texts = [line.split(',')[0].strip() for line in lines]
    labels = [line.split(',')[1].strip() for line in lines]

    # Ubah teks menjadi angka menggunakan TF-IDF
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    y = np.array(labels)

    # Latih model dengan Naive Bayes
    classifier = MultinomialNB()
    classifier.fit(X, y)
    return classifier, vectorizer

def predict_emergency(classifier, vectorizer, text):
    # Ubah teks input jadi angka dan prediksi
    X_new = vectorizer.transform([text])
    prediction = classifier.predict(X_new)
    return prediction[0]

if __name__ == "__main__":
    # Latih model dengan data
    classifier, vectorizer = train_emergency_classifier("data/emergency_data.txt")

    # Contoh teks dari Speech-to-Text
    stt_text = "ada kecelakaan di flyover Cawang"
    emergency_type = predict_emergency(classifier, vectorizer, stt_text)
    print("Jenis darurat:", emergency_type)