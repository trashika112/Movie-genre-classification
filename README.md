# Movie Genre Classification

A machine learning model that predicts movie genres based on plot summaries using Logistic Regression and TF-IDF features.

---

## Overview

This project addresses the task of movie genre classification from textual plot summaries. Leveraging classical NLP techniques and supervised learning, the model uses TF-IDF vectorization combined with a Logistic Regression classifier to categorize movies into multiple genres.

The solution includes:

- Data preprocessing and feature extraction with TF-IDF
- Model training and evaluation on a diverse IMDB-based dataset
- Serialization of the trained model and preprocessing tools
- A user-friendly interactive web interface deployed via Hugging Face Spaces for real-time genre prediction

---

## Dataset

The model is trained on the [Genre Classification Dataset (IMDB)](https://www.kaggle.com/datasets/hijest/genre-classification-dataset-imdb), a publicly available dataset containing movie plots and genre labels.


---

## Features

- **Text vectorization** using TF-IDF with a vocabulary size optimized for performance
- **Logistic Regression** classifier providing interpretable and efficient genre predictions
- **Multi-class support** for a wide range of movie genres
- **Interactive demo** accessible online via Hugging Face Spaces

---

## How to Use

### Locally

1. Clone the repository.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
Run the application:

bash

python app.py
Access the local interface, input a movie plot summary, and receive genre predictions.

Online Demo
Access the deployed model with an intuitive UI at:
https://huggingface.co/spaces/Trashika112/Movie-genre-classifier

Project Structure
app.py — Gradio web interface for inference

logistic_model.pkl — Serialized Logistic Regression model

tfidf_vectorizer.pkl — Serialized TF-IDF vectorizer

label_encoder.pkl — Label encoder for genre categories

requirements.txt — Project dependencies

Dependencies
Python 3.7+

scikit-learn

joblib

gradio

pandas

numpy

For full environment setup, use:

bash

pip install -r requirements.txt

License
This project is licensed under the MIT License. See the LICENSE file for details.













