import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def train_model():
    data = pd.read_csv('house_data.csv')
    
    data = pd.get_dummies(data, columns=['location'], drop_first=True)
    
    X = data.drop('price', axis=1)
    y = data['price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model

def predict_price(model, features):
    return model.predict([features])[0]
