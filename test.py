import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Get the maximum value from the entire DataFrame
max_value = df.max().max()

print("The maximum value in the DataFrame is:", max_value)
