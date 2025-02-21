import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import streamlit as st
from tensorflow.keras.models import load_model # type: ignore

def load_models(model_paths):
    models = {}
    for name, path in model_paths.items():
        try:
            models[name] = load_model(path)  # Load the model here
        except Exception as e:
            print(f"Failed to load {name} from {path}: {e}")
    return models

def make_predictions(models_to_predict, img_array):
    predictions = {}
    for model_name, model in models_to_predict.items():
        # Ensure we have a model instance, not a dictionary
        if not hasattr(model, "predict"):
            raise TypeError(f"{model_name} is not a valid model object")

        # Make prediction
        pred = model.predict(img_array)[0]  # Batch size = 1
        top_5_indices = np.argsort(pred)[-5:][::-1]
        top_5 = {chr(65 + i) if i < 26 else chr(97 + i - 26): round(pred[i] * 100, 2) for i in top_5_indices}

        # Predicted label
        predicted_idx = np.argmax(pred)
        label = chr(65 + predicted_idx) if predicted_idx < 26 else chr(97 + predicted_idx - 26)
        confidence = round(pred[predicted_idx] * 100, 2)

        predictions[model_name] = {
            "label": label,
            "confidence": confidence,
            "top_5": top_5
        }

    return predictions

def preprocess_image(image_path, target_size=(64, 64)):
    try:
        # Open image and convert to RGB
        img = Image.open(image_path).convert("RGB")
        img = img.resize(target_size)
        img_array = np.array(img) / 255.0  # Normalize
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        return img_array
    except Exception as e:
        print(f"Failed to preprocess image: {e}")
        return None

def plot_predictions(predictions):
    """Plot prediction probabilities for the top 5 predictions of each model."""

    num_models = len(predictions)
    fig, axes = plt.subplots(num_models, 1, figsize=(8, 6 * num_models))

    if num_models == 1:
        axes = [axes]

    for i, (model_name, result) in enumerate(predictions.items()):
        top_5 = sorted(result['top_5'].items(), key=lambda item: convert_to_float(item[1]), reverse=True)[:5]
        labels = [f"{label}: {prob}" for label, prob in top_5]
        probabilities = [convert_to_float(prob) for _, prob in top_5]

        ax = axes[i]
        ax.barh(labels, probabilities, color='skyblue')
        ax.set_xlabel("Confidence (%)")
        ax.set_title(f"Top 5 classification probabilities of {model_name}")
        ax.invert_yaxis()
        ax.set_xlim(0, 100)
        for label, prob in zip(labels, probabilities):
            ax.text(prob + 1, label, f'{prob:.2f}%', va='center')

    plt.tight_layout()
    st.pyplot(fig)


def convert_to_float(value):
    """Converts a value (string or number) to a float."""
    if isinstance(value, str):
        try:
            return float(value.strip('%'))
        except ValueError:  # Handle cases where stripping and converting fails.
            st.error(f"Could not convert '{value}' to float. Check prediction output.")
            return 0.0 # Return a default value.
    elif isinstance(value, (int, float, np.float64)):  # Check for int, float, or numpy float
        return float(value)
    else:
        st.error(f"Unexpected value type: {type(value)}. Check prediction output.")
        return 0.0

def classify_image(uploaded_image, model_paths):
    """Classify an uploaded image using the selected models."""
    models = load_models(model_paths)
    image, image_array = preprocess_image(uploaded_image)
    predictions = make_predictions(models, image_array)
    plot_predictions(predictions, image)
    return predictions

def plot_predict(predictions):
    if not predictions:
        st.warning("No predictions to display.")
        return

    num_models = len(predictions)
    fig, axes = plt.subplots(num_models, 1, figsize=(8, 6 * num_models))

    # Ensure axes is iterable even if there's only one model
    if num_models == 1:
        axes = [axes]

    for ax, (model_name, result) in zip(axes, predictions.items()):
        top_labels = list(result["top_5"].keys())
        top_probs = list(result["top_5"].values())

        ax.barh(top_labels, top_probs, color="skyblue")
        ax.set_xlabel("Confidence (%)")
        ax.set_title(f"Top 5 Predictions - {model_name}")
        ax.invert_yaxis()

    plt.tight_layout()
    st.pyplot(fig)

def save_summary_to_csv(predictions, file_path="prediction_summary.csv"):
    """Save prediction summary to CSV."""
    import pandas as pd
    summary = {
        "Model": [],
        "Predicted Label": [],
        "Confidence (%)": []
    }
    for model_name, result in predictions.items():
        summary["Model"].append(model_name)
        summary["Predicted Label"].append(result['label'])
        summary["Confidence (%)"].append(result['confidence'])

    df = pd.DataFrame(summary)
    df.to_csv(file_path, index=False)
    st.success(f"Prediction summary saved to {file_path}")