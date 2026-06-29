import os
import pandas as pd
import matplotlib.pyplot as plt

from preprocess import load_and_preprocess

# Load dataset
df = load_and_preprocess()

# Create plots folder
project_dir = os.path.dirname(os.path.dirname(__file__))
plot_dir = os.path.join(project_dir, "static", "plots")

os.makedirs(plot_dir, exist_ok=True)

# ---------------- Histogram ----------------

plt.figure(figsize=(6,4))
plt.hist(df["G3"], bins=10)
plt.title("Distribution of Final Marks")
plt.xlabel("Final Marks")
plt.ylabel("Number of Students")
plt.tight_layout()

plt.savefig(os.path.join(plot_dir,"histogram.png"))
plt.close()


# ---------------- Pie Chart ----------------

passed = len(df[df["G3"]>=10])
failed = len(df[df["G3"]<10])

plt.figure(figsize=(5,5))
plt.pie(
    [passed, failed],
    labels=["Pass","Fail"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Pass vs Fail")

plt.savefig(os.path.join(plot_dir,"pie.png"))
plt.close()


# ---------------- Heatmap ----------------

plt.figure(figsize=(10,8))

corr = df.corr()

plt.imshow(corr)

plt.xticks(range(len(corr.columns)),corr.columns,rotation=90)

plt.yticks(range(len(corr.columns)),corr.columns)

plt.colorbar()

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(os.path.join(plot_dir,"heatmap.png"))

plt.close()

print("Plots Generated Successfully!")