from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
 
# Step 1: Generate dummy classification data
X, y = make_classification(n_samples=100, n_features=4, random_state=42)
 
# Step 2: Split and scale the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
 
# Step 3: Train a logistic regression model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)
print("Model trained successfully.")
# Step 4: Save the model and scaler for later use       
X_test_scaled = scaler.transform(X_test)
y_pred = model.predict(X_test_scaled)
print("Model predictions on test set:", y_pred)





import skl2onnx
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
from logistic import model, X_train
 
# Define the input type and shape
initial_type = [('float_input', FloatTensorType([None, X_train.shape[1]]))]
 
# Convert the trained model to ONNX
onnx_model = convert_sklearn(model, initial_types=initial_type)
 
# Save the model to a file
with open("logistic_model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())
 
print("ONNX model saved as logistic_model.onnx")
