import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
# from sklearn_extra.cluster import KMedoids
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

# Load data
data = pd.read_csv('D:\Karthikyan\SECRET\Python\lab 10\OnlineRetail - OnlineRetail.csv')

# Select relevant columns and drop missing values
data = data[['Quantity', 'UnitPrice', 'CustomerID']]
data.dropna(inplace=True)

# Convert data types
data['CustomerID'] = data['CustomerID'].astype(str)

# Aggregate data by CustomerID to create features like total spent and total items purchased
data['TotalSpent'] = data['Quantity'] * data['UnitPrice']
customer_data = data.groupby('CustomerID').agg(TotalSpent=('TotalSpent', 'sum'),
                                               AverageUnitPrice=('UnitPrice', 'mean'),
                                               TotalItems=('Quantity', 'sum')).reset_index()

# Filter out extreme outliers for more meaningful clusters
customer_data = customer_data[(customer_data['TotalSpent'] < customer_data['TotalSpent'].quantile(0.95)) &
                              (customer_data['TotalItems'] < customer_data['TotalItems'].quantile(0.95))]

# Normalize the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(customer_data[['TotalSpent', 'AverageUnitPrice', 'TotalItems']])

# Apply K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
customer_data['KMeans_Cluster'] = kmeans.fit_predict(scaled_features)

# Apply K-Medoids Clustering
# kmedoids = KMedoids(n_clusters=3, random_state=42)
# customer_data['KMedoids_Cluster'] = kmedoids.fit_predict(scaled_features)

# Apply Hierarchical Clustering
linked = linkage(scaled_features, method='ward')
customer_data['Hierarchical_Cluster'] = fcluster(linked, t=3, criterion='maxclust')

# Display clusters
print(customer_data[['CustomerID', 'KMeans_Cluster', 'KMedoids_Cluster', 'Hierarchical_Cluster']].head())

# Optionally, save the output to a CSV file
customer_data.to_csv('D:\Karthikyan\SECRET\Python\lab 10\output.csv', index=False)
