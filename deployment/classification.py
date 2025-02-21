import streamlit as st
from PIL import Image
from utilis import load_models, preprocess_image, make_predictions, plot_predictions  # Import from utils.py

def classification_page():
    st.title("🔍 Image Classification")

    st.header("📷 Make a Prediction")

    # Model Selection
    st.subheader("🧠 Select Models")

    model_type = st.selectbox("Choose Model Type", ["Non-Tuned", "Tuned"], label_visibility="collapsed")

    if model_type == "Non-Tuned":
        model_names = ["LeNet-5", "VGG-16", "LSTM", "GRU", "LeNet5-GRU", "VGG16-GRU"]
        model_paths = {name: f"../save/no_tune/{name.lower()}.h5" for name in model_names}
    else:  # Tuned
        model_names = ["LeNet-5", "VGG-16", "LeNet5-GRU", "VGG16-GRU"]
        model_paths = {name: f"../save/tune/{name.lower()}.keras" for name in model_names}

    selected_models = st.multiselect("Select Models", model_names, max_selections=3, label_visibility="collapsed")  # Allow up to 3 selections.

    if not selected_models:  # Check if models are selected.
        st.warning("⚠️ Please select at least one model.")
        return  # Exit early if no models selected.

    with st.spinner("🔄 Loading Models..."):
        models_to_predict = {}
        for model_name in selected_models:
            if model_name in model_paths:
                models_to_predict = load_models({model_name: model_paths[model_name] for model_name in selected_models})
            else:
                st.error(f"❌ Model path not found for {model_name}")
                return

    # Image Upload
    st.subheader("📂 Upload Image")
    uploaded_image = st.file_uploader("Upload an image for classification", type=["jpg", "png", "jpeg"])

    if uploaded_image:
        try:
            # Preprocess uploaded image directly without saving to /tmp
            img_array = preprocess_image(uploaded_image, target_size=(64, 64))
            if img_array is None:
                st.error("⚠️ Image preprocessing failed.")
                return

            with st.spinner("🤖 Classifying Image..."):
                predictions = make_predictions(models_to_predict, img_array)

            if predictions is None:
                st.error("❌ Classification failed.")
                return

            col1, col2, col3 = st.columns([1, 1, 2])  # Adjust column ratios as needed.

            with col1:
                img = Image.open(uploaded_image)
                aspect_ratio = img.width / img.height
                max_width = 375  # Adjust as needed
                new_height = int(max_width / aspect_ratio)
                resized_img = img.resize((max_width, new_height))
                st.image(resized_img, caption="🖼️ Uploaded Image", use_column_width=False)
                st.markdown("---")

            if predictions:  # Check if results are not None (handle errors in classify_image)
                # Classification Results (col3)
                with col3:
                    st.subheader("📊 Classification Results")
                    for model_name, result in predictions.items():
                        st.write(f"**🧠 Model:** {model_name}")
                        st.success(f"🏷️ Prediction: **{result['label']}**")
                        st.info(f"✅ Confidence: **{result['confidence']:.2f}%**")
                        st.write("🔝 Top 5 Predictions:")
                        for lbl, conf in result['top_5'].items():
                            st.write(f"- {lbl}: {conf:.2f}%")
                        st.markdown("---")

                plot_predictions(predictions)  # Call plotting function from utils.py

            else:
                st.error("❌ Classification failed. Please check the uploaded image and model paths.")

        except Exception as e:
            st.error(f"🚨 An error occurred: {e}")

    else:
        st.info("ℹ️ Please upload an image and select at least one model to proceed.")