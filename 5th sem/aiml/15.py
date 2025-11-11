import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = {
    "Feature1": [1,2,3,8,9,10, 2,3,4, 8,9,11],
    "Feature2": [2,3,4,9,9,11, 1,2,3, 7,8,10],
    "Class":    [0,0,0,1,1,1, 0,0,0, 2,2,2]
}

df = pd.DataFrame(data)

X = df[["Feature1", "Feature2"]]
y = df["Class"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("Explained Variance Ratio:", pca.explained_variance_ratio_)
print("PCA Components:\n", pca.components_)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', s=80)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA Result (Own Dataset)")
plt.colorbar(label="Class")
plt.grid(True)
plt.show()
