import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from model import suggest_diseases
from collections import defaultdict
import random

# Load dataset
df = pd.read_csv("dataset.csv")

# Preprocess the data to create test cases
def prepare_test_cases(df, num_samples_per_disease=5):
    test_cases = []
    
    # Group by disease
    grouped = df.groupby('Disease')
    
    for disease, group in grouped:
        # Get all symptom combinations for this disease
        symptom_combinations = []
        for _, row in group.iterrows():
            symptoms = [str(s).strip().lower().replace(" ", "_") 
                       for s in row[1:] if pd.notna(s) and str(s).strip()]
            symptom_combinations.append(symptoms)
        
        # Create test cases by sampling symptom combinations
        samples = random.sample(symptom_combinations, min(num_samples_per_disease, len(symptom_combinations)))
        
        for symptoms in samples:
            # Create natural language description
            description = "I have " + ", ".join(s.replace("_", " ") for s in symptoms)
            test_cases.append({
                'input': description,
                'expected': disease,
                'symptoms': symptoms
            })
    
    return test_cases

# Evaluation function
def evaluate_model(test_cases, threshold=0.3):
    results = {
        'exact_match': 0,
        'top3_match': 0,
        'symptom_coverage': [],
        'precision': [],
        'recall': [],
        'f1': []
    }
    
    for case in test_cases:
        # Get model predictions
        predictions = suggest_diseases(case['input'], threshold)
        
        # Extract just disease names from predictions (remove percentages)
        predicted_diseases = [pred.split(' (')[0] for pred in predictions]
        
        # Check exact match
        if case['expected'] in predicted_diseases:
            results['exact_match'] += 1
        
        # Check if in top 3 predictions
        if case['expected'] in predicted_diseases[:3]:
            results['top3_match'] += 1
        
        # Calculate precision/recall for symptoms
        if predicted_diseases:  # Only calculate if we got predictions
            # Get all possible symptoms for predicted diseases
            predicted_symptoms = set()
            for disease in predicted_diseases:
                disease_data = df[df['Disease'] == disease]
                for _, row in disease_data.iterrows():
                    symptoms = [str(s).strip().lower().replace(" ", "_") 
                              for s in row[1:] if pd.notna(s) and str(s).strip()]
                    predicted_symptoms.update(symptoms)
            
            # Calculate metrics
            actual_symptoms = set(case['symptoms'])
            true_positives = len(actual_symptoms & predicted_symptoms)
            false_positives = len(predicted_symptoms - actual_symptoms)
            false_negatives = len(actual_symptoms - predicted_symptoms)
            
            precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
            recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
            f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
            
            results['precision'].append(precision)
            results['recall'].append(recall)
            results['f1'].append(f1)
    
    # Calculate final metrics
    total_cases = len(test_cases)
    results['exact_match_accuracy'] = results['exact_match'] / total_cases
    results['top3_accuracy'] = results['top3_match'] / total_cases
    results['avg_precision'] = np.mean(results['precision']) if results['precision'] else 0
    results['avg_recall'] = np.mean(results['recall']) if results['recall'] else 0
    results['avg_f1'] = np.mean(results['f1']) if results['f1'] else 0
    
    return results

# Main evaluation
def main():
    # Prepare test cases
    test_cases = prepare_test_cases(df, num_samples_per_disease=5)
    print(f"Prepared {len(test_cases)} test cases")
    
    # Evaluate with different thresholds
    thresholds = [0.1, 0.2, 0.3, 0.4, 0.5]
    
    for threshold in thresholds:
        print(f"\nEvaluating with threshold = {threshold}")
        metrics = evaluate_model(test_cases, threshold)
        
        print("\nEvaluation Results:")
        print(f"Exact Match Accuracy: {metrics['exact_match_accuracy']:.2%}")
        print(f"Top 3 Accuracy: {metrics['top3_accuracy']:.2%}")
        print(f"Average Precision: {metrics['avg_precision']:.2%}")
        print(f"Average Recall: {metrics['avg_recall']:.2%}")
        print(f"Average F1 Score: {metrics['avg_f1']:.2%}")

if __name__ == "__main__":
    main()