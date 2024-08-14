from flask import Flask, request, render_template
import pandas as pd
from model import train_model, predict_price

model = train_model()
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    price = None
    if request.method == 'POST':
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])
        size = int(request.form['size'])
        location = request.form['location']
       
        data = pd.read_csv('house_data.csv')
        dummy_columns = pd.get_dummies(data['location'], drop_first=True).columns
        
        features = [bedrooms, bathrooms, size]
        for col in dummy_columns:
            if col == location:
                features.append(1)
            else:
                features.append(0)
        
        price = predict_price(model, features)
        price = f"{price:.2f}"
    
    return render_template('index.html', price=price)

if __name__ == "__main__":
    app.run(debug=True)

