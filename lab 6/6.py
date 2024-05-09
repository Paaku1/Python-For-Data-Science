# # a) DataFrame creation is done in step 1
import pandas as pd
import numpy as np

data = {
    'Name': ['Raman']*3 + ['Zuhaire']*3 + ['Aashravy']*3 + ['Mishti']*3,
    'UT': [1, 2, 3]*4,
    'Maths': [22, 21, 14, 20, 23, 22, 23, 24, 12, 15, 18, 17],
    'Science': [21, 20, 19, 17, 15, 18, 19, 22, 25, 22, 21, 18],
    'S.St.': [18, 17, 15, 22, 21, 19, 20, 24, 19, 25, 25, 20],
    'Hindi': [20, 22, 24, 24, 25, 23, 15, 17, 21, 22, 24, 25],
    'Eng': [21, 24, 23, 19, 15, 13, 22, 21, 23, 22, 23, 20]
}

marksUT = pd.DataFrame(data)


# # b) Maximum values for each column
# max_values = marksUT.max()

# # c) Minimum values for each column
# min_values = marksUT.min()

# # d) Sum of values for each column
# sum_values = marksUT.sum()

# # e) Total number of values for each column
# count_values = marksUT.count()

# # f) Mean of each column
# mean_values = marksUT.mean()

# # g) Median of each column
# median_values = marksUT.median()

# # h) Mode of each column
# mode_values = marksUT.mode()

# # i) Quartiles of each column
# quartile_values = marksUT.quantile([0.25, 0.5, 0.75])

# # j) Variance of each column
# variance_values = marksUT.var()

# # k) Standard Deviation of each column
# std_dev_values = marksUT.std()

# # l) Aggregated functions
# aggregated_values = marksUT.agg(['max', 'min', 'sum', 'count', 'std', 'var'])

# # m) Sort by name in ascending order
# sorted_by_name = marksUT.sort_values(by='Name')

# # n) Sort by each subject and display (example for Maths)
# sorted_by_maths = marksUT.sort_values(by='Maths')

# # o) Group by name of student
# grouped_by_name = marksUT.groupby('Name').mean()

# # p) Group by name and UT
# grouped_by_name_ut = marksUT.groupby(['Name', 'UT']).mean()

# # q) Average marks by all students in each subject for each UT
# average_marks_ut = marksUT.groupby('UT').mean()

# # r) Average marks in Maths for each UT
# average_maths_ut = marksUT.groupby('UT')['Maths'].mean()



# Assuming marksUT DataFrame is defined as previously described

# Calculate statistics only for numeric columns
numeric_cols = marksUT.select_dtypes(include=[np.number])   # Use pd.np.number to specify numeric types

# Calculate maximum values for each numeric column
max_values = numeric_cols.max()

# Calculate minimum values for each numeric column
min_values = numeric_cols.min()

# Calculate the sum of values for each numeric column
sum_values = numeric_cols.sum()

# Calculate the mean of values for each numeric column
mean_values = numeric_cols.mean()

# Calculate the median of values for each numeric column
median_values = numeric_cols.median()

# Calculate the mode of values for each numeric column
mode_values = numeric_cols.mode()

# Calculate the quartiles
quartile_values = numeric_cols.quantile([0.25, 0.5, 0.75])

# Calculate variance
variance_values = numeric_cols.var()

# Calculate standard deviation
std_dev_values = numeric_cols.std()

# Aggregate functions applied to numeric columns only
aggregated_values = numeric_cols.agg(['max', 'min', 'sum', 'count', 'std', 'var'])

# Output example
print("Maximum values:\n", max_values)
print("Minimum values:\n", min_values)
print("Sum of values:\n", sum_values)
print("Mean values:\n", mean_values)

