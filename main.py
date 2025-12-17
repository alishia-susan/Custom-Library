import numpy as np

from preprocessing.MinMaxScaler import MinMaxScaler
from preprocessing.StandardScaler import StandardScaler

from metrics.accuracy_score import accuracy_score
from metrics.mean_squared_error import mean_squared_error
from metrics.mean_absolute_error import mean_absolute_error
from metrics.mean_absolute_percentage_error import mean_absolute_percentage_error


# ---------------- Preprocessing ----------------
data = np.array([[1], [2], [3], [4], [5]])

z = MinMaxScaler(data)
y = StandardScaler(data)

print("MinMax Scaled Data:")
print(z)

print("\nStandard Scaled Data:")
print(y)


# ---------------- Metrics ----------------
# IMPORTANT: y_true must NOT contain 0 for MAPE
y_true = np.array([1, 2, 3, 4, 5])
y_pred = np.array([1, 2, 2, 4, 5])

print("\nAccuracy:", accuracy_score(y_true, y_pred))
print("Mean Squared Error:", mean_squared_error(y_true, y_pred))
print("Mean Absolute Error:", mean_absolute_error(y_true, y_pred))
print("Mean Absolute Percentage Error:", mean_absolute_percentage_error(y_true, y_pred))
