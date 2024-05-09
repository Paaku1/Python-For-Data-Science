import numpy as np

temperatures = np.array([4.0, 5.5, 9.0, 12.0, 16.5, 20.0, 22.5, 22.0, 19.0, 14.0, 9.5, 5.0])

mean_temperature = np.mean(temperatures)
print(f"Mean Temperature: {mean_temperature:.2f}°C")

median_temperature = np.median(temperatures)
print(f"Median Temperature: {median_temperature:.2f}°C")

std_deviation = np.std(temperatures)
print(f"Standard Deviation: {std_deviation:.2f}")

hottest_month_index = np.argmax(temperatures) + 1
coldest_month_index = np.argmin(temperatures) + 1
hottest_temperature = temperatures[hottest_month_index - 1]
coldest_temperature = temperatures[coldest_month_index - 1]

print(f"Hottest Month: Month {hottest_month_index} with {hottest_temperature}°C")
print(f"Coldest Month: Month {coldest_month_index} with {coldest_temperature}°C")
