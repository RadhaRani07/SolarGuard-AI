
# SolarGuard AI

## Project Overview
SolarGuard AI is an educational AI project that classifies solar panel images into six condition categories using a ResNet18 deep learning model.

## Classes
- Clean
- Dusty
- Bird-drop
- Physical-Damage
- Electrical-damage
- Snow-Covered

## Technology Used
- Python
- PyTorch
- ResNet18
- Streamlit
- Pillow

## Model Evaluation
The model achieved 86.47% accuracy on the held-out test dataset during the training experiment.

External photo tests were also performed. Some predictions matched the expected class, while a cracked-panel image was incorrectly classified as Electrical-damage.

## Limitations
- This is an educational prototype, not an industrial inspection system.
- Confidence scores are not guarantees of correctness.
- Electrical damage cannot be reliably confirmed from an image alone.
- More diverse and carefully labelled images are needed for further evaluation.

## How to Run
1. Install the required Python packages.
2. Keep app.py, class_names.json, and solarguard_experiment2.pth in the same folder.
3. Run the application using:
   streamlit run app.py

## Author
Created as an AI/ML learning project.
