# 🎬 Movie Genre Classifier using Logistic Regression and TF-IDF

This repository contains a machine learning model that predicts movie genres based on plot summaries. It uses **TF-IDF vectorization** combined with a **Logistic Regression** classifier to categorize movies into multiple genres.

---

## 🚀 Live Demo

You can try the model directly on Hugging Face Spaces:  
👉 [https://huggingface.co/spaces/Trashika112/Movie-genre-classifier](https://huggingface.co/spaces/Trashika112/Movie-genre-classifier)

---

## 📌 Project Description

Movie genre classification from plot summaries is a useful NLP task in the field of content recommendation and metadata enrichment. This project includes:

- ✅ **TF-IDF Vectorization:** Extracts informative textual features from plot summaries.
- ✅ **Logistic Regression Classifier:** Interpretable and efficient for multi-class classification.
- ✅ **Gradio Web Interface:** Allows real-time user interaction for predictions.
- ✅ **Multi-genre Support:** Handles various common movie genres.

---

## 🛠️ Setup and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/trashika112/Movie-genre-classification.git
cd Movie-genre-classification
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

## 📁 Project Files

- `app.py` – Gradio interface script for genre prediction  
- `logistic_model.pkl` – Trained Logistic Regression model  
- `tfidf_vectorizer.pkl` – Fitted TF-IDF vectorizer  
- `label_encoder.pkl` – Label encoder for genre names  
- `requirements.txt` – Python dependencies list

---

## 📦 Dependencies

- `scikit-learn`  
- `joblib`  
- `gradio`  
- `pandas`  
- `numpy`

Install them using:

```bash
pip install -r requirements.txt
```

---

## 📊 Dataset

This model is trained on the **IMDB Genre Classification Dataset** from kaggle, which includes thousands of movie plot summaries labeled by genre.

---

## 🤝 Contributing

Contributions are welcome!  
If you'd like to contribute:

1. Fork the repository  
2. Create a new branch 
3. Commit your changes  
4. Push to the branch 
5. Open a pull request



---

## 🔮 Future Work

- 🔁 Improve performance using transformer-based models like BERT  
- 📚 Add support for **multi-label** genre classification  
- 📱 Deploy as a mobile or desktop application

---

## 📄 License

This project is licensed under the **MIT License**. 

---

## 👩‍💻 Author
**Trashika S Karkera**  
