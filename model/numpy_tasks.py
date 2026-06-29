import os
import pandas as pd
import numpy as np

current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, "..", "dataset", "student-mat.csv")
df = pd.read_csv(csv_path, sep=";")

marks = df["G3"].to_numpy()

# Mean
print(f"\nMean Marks: {np.mean(marks):.2f}")

# Median
print(f"Median Marks: {np.median(marks):.2f}")

# Standard Deviation
print(f"Standard Deviation: {np.std(marks):.2f}")

# Percentiles
print(f"\n25th Percentile : {np.percentile(marks,25)}")
print(f"50th Percentile : {np.percentile(marks,50)}")
print(f"75th Percentile : {np.percentile(marks,75)}")