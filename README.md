# ☀️ SolarGuard AI

### AI-Based Solar Panel Condition Classification

SolarGuard AI is a deep learning project that classifies solar panel images into six condition categories using a fine-tuned ResNet18 model. The project provides a simple web interface built with Streamlit.

## 🚀 Live Demo

[Try SolarGuard AI](https://solarguard-ai-rcyucvvpewvauew5zk4s6h.streamlit.app/)

## 🖼️ App Screenshots

### 1. SolarGuard AI — Prediction Result

![Prediction Result](Screenshot%202026-10-20%20183823.png)

### 2. SolarGuard AI — Screenshot 2

![SolarGuard AI Screenshot 2](Screenshot%202026-10-20%20183838.png)

### 3. SolarGuard AI — Screenshot 3

![SolarGuard AI Screenshot 3](Screenshot%202026-10-20%20183847.png)


## 🎯 Project Objective

The objective is to explore how computer vision can help identify different visible solar panel conditions from images.

## 🔍 Supported Classes

- Clean
- Dusty
- Bird-drop
- Physical-Damage
- Electrical-damage
- Snow-Covered

## 🛠️ Technologies Used

- Python
- PyTorch
- Torchvision
- ResNet18 Transfer Learning
- Streamlit
- Pillow

## 📊 Model Performance

- **Test Accuracy:** 86.47%
- **Test Images:** 133
- **Model:** Fine-tuned ResNet18
- **Dataset Size:** 885 images

These results are from the project's recorded test evaluation. Performance may vary on new images, and predictions should be treated as estimates.

## ⚙️ How to Use

1. Open the live demo.
2. Upload a solar panel image in JPG, JPEG, or PNG format.
3. Click **Predict Condition**.
4. Review the predicted class, confidence score, and class probabilities.

## ⚠️ Limitations

This is an educational AI prototype. Predictions are not a substitute for professional solar panel inspection. Image-based classification may not detect hidden cracks or internal electrical faults reliably.

## 🔮 Future Improvements

- Expand and improve the training dataset.
- Evaluate performance on more real-world images.
- Improve classification of damaged and dusty panels.
- Enhance the user interface and model evaluation.

## 👩‍💻 Project Status

The model has been trained and evaluated, and a Streamlit web demo is deployed.

## 🧪 Sample Image Testing

SolarGuard AI was manually tested on six sample images.

| Metric | Result |
|---|---:|
| Sample images tested | 6 |
| Correct predictions | 5 |
| Incorrect predictions | 1 |
| Sample accuracy | 83.33% |

### Observations

- Clean, Dusty, Bird-drop, and Snow-Covered examples were classified correctly in the recorded tests.
- One Physical-Damage example was incorrectly classified as Electrical-damage.
- These results represent a small sample and should not be confused with the full test-set accuracy.

The model achieved **86.47% accuracy on the recorded 133-image test set** during model evaluation. Performance on new images may vary.


## 💻 Run Locally

### 1. Clone the repository

git clone https://github.com/RadhaRani07/SolarGuard-AI.git

### 2. Open the project folder

cd SolarGuard-AI

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the Streamlit app

streamlit run app.py
