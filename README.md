# Disease Prediction from Symptoms using NLP

<p align="center">
  An AI-powered symptom checker that uses Natural Language Processing to analyze user-described symptoms and suggest possible diseases.
</p>


<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue" />
  <img src="https://img.shields.io/badge/Technology-NLP-purple" />
  <img src="https://img.shields.io/badge/NLP-spaCy-09A3D5" />
  <img src="https://img.shields.io/badge/UI-Gradio-orange" />
  <img src="https://img.shields.io/badge/Status-Development-yellow" />
</p>

## Project Overview

Searching for symptoms online often leads to information overload, conflicting results, and unnecessary anxiety.

**Disease Prediction from Symptoms using NLP** aims to simplify preliminary symptom analysis through an interactive NLP-based application.

Users can describe their symptoms in natural language, and the system processes the input, identifies relevant symptoms, and returns a ranked list of possible diseases based on symptom matching.

The application is developed using Python, spaCy, and Gradio.

## Key Features

- **Natural Language Input:** Describe symptoms using everyday language.
- **Symptom Extraction:** Identify relevant symptoms from free-text descriptions using NLP.
- **Disease Matching:** Compare extracted symptoms with disease-symptom mappings.
- **Ranked Predictions:** Display the top five matching disease suggestions.
- **Interactive Interface:** Simple and user-friendly Gradio interface.
- **Example Inputs:** Try predefined symptom descriptions to explore the application.

## Application Preview

<img width="1870" height="967" alt="image" src="https://github.com/user-attachments/assets/212f6723-98ca-45fb-bc2c-cb4d23b23848" />


## How It Works

The application follows a five-stage workflow:

1. **Input Symptoms:** The user enters a natural-language description of their symptoms.
2. **Symptom Processing:** spaCy processes the text and extracts recognized symptoms.
3. **Disease Matching:** Extracted symptoms are compared against the symptom-disease dataset.
4. **Prediction Generation:** Diseases are scored and ranked according to symptom overlap.
5. **Results Display:** The application returns the top matching conditions.

## Algorithm: Disease Suggestion Logic

The system uses a symptom-matching and ranking approach.

**Step 1 – Symptom Extraction**

Process the user's input and identify relevant symptoms using NLP techniques.

**Step 2 – Match Scoring**

Compare the extracted symptoms with the symptoms associated with each disease.

**Step 3 – Calculate Match Percentage**

Calculate a symptom-match score based on the overlap between identified symptoms and the known symptoms associated with a disease.

**Step 4 – Threshold Filtering**

Apply a configurable threshold to filter out low-scoring disease matches.

**Step 5 – Ranking**

Sort the remaining disease candidates in descending order and return the top five matches.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| spaCy | Natural Language Processing and symptom extraction |
| Pandas | Dataset processing |
| Gradio | Interactive user interface |
| NumPy | Numerical operations |

## 📊 Dataset

The project uses a structured symptom-disease dataset containing mappings between diseases and their associated symptoms.

The dataset is used to:
- Identify relationships between symptoms and diseases.
- Compare user-reported symptoms against known symptom patterns.
- Generate ranked disease suggestions.

**Dataset source:** Kaggle

## 📈 Model Evaluation

The project presentation reports the following evaluation results:

| Metric | Reported result |
|---|---:|
| Accuracy | 78% |
| Precision | 0.84 |
| Threshold used for reported accuracy | 0.3 |
| Threshold range explored | 0.1–0.5 |

Top-3 accuracy was also evaluated, although its numerical result was not specified in the presentation.

*Note: These are the results reported in the project evaluation. The dataset split, evaluation procedure, and metric definitions should be documented separately before treating these values as independently reproducible benchmarks.*

## 💻 Installation and Usage

### 1. Clone the repository

```bash
git clone https://github.com/daspiyushh/nlp-disease-predictor.git
cd nlp-disease-predictor
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Install the spaCy English language model if required:

```bash
python -m spacy download en_core_web_sm
```

### 4. Run the application

```bash
python app.py
```

Open the local Gradio URL displayed in your terminal.

## Project Structure

```text
nlp-disease-predictor/
│
├── app.py             # Gradio application
├── model.py           # Disease suggestion logic
├── nlp_utils.py       # NLP and symptom extraction
├── dataset.csv        # Symptom-disease dataset
├── evaluate.py        # Model evaluation
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
```

## Limitations and Disclaimer

- Predictions depend on the quality and coverage of the underlying dataset.
- Vague or unrecognized symptom descriptions may affect symptom extraction.
- Multiple diseases can share similar symptoms.
- Match scores should not be interpreted as medically validated probabilities.

**Disclaimer:** This project is intended for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional regarding medical concerns.

## Future Improvements

- Improve symptom recognition using advanced NLP techniques.
- Incorporate synonym handling and negation detection.
- Explore machine learning and deep learning classification models.
- Expand and validate the symptom-disease dataset.
- Improve evaluation through robust validation and additional metrics.
- Deploy the application for public access.

##  Contributors

This project was developed collaboratively by:

- **Dipam Gope**
- **Saksham Raj**
- **Piyush Das**

## Support

If you find this project interesting, consider giving the repository a star ⭐.

Contributions and suggestions are welcome!
