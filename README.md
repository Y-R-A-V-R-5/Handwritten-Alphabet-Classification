# **Handwritten Alphabet Classification using Deep Learning**  

### **📌 Project Overview**  
This project focuses on **handwritten alphabet classification** using **CNNs, RNNs, and hybrid models** trained on uppercase (A-Z) and lowercase (a-z) English alphabets. The system includes **data preprocessing, model training, hyperparameter tuning, performance evaluation, and deployment via Streamlit** for real-time classification.  

---

## **📂 Project Directory Structure with Images**  

```
📁 Handwritten_Alphabet_Classification  
│── 📁 plots/                # Model architecture & performance plots  
│── 📁 gradients/            # Gradient-based visualizations (Grad-CAM)  
│── 📁 save/                 # Saved models and classification outputs  
│   ├── 📁 no_tune/          # Non-tuned models (.h5 files)  
│   ├── 📁 tune/             # Tuned models (.keras files)  
│── 📁 deployment/        # Streamlit deployment files  
│   ├── main.py              # Main Streamlit application  
│   ├── models.py            # Model selection and loading  
│   ├── classification.py    # Classification interface  
│   ├── about_me.py          # About the developer  
│   ├── nn_models.py         # Model architecture descriptions  
│   ├── utils.py             # Utility functions (preprocessing, visualization)  
│   ├── style.css            # Custom CSS for UI styling  
│── requirements.txt         # Dependencies  
│── README.md                # Project Documentation  
```
---

## **🧠 Deep Learning Models Used**
The following **six models** were implemented:  
✅ **CNN-based Models:**  
- **LeNet-5** – Lightweight CNN for character recognition.  
- **VGG-16** – Deep CNN for robust feature extraction.  

✅ **RNN-based Models:**  
- **LSTM** – Captures handwriting sequence dependencies.  
- **GRU** – Optimized RNN variant.  

✅ **Hybrid Models (CNN + RNN):**  
- **LeNet5-GRU** – CNN for spatial features & GRU for sequence modeling.  
- **VGG16-GRU** – Uses deep feature extraction from VGG-16 with GRU.  

---

## **🔬 Model Training & Evaluation**
📌 **Training Pipeline:**  
- Models trained using **Categorical Cross-Entropy Loss** with **Adam, SGD, and RMSprop optimizers**.  
- Tuned models optimized via **Random Search (5 trials)**, trained for **50 epochs with Early Stopping**.  

📌 **Visualization & Interpretability:**  
✅ **Confusion Matrix** – Highlights misclassifications.  
✅ **Grad-CAM** – Shows CNN focus areas.  .  

---

## **🌐 Model Deployment**
The trained models are deployed using **Streamlit**.  

📌 **Deployment Features:**  
✔ **Upload handwritten character images (JPG, PNG, JPEG).**  
✔ **Select model(s) for classification.**  
✔ **View prediction results with confidence scores.**  
✔ **Compare predictions from multiple models.**  
✔ **Download classification results.**  

Run the **Streamlit App** locally:  
```bash
streamlit run main.py
```

---

## **📦 Installation & Setup**
1️⃣ **Clone the Repository:**  
```bash
git clone https://github.com/Y-R-A-V-R-5/Handwritten_Alphabet_Classification.git
cd Handwritten_Alphabet_Classification
```
2️⃣ **Create Virtual Environment (Recommended):**  
```bash
python -m venv venv
source venv\Scripts\activate
```
3️⃣ **Install Dependencies:**  
```bash
pip install -r requirements.txt
```
4️⃣ **Run Streamlit Application:**  
```bash
streamlit run models.py
```

---

## **📚 Requirements**
A **`requirements.txt`** file is provided:  
```txt
tensorflow==2.12.0
keras==2.12.0
numpy==1.23.5
scipy==1.10.1
pandas==1.5.3
scikit-learn==1.2.2
opencv-python==4.7.0.72
Pillow==9.5.0
matplotlib==3.7.1
streamlit==1.18.0
```

---

## **🔗 References**
- **Deep Learning Frameworks**: TensorFlow, Keras  
- **Visualization Tools**: Matplotlib, Seaborn, Grad-CAM  
- **Deployment**: Streamlit  

🔹 **Author**: Adithya Vardhan Reddy  
🔹 **Institution**: Kapil IT Skill Hub  

📌 **Dataset**:  [Handwritten images](https://drive.google.com/drive/folders/1LRNMUi1tiwbFxk7r-r0KVWaRnrixCdUa?usp=drive_link)

📌 **GitHub Repository**: [Project Link](https://github.com/Y-R-A-V-R-5/Handwritten_Alphabet_Classification)  

---
