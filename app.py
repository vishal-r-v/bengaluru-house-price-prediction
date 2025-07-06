from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model and data columns
model = pickle.load(open('model.pkl', 'rb'))
data_columns = pickle.load(open('columns.pkl', 'rb'))  # This should include area_type, location, size, etc.

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        area_type = request.form.get('area_type')
        location = request.form.get('location')
        size = request.form.get('size')
        total_sqft = float(request.form.get('total_sqft'))
        bath = int(request.form.get('bath'))
        balcony = int(request.form.get('balcony'))

        # Construct feature vector
        input_dict = {
            'area_type': area_type,
            'location': location,
            'size': size,
            'total_sqft': total_sqft,
            'bath': bath,
            'balcony': balcony
        }

        # One-hot encode manually
        df = pd.DataFrame([input_dict])
        df_final = pd.get_dummies(df)

        # Make sure all columns match training data
        missing_cols = [col for col in data_columns if col not in df_final.columns]
        for col in missing_cols:
            df_final[col] = 0
        df_final = df_final[data_columns]  # Order columns

        prediction = model.predict(df_final)[0]
        final_price = round(prediction, 2)

        return render_template('index.html', prediction=final_price)

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
