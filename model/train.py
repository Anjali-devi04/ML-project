import os
import joblib
from sklearn.linear_model import LinearRegression
from preprocess import load_and_preprocess

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load processed data
df = load_and_preprocess()
# Inputs(X)
X = df.drop("G3", axis=1)
# Target (y)
y = df["G3"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Create model
model = LinearRegression()
# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
# Evaluation
print(f"R² Score : {r2_score(y_test, y_pred):.3f}")
print(f"MAE      : {mean_absolute_error(y_test, y_pred):.3f}")
print(f"MSE      : {mean_squared_error(y_test, y_pred):.3f}")


# Save model
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "student_marks_model.pkl")
joblib.dump(model, model_path)
print("\nModel saved successfully")