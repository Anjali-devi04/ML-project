import pandas as pd
import os

current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, "..", "dataset", "student-mat.csv")
df = pd.read_csv(csv_path, sep=";")

# 1. Average Marks

print("\nAverage Marks")
print("Average G1 :", round(df["G1"].mean(),2))
print("Average G2 :", round(df["G2"].mean(),2))
print("Average G3 :", round(df["G3"].mean(),2))

# 2. Students grouped by Gender

print("\nStudents by Gender")
print(df.groupby("sex").size())

# 3. Pass Percentage

# Passing mark = 10
passed = df[df["G3"] >= 10]
pass_percentage = (len(passed)/len(df))*100
print("\nPass Percentage")
print(round(pass_percentage,2),"%")


# 4. Top Performers

print("\nTop 10 Students")
top_students = df.sort_values(by="G3", ascending=False)
print(top_students[["sex","age","studytime","absences","G3"]].head(10))