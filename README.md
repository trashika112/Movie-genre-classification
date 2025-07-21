# Movie Genre Classifier using Logistic Regression and TF-IDF

This repository contains a machine learning model that predicts movie genres based on plot summaries. The model uses TF-IDF vectorization combined with a Logistic Regression classifier to categorize movies into multiple genres.

## Live Demo

You can interact with the trained model directly on Hugging Face Spaces:  
[https://huggingface.co/spaces/Trashika112/Movie-genre-classifier](https://huggingface.co/spaces/Trashika112/Movie-genre-classifier)

## Project Description

Movie genre classification from plot summaries is an important NLP task. This project leverages:

- **TF-IDF Vectorization:** To extract meaningful textual features from movie plots.  
- **Logistic Regression:** An efficient and interpretable classifier for multiple genres.  
- **Gradio Interface:** A user-friendly web app for real-time predictions.  
- **Multi-genre Support:** Handles classification across various movie genres.

## Setup and Usage

### Clone the Repository
```bash
git clone https://github.com/Trashika112/Movie-Genre-Classifier.git  
cd Movie-Genre-Classifier
Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Run the App
bash
Copy
Edit
python app.py
Project Files
app.py — Gradio web interface for inference

logistic_model.pkl — Trained Logistic Regression model

tfidf_vectorizer.pkl — TF-IDF vectorizer used for feature extraction

label_encoder.pkl — Label encoder for genre categories

requirements.txt — Python dependencies

Dependencies
scikit-learn

joblib

gradio

pandas

numpy

Dataset
The model was trained on the IMDB Genre Classification Dataset, which contains movie plot summaries and genre labels.

Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. Follow the code of conduct.

Future Work
Improve performance using transformer-based models (e.g., BERT)

Support multi-label classification for movies with multiple genres

Deploy as a mobile or desktop app

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Trashika S Karkera

yaml
Copy
Edit
