import os
import pandas as pd


def load_and_preprocess():

    current_dir = os.path.dirname(__file__)
    csv_path = os.path.join(current_dir, "..", "dataset", "student-mat.csv")
    df = pd.read_csv(csv_path, sep=";")

    df = df[
        [
            "age",
            "sex",
            "famsize",
            "Medu",
            "Fedu",
            "traveltime",
            "studytime",
            "failures",
            "schoolsup",
            "famsup",
            "internet",
            "famrel",
            "goout",
            "health",
            "absences",
            "G3",
        ]
    ]

    df["sex"] = df["sex"].map({"F": 0, "M": 1})
    df["famsize"] = df["famsize"].map({"LE3": 0, "GT3": 1})
    df["schoolsup"] = df["schoolsup"].map({"no": 0, "yes": 1})
    df["famsup"] = df["famsup"].map({"no": 0, "yes": 1})
    df["internet"] = df["internet"].map({"no": 0, "yes": 1})

    return df

# Run only if this file is executed directly
if __name__ == "__main__":

    processed_df = load_and_preprocess()
    print(processed_df.head())
    print("\nShape:", processed_df.shape)