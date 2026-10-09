import numpy as np

values = np.array([10, 20, 30, 40, 50])
print("Original 1D array:", values)
print("Each element plus 2:", values + 2)
print("Each element multiplied by 3:", values * 3)
print("Each element divided by 2:", values / 2)

arr = np.array([1, 2, 3, 6, 4, 5])
print("\nReversed array:", arr[::-1])

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
x_values, x_counts = np.unique(x, return_counts=True)
x_max_count = x_counts.max()
x_frequent = x_values[x_counts == x_max_count]
print("\nMost frequent value(s) in x:", x_frequent)
for value in x_frequent:
    print(f"Indices of {value} in x:", np.where(x == value)[0])

y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])
y_values, y_counts = np.unique(y, return_counts=True)
y_max_count = y_counts.max()
y_frequent = y_values[y_counts == y_max_count]
print("\nMost frequent value(s) in y:", y_frequent)
for value in y_frequent:
    print(f"Indices of {value} in y:", np.where(y == value)[0])

matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("\n1st row, 2nd column:", matrix[0, 1])
print("3rd row, 1st column:", matrix[2, 0])

your_name = input("\nEnter your name for the array variable label: ").strip().replace(" ", "_")
if not your_name:
    your_name = "student"
name_array = np.linspace(10, 100, 25)
print(f"\nArray for {your_name}:", name_array)
print("Dimensions:", name_array.ndim)
print("Shape:", name_array.shape)
print("Total elements:", name_array.size)
print("Data type:", name_array.dtype)
print("Bytes consumed:", name_array.nbytes)
print("Reshaped transpose-like column array:\n", name_array.reshape(25, 1))
print("Can T be used for the same result on a 1D array?", name_array.T.shape == name_array.shape)

ucs420_name = f"ucs420_{your_name}"
ucs420_array = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 15, 20, 35]])
print(f"\n{ucs420_name}:\n", ucs420_array)
print("Mean:", np.mean(ucs420_array))
print("Median:", np.median(ucs420_array))
print("Maximum:", np.max(ucs420_array))
print("Minimum:", np.min(ucs420_array))
print("Unique elements:", np.unique(ucs420_array))

reshaped_ucs420 = ucs420_array.reshape(4, 3)
print("\nReshaped array (4 rows, 3 columns):\n", reshaped_ucs420)

resized_ucs420 = np.resize(ucs420_array, (2, 3))
print("\nResized array (2 rows, 3 columns):\n", resized_ucs420)
