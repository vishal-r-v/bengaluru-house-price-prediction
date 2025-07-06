# bengaluru-house-price-prediction
# 🏡 Bengaluru House Price Prediction

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Built with: Flask + ML](https://img.shields.io/badge/Built%20With-Flask%20%7C%20RandomForest-blue)

A machine learning web application built with Flask to predict housing prices in Bengaluru based on area type, location, size, square footage, number of bathrooms, and balconies.

---

## 📊 Features

- Predict price of a house based on key input features
- Trained with `RandomForestRegressor` on Bengaluru housing data
- Frontend form with modern glassmorphism UI
- Backend built with Flask and scikit-learn
- Real-time prediction rendered on the same page

---

## 🧠 Technologies Used

- Python 3.x
- Flask
- scikit-learn (Random Forest Regressor)
- Pandas, NumPy
- HTML, CSS (inline in `index.html`)
- Jupyter Notebook (for model training)

---

## 📁 Folder Structure

bengaluru-house-price-prediction/
├── app.py # Flask web app to serve predictions
├── train_model.py # Model training script
├── Bengaluru_House_Data.csv # Raw dataset
├── model.pkl # Trained model file
├── columns.pkl # Feature columns saved for inference
├── templates/
│ └── index.html # Web form UI + result display
├── LICENSE # MIT license
└── README.md # This file
├── Output/
│ └── predict.jpg # webpage display
│ └── result.jpg # prediction result display

---

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/bengaluru-house-price-prediction.git
   cd bengaluru-house-price-prediction
2. Install dependencies:
   ```bash
   pip install flask pandas scikit-learn
3. Run the Flask app:
   ```bash
   python app.py
4. Open your browser and go to:
   ```cpp
   http://127.0.0.1:5000

---

🧪 Inputs Expected
Area Type: Super built-up / Plot / Built-up / Carpet

Location: Any locality (e.g., Whitefield)

Size: Format like 2 BHK, 3 BHK

Total Sqft: Numeric value

Bathrooms: Number of bathrooms

Balconies: Number of balconies

---

📦 Dataset
The dataset used is:
Bengaluru_House_Data.csv (included in this repo)

---

📜 License
This project is licensed under the MIT License.

---

👨‍💻 Author
vishal r v
B.Tech, Artificial Intelligence and Machine Learning
SRM Institute of Science and Technology, Ramapuram
