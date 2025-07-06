import streamlit as st
import os
from PIL import Image

def nn_models_page():
    st.title("Neural Network Architectures")

    st.header("Model Architectures")

    st.write("""
    This page provides an overview of the neural network architectures used in this app.
    Click on the expanders below to explore each model.
    """)

    # General information about neural networks (moved outside the loop)
    st.write("Neural Networks have revolutionized the way we handle various machine learning tasks. Different models are suited for different types of data, whether it's sequential, image, or text data.")
    st.write("In this project, we have explored various models like LeNet-5, VGG-16, GRU, LSTM, and hybrid models to classify handwritten alphabet images.")

    base_dir = os.path.dirname(__file__)  # Current file directory
    plots_dir = os.path.join(base_dir, "../plots")

    model_info = {
        "LeNet-5": {
            "image_path": os.path.join(plots_dir, "LeNet-5.png"),
            "description": """
            LeNet-5 is a classic CNN architecture with convolutional layers, 
            max-pooling, and fully connected layers.
            """,
            "details": """
            - **Key Features:** Convolutional layers (5x5 filters), max pooling, and dense layers.
            - **Strengths:** Simple and effective for handwritten character recognition.
            - **Limitations:** Shallow compared to modern architectures.
            - **Applications:** Handwritten digit/image classification.
            """
        },
        "VGG-16": {
            "image_path": os.path.join(plots_dir, "VGG-16.png"),
            "description": """
            VGG-16 is a deep CNN architecture with multiple layers of 3x3 filters.
            """,
            "details": """
            - **Key Features:** Repeated 3x3 convolutional layers, max pooling, and fully connected layers.
            - **Strengths:** High performance in image classification tasks.
            - **Limitations:** High computational cost.
            - **Applications:** Image classification, object detection.
            """
        },
        "LSTM": {
            "image_path": os.path.join(plots_dir, "LSTM.png"),
            "description": """
            LSTM is an RNN variant designed to capture long-term dependencies in sequential data.
            """,
            "details": """
            - **Key Features:** Memory cells, input/output gates, and forget gates.
            - **Strengths:** Excels at time-series and sequential data tasks.
            - **Limitations:** Computationally intensive compared to simpler RNNs.
            - **Applications:** NLP, time-series analysis.
            """
        },
        "GRU": {
            "image_path": os.path.join(plots_dir, "GRU.png"),
            "description": """
            GRU is a simpler, faster alternative to LSTMs for sequential data.
            """,
            "details": """
            - **Key Features:** Update and reset gates.
            - **Strengths:** Similar performance to LSTMs with reduced complexity.
            - **Limitations:** Slightly less flexible than LSTMs.
            - **Applications:** NLP, time-series forecasting.
            """
        },
        "LeNet5-GRU": {
            "image_path": os.path.join(plots_dir, "LeNet5-GRU.png"),
            "description": """
            Combines LeNet-5's feature extraction with GRU's sequential pattern detection.
            """,
            "details": """
            - **Key Features:** CNN for spatial features, GRU for temporal patterns.
            - **Strengths:** Leverages strengths of both architectures.
            - **Limitations:** More complex to train.
            - **Applications:** Handwritten character recognition.
            """
        },
        "VGG16-GRU": {
            "image_path": os.path.join(plots_dir, "VGG16-GRU.png"),
            "description": """
            Combines VGG-16's feature extraction with GRU's sequential capabilities.
            """,
            "details": """
            - **Key Features:** Deep CNN layers followed by GRU units.
            - **Strengths:** Strong feature extraction with sequence understanding.
            - **Limitations:** High computational cost.
            - **Applications:** Handwritten text/image recognition.
            """
        }
    }

    for model_name, info in model_info.items():
        with st.expander(f"🔍 {model_name}"):
            col1, col2 = st.columns([2, 5])

            # Display model image
            with col1:
                if os.path.exists(info["image_path"]):
                    try:
                        img = Image.open(info["image_path"])
                        st.image(img, caption=f"{model_name} Architecture", use_column_width=True)
                    except Exception as e:
                        st.error(f"Failed to load image: {e}")
                else:
                    st.warning(f"Image not found: {info['image_path']}")

            # Display description and details
            with col2:
                st.markdown(f"**{model_name}**")
                st.write(info["description"])
                st.markdown(info["details"])

    st.info("These models are trained to classify handwritten alphabet images with 52 labels (A-Z, a-z).")
