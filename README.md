# House Predication
This is a simple Flask web application to predict house prices based on input features using a machine learning model.

## Features
- Number of Bedrooms
- Number of Bathrooms
- Size in Square Feet
- Location

# Setup Instruction
1. Install a virtual environmental for this flask app using: `pip install virtualenv`.
2. Create a virtual environmental using: `virtualenv env`.
3. Activate the virtual environmental using: `.\env\Scripts\activate.ps1`.
4. Install necessary packages and library to implements the task: `pip install pands flask scikit-learn` inside the env.
5. Run the application: `python app.py`
6. Open the browser and nevigate to `http://127.0.0.1:5000`

# Project Overview
1. Create a model to predicate the house price where we are using Linear regression model to train the model using `house_data.csv` file to train the model.
2. Using `pd.get_dummies` function to convert categorical variable into dummy/indicator variables.
3. Create templates for form development and fill in the form with the house features (e.g., number of bedrooms, bathrooms, size in square feet, and location).
4.  Click the "Predict Price" button to get the predicted house price
5. Create a index function in `app.py` it will predicated the price based the form of data you filled.

# Prediction
The predicted house price is displayed on the same page after submitting the form.

# Snapshots
![empty_form](https://github.com/user-attachments/assets/6812a31c-9a69-4328-8d6a-70f38b1f2ba3)
![predicate_price](https://github.com/user-attachments/assets/d5eca185-8e69-4385-a376-59c333aab09f)

