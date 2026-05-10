from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("phishing_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']

    prediction = model.predict([url])[0]
    prob = model.predict_proba([url])[0]
    confidence = round(max(prob) * 100, 2)

    if prediction == 1:
        result = "PHISHING WEBSITE DETECTED"
        color = "red"
    else:
        result = "SAFE WEBSITE"
        color = "green"

    return render_template("result.html",
                           url=url,
                           result=result,
                           confidence=confidence,
                           color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)