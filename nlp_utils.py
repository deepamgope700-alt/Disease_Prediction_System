import spacy
from spacy.matcher import PhraseMatcher
import pandas as pd

# Load English model
nlp = spacy.load("en_core_web_sm")

# Load symptom phrases from dataset
df = pd.read_csv("dataset.csv")
symptom_columns = [col for col in df.columns if col.startswith("Symptom_")]

# Get all unique symptoms
all_symptoms = set()
for col in symptom_columns:
    symptoms = df[col].dropna().unique()
    all_symptoms.update(str(s).strip().lower().replace(" ", "_") for s in symptoms)

# Create phrase matcher for symptoms
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp.make_doc(symptom.replace("_", " ")) for symptom in all_symptoms]
matcher.add("SYMPTOMS", patterns)

def extract_symptoms(text):
    doc = nlp(text.lower())
    matches = matcher(doc)
    
    # Get matched symptoms
    matched_symptoms = set()
    for match_id, start, end in matches:
        span = doc[start:end]
        matched_symptoms.add(span.text.replace(" ", "_"))
    
    # Also look for symptom-like nouns and adjectives
    for token in doc:
        if token.pos_ in ['NOUN', 'ADJ'] and len(token.text) > 3:
            normalized = token.lemma_.replace(" ", "_")
            if normalized in all_symptoms and normalized not in matched_symptoms:
                matched_symptoms.add(normalized)
    
    return list(matched_symptoms)