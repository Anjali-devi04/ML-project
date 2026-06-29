from flask import Flask, render_template, request

from model.predict import predict_marks
from utils.feedback import generate_feedback

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    age = int(request.form["age"])
    sex = int(request.form["sex"])
    famsize = int(request.form["famsize"])
    Medu = int(request.form["Medu"])
    Fedu = int(request.form["Fedu"])
    traveltime = int(request.form["traveltime"])
    studytime = int(request.form["studytime"])
    failures = int(request.form["failures"])
    schoolsup = int(request.form["schoolsup"])
    famsup = int(request.form["famsup"])
    internet = int(request.form["internet"])
    famrel = int(request.form["famrel"])
    goout = int(request.form["goout"])
    health = int(request.form["health"])
    absences = int(request.form["absences"])

    prediction = predict_marks(
        age,
        sex,
        famsize,
        Medu,
        Fedu,
        traveltime,
        studytime,
        failures,
        schoolsup,
        famsup,
        internet,
        famrel,
        goout,
        health,
        absences,
    )

    level, suggestions = generate_feedback(
        prediction,
        studytime,
        failures,
        absences,
        goout,
        health,
        internet,
        famsup,
        schoolsup,
    )

    return render_template(
        "index.html",
        prediction=round(prediction,2),
        level=level,
        suggestions=suggestions
    )


if __name__ == "__main__":
    app.run(debug=True)