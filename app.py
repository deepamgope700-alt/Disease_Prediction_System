import gradio as gr
from model import suggest_diseases

examples = [
    "I have fever, headache and nausea",
    "Experiencing chest pain and dizziness",
    "Itching and skin rash",
    "Fatigue, weight loss and excessive hunger",
    "Stomach pain and acidity"
]

def predict_disease(user_input):
    diseases = suggest_diseases(user_input)
    if len(diseases) == 1 and diseases[0].startswith("No"):
        return diseases[0]
    
    response = "Possible conditions (with match probability):\n\n"
    response += "\n".join(f"• {disease}" for disease in diseases)
    response += "\n\nNote: This is not a medical diagnosis. Please consult a healthcare professional."
    return response

interface = gr.Interface(
    fn=predict_disease,
    inputs=gr.Textbox(
        lines=3,
        placeholder="Enter your symptoms in plain English (e.g., 'I have fever and headache')",
        label="Describe your symptoms"
    ),
    outputs=gr.Textbox(label="Possible Conditions"),
    title="Symptom Checker - Disease Prediction",
    description="Describe your symptoms to get possible matching conditions. This is not a substitute for professional medical advice.",
    examples=examples,
    theme="default"
)

interface.launch()