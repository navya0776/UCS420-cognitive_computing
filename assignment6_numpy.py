import numpy as np

temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40])
corrected_temperature = temperature + 2
print("Corrected temperatures in Celsius:", corrected_temperature)

fahrenheit = corrected_temperature * 9 / 5 + 32
print("Corrected temperatures in Fahrenheit:", fahrenheit)

above_32 = corrected_temperature[corrected_temperature > 32]
print("Readings greater than 32°C:", above_32)
print("Number of readings greater than 32°C:", np.count_nonzero(corrected_temperature > 32))

steps = np.array([
    [5000, 6200, 7100],
    [8000, 7500, 9000],
    [4500, 5100, 4800],
    [9000, 8500, 9500]
])

print("\nTotal steps:", np.sum(steps))
print("Mean steps:", np.mean(steps))
print("Maximum steps:", np.max(steps))
print("Minimum steps:", np.min(steps))
print("Total steps for each day:", np.sum(steps, axis=0))
print("Total steps for each user:", np.sum(steps, axis=1))
max_position = np.unravel_index(np.argmax(steps), steps.shape)
print("Maximum step count position (user index, day index):", max_position)
print("Maximum step count position (user number, day number):", (max_position[0] + 1, max_position[1] + 1))

original = np.array([1, 2, 3, 4, 5, 6])
subset = original[1:5]
subset[0] = 999
print("\nOriginal after changing subset:", original)
print("Subset:", subset)

copied_subset = original[1:5].copy()
copied_subset[0] = 500
print("\nOriginal after changing copied subset:", original)
print("Copied subset:", copied_subset)

matrix = np.arange(1, 13).reshape(3, 4)
print("\n3 x 4 matrix:\n", matrix)
print("First row:", matrix[0, :])
print("Last row:", matrix[-1, :])
print("Second column:", matrix[:, 1])
print("Rows 1–2 and columns 2–3:", matrix[1:3, 2:4])

flattened = matrix.flatten()
raveled = matrix.ravel()
print("\nFlattened array:", flattened)
print("Raveled array:", raveled)

raveled[0] = 100
print("Matrix after changing ravel result:\n", matrix)
flattened[1] = 200
print("Matrix after changing flatten result:\n", matrix)
print("Flattened array after modification:", flattened)

print("\nMatrix shape:", matrix.shape)
print("Matrix dimensions:", matrix.ndim)
print("Matrix size:", matrix.size)
print("Matrix data type:", matrix.dtype)

X = np.array([
    [6, 70, 3],
    [5, 50, 6],
    [8, 80, 2],
    [4, 30, 8]
])
y = np.array([40, 65, 30, 85])

print("\nShape of X:", X.shape)
print("Dimensions of X:", X.ndim)
print("Transpose of X:\n", X.T)
print("X transpose multiplied by X:\n", X.T @ X)

beta = np.linalg.pinv(X.T @ X) @ X.T @ y
print("OLS coefficients:", beta)
print("Coefficient order: sleep hours, activity level, stress level")

new_user = np.array([5, 40, 7])
predicted_score = new_user @ beta
print("Predicted assistance score for the new user:", predicted_score)
