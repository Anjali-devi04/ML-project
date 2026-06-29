import os
import joblib
import pandas as pd

# Load trained model
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "student_marks_model.pkl")

model = joblib.load(model_path)

def predict_marks(
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
    absences
):

    data = pd.DataFrame([{
        "age": age,
        "sex": sex,
        "famsize": famsize,
        "Medu": Medu,
        "Fedu": Fedu,
        "traveltime": traveltime,
        "studytime": studytime,
        "failures": failures,
        "schoolsup": schoolsup,
        "famsup": famsup,
        "internet": internet,
        "famrel": famrel,
        "goout": goout,
        "health": health,
        "absences": absences
    }])

    prediction = model.predict(data)

    return round(prediction[0], 2)


# Test the model
if __name__ == "__main__":

    result = predict_marks(
        age=17,
        sex=0,
        famsize=1,
        Medu=3,
        Fedu=3,
        traveltime=2,
        studytime=2,
        failures=0,
        schoolsup=0,
        famsup=1,
        internet=1,
        famrel=4,
        goout=3,
        health=5,
        absences=4
    )

    print("Predicted Marks:", result)