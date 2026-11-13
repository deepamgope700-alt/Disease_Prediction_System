import pandas as pd
import re
from collections import Counter
from nlp_utils import extract_symptoms  # Using the improved NLP processing

# Load dataset
df = pd.read_csv("dataset.csv")

# Combine all symptom columns into one list per row
symptom_columns = [col for col in df.columns if col.startswith("Symptom_")]

def clean_symptom(s):
    if pd.isna(s):
        return ""
    return str(s).strip().lower().replace(" ", "_")

# Create a new column with a list of cleaned symptoms per row
df["all_symptoms"] = df[symptom_columns].apply(
    lambda row: [clean_symptom(s) for s in row if clean_symptom(s)],
    axis=1
)

# Create a dictionary of disease to symptoms
disease_symptoms = df.groupby("Disease")["all_symptoms"].apply(list).to_dict()

# Create a symptom to diseases mapping
symptom_diseases = {}
for disease, symptoms_list in disease_symptoms.items():
    for symptoms in symptoms_list:
        for symptom in symptoms:
            if symptom not in symptom_diseases:
                symptom_diseases[symptom] = []
            symptom_diseases[symptom].append(disease)

def suggest_diseases(user_input, threshold=0.3):
    # Extract symptoms using NLP
    input_symptoms = extract_symptoms(user_input)
    
    if not input_symptoms:
        return ["No symptoms detected in your input. Please describe your symptoms in more detail."]
    
    # Find diseases that match any of the input symptoms
    disease_scores = Counter()
    
    for symptom in input_symptoms:
        if symptom in symptom_diseases:
            for disease in symptom_diseases[symptom]:
                disease_scores[disease] += 1
    
    if not disease_scores:
        return ["No matching diseases found. Please try describing your symptoms differently."]
    
    # Normalize scores by maximum possible matches
    max_possible_matches = {}
    for disease in disease_scores:
        # Get the maximum number of symptoms any instance of this disease has
        max_symptoms = max(len(symptoms) for symptoms in disease_symptoms[disease])
        max_possible_matches[disease] = max_symptoms
    
    # Calculate match percentage for each disease
    scored_diseases = []
    for disease, count in disease_scores.most_common():
        match_percentage = count / max_possible_matches[disease]
        if match_percentage >= threshold:
            scored_diseases.append((disease, match_percentage))
    
    if not scored_diseases:
        return ["No strong matches found. Please consult a healthcare professional."]
    
    # Sort by match percentage (descending)
    scored_diseases.sort(key=lambda x: x[1], reverse=True)
    
    # Format results
    results = []
    for disease, percentage in scored_diseases[:5]:  # Return top 5 matches
        results.append(f"{disease} ({percentage:.0%} match)")
    
    return results