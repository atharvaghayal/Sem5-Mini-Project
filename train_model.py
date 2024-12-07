# train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Sample data for training (replace with actual data if available)
data = {'amount': [100, 150, 200, 250, 300]}  # Example past expenses
df = pd.DataFrame(data)

# Prepare the training data
X = df.index.values.reshape(-1, 1)  # Days or record index
y = df['amount']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model to a file
joblib.dump(model, 'expense_predictor_model.pkl')
print("Model trained and saved as 'expense_predictor_model.pkl'")
