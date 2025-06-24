import pandas as pd
import joblib
from flask import (
    Flask,
    url_for,
    render_template
)
from forms import InputForm

model = joblib.load("model.joblib")
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

@app.route('/')
def index():
    return render_template("home.html", title="Home")

@app.route('/home')
def home():
    return render_template("home.html", title="Home")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = InputForm()
    if form.validate_on_submit():
        x_new = pd.DataFrame(dict(
            age=[form.age.data],
            sex=[form.sex.data],
            cp=[form.cp.data],
            trestbps=[form.trestbps.data],
            chol=[form.chol.data],
            fbs=[form.fbs.data],
            restecg=[form.restecg.data],
            thalach=[form.thalach.data],
            exang=[form.exang.data],
            oldpeak=[form.oldpeak.data],
            slope=[form.slope.data],
            ca=[form.ca.data],
            thal=[form.thal.data]
        ))
        
       
        prediction = model.predict(x_new)[0]
        
        
        if prediction > 0.5:
            risk_level = "HIGH RISK"
            message = f"⚠️ High Risk of Heart Disease (Score: {prediction:.3f})"
            recommendation = "Please consult with a cardiologist for further evaluation."
            risk_class = "high-risk"
        else:
            risk_level = "LOW RISK"
            message = f"✅ Low Risk of Heart Disease (Score: {prediction:.3f})"
            recommendation = "Maintain a healthy lifestyle and regular check-ups."
            risk_class = "low-risk"
        
        
        confidence = abs(prediction - 0.5) * 2  
        probability_percent = prediction * 100
        
        result_data = {
            'prediction': prediction,
            'risk_level': risk_level,
            'message': message,
            'recommendation': recommendation,
            'risk_class': risk_class,
            'confidence': f"{confidence:.1%}",
            'probability': f"{probability_percent:.1f}%"
        }
        
    else:
        message = "Please provide valid input details!"
        result_data = None
    
    return render_template("predict.html", 
                         title="Predict", 
                         form=form, 
                         output=message,
                         result=result_data)

if __name__ == "__main__":
    app.run(debug=True, port=7341)