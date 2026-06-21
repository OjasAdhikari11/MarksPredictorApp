# Marks Predictor App

A simple machine learning web app that predicts a student's **exam marks percentage** based on their **daily study hours**. Built with **Linear Regression** and served through a **Flask** web interface.

## Overview

Given the number of hours a student studies per day, the app predicts the percentage marks they are likely to score. The model is trained on a dataset of study hours vs. student marks and deployed as an interactive Flask application.

## Features

- Predict marks from daily study hours
- Flask web UI with instant predictions
- Input validation (study hours must be between 0–24)
- Prediction logging to CSV (`smp_data_from_app.csv`)
- Exploratory data analysis and model training in Jupyter

## Tech Stack

| Layer | Technology |
|-------|------------|
| Web framework | Flask |
| ML | scikit-learn (Linear Regression) |
| Data | pandas, NumPy |
| Visualization | matplotlib, seaborn |
| Model serialization | joblib |
| Frontend | HTML, CSS |

## Project Structure

```
MarksPredictorApp/
├── app.py                              # Flask web application
├── templates/
│   └── index.html                      # Prediction form UI
├── student_info.csv                    # Training dataset (~200 records)
├── students_mark_predictor.ipynb       # EDA & model training
├── smp_data_from_app.csv               # Logged predictions from app usage
└── README.md
```

## Dataset

`student_info.csv`:

| Column | Description |
|--------|-------------|
| study_hours | Hours studied per day |
| student_marks | Marks scored (percentage) |

## Model

- **Algorithm:** Linear Regression
- **Input:** Daily study hours (single feature)
- **Output:** Predicted marks percentage
- **Serialized as:** `Students_mark_predictor_model.pkl`

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/OjasAdhikari11/MarksPredictorApp.git
cd MarksPredictorApp

pip install flask scikit-learn pandas numpy matplotlib seaborn joblib jupyter
```

### Train the Model

Run `students_mark_predictor.ipynb` to explore the data, train the Linear Regression model, and generate `Students_mark_predictor_model.pkl`. Place the pickle file in the project root.

### Run the App

```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000), enter study hours, and click **Predict Marks**.

## How It Works

1. User enters daily study hours on the web form.
2. Flask validates the input (0–24 hours).
3. The Linear Regression model predicts the marks percentage.
4. Result is displayed: *"You will get [X%] marks, if you study for [Y] hours per day"*
5. Each prediction is logged to `smp_data_from_app.csv`.

## Example

| Study Hours | Predicted Marks |
|-------------|-----------------|
| 5 | ~72% |
| 8 | ~85% |
| 2 | ~45% |

*(Actual values depend on the trained model)*

## Limitations

- Single-feature model (only study hours considered)
- Small training dataset (~200 samples)
- Serialized model file not included — run the notebook first
- Not a substitute for actual academic planning

