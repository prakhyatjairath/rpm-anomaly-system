import random
import joblib
from sklearn.ensemble import IsolationForest

print("Starting the Lab Environment...")

# 1. Generate the historical training data
training_data = [[random.randint(900, 1200)] for _ in range(500)]
training_data.extend([[0], [2000], [100], [1800]]) # Add anomalies

# 2. Initialize and train the model
model = IsolationForest(contamination=0.05, random_state=42)
print("Training model...")
model.fit(training_data)

# 3. Export the "Brain" to a file
joblib.dump(model, "anomaly_model.pkl")
print("Success! Model saved to 'anomaly_model.pkl'")