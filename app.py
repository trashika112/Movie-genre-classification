
import gradio as gr
import joblib

# Load model and vectorizer
model = joblib.load("logistic_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")

def predict_genre(plot_summary):
    X = vectorizer.transform([plot_summary])
    pred = model.predict(X)
    genre = label_encoder.inverse_transform(pred)[0]
    return f"Predicted Genre: {genre}"

interface = gr.Interface(
    fn=predict_genre,
    inputs=gr.Textbox(label="Enter Movie Plot Summary", lines=5, placeholder="e.g. A young boy discovers he's a wizard..."),
    outputs=gr.Textbox(label="Predicted Genre"),
    title="🎬 Movie Genre Classifier",
    description="Enter a movie plot summary to predict its genre using a Logistic Regression model trained on TF-IDF features."
)

if __name__ == "__main__":
    interface.launch()
