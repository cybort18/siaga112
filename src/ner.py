import spacy
from spacy.training.example import Example

def train_ner_model(data_file, model_path="ner_model"):
    # Muat model dasar spaCy (tanpa NER terlatih)
    nlp = spacy.blank("id")  # Bahasa Indonesia
    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner")
    else:
        ner = nlp.get_pipe("ner")

    # Tambah label lokasi
    ner.add_label("LOC")

    # Baca data pelatihan
    with open(data_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    training_data = []
    for line in lines:
        text, entities = line.strip().split('|')
        start = text.index(entities)
        end = start + len(entities)
        training_data.append((text, {"entities": [(start, end, "LOC")]}))

    # Latih model
    optimizer = nlp.begin_training()
    for _ in range(10):  # Latih 10 iterasi
        for text, annotations in training_data:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            nlp.update([example], drop=0.5, sgd=optimizer)

    # Simpan model
    nlp.to_disk(model_path)
    return nlp

def extract_location(nlp, text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "LOC":
            return ent.text
    return None

if __name__ == "__main__":
    # Latih model
    nlp = train_ner_model("data/ner_data.txt")

    # Contoh teks dari Speech-to-Text
    stt_text = "ada kecelakaan di flyover Cawang"
    location = extract_location(nlp, stt_text)
    print("Lokasi:", location)