import pandas as pd

# Load the CSV file
df = pd.read_csv("D:\Karthikyan\SECRET\Python\lab 7\IOT-temp.csv")

# Display first and last 10 records
print("First 10 records:")
print(df.head(10))
print("\nLast 10 records:")
print(df.tail(10))

# Get shape, index, and column details
print("Shape of DataFrame:", df.shape)
print("Index of DataFrame:", df.index)
print("Columns in DataFrame:", df.columns)

# Select rows where temperature is greater than 25
selected_rows = df[df['temp'] > 25]
print("\nSelected rows where temperature is greater than 25:")
print(selected_rows)

# Delete rows where temperature is less than 20 (if needed)
df = df[df['temp'] >= 20]

# Delete an unnecessary column example, if exists
if 'unnecessary_column' in df.columns:
    df.drop('unnecessary_column', axis=1, inplace=True)

# Sort DataFrame by temperature
df.sort_values(by='temp', ascending=False, inplace=True)

# Compute basic statistical data
temperature_stats = df['temp'].describe()
print("\nTemperature Statistics:")
print(temperature_stats)

# Find the count and uniqueness of the 'out/in' categorical values
out_in_counts = df['out/in'].value_counts()
unique_out_in = df['out/in'].nunique()
print("\nCount of 'out/in' values:")
print(out_in_counts)
print("Unique count of 'out/in':", unique_out_in)

# Rename columns if necessary
df.rename(columns={'temp': 'temperature'}, inplace=True)
print("\nRenamed columns:")
print(df.columns)
