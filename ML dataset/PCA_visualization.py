import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os

# Tạo thư mục lưu nếu chưa có
os.makedirs("images", exist_ok=True)

# Đọc dữ liệu
df_before = pd.read_csv("fetal_health.csv")
df_after = pd.read_csv("fetal_health_after.csv")

# Loại bỏ cột nhãn nếu có
features = [col for col in df_before.columns if col != "fetal_health"]
X_before = df_before[features].dropna()
X_after = df_after[features].dropna()

# Standardize dữ liệu dựa trên dữ liệu gốc
scaler = StandardScaler()
X_before_scaled = scaler.fit_transform(X_before)
X_after_scaled = scaler.transform(X_after)

# PCA 2D cho cả dữ liệu
pca = PCA(n_components=2)
X_combined = pd.concat([pd.DataFrame(X_before_scaled), pd.DataFrame(X_after_scaled)], ignore_index=True)
X_pca = pca.fit_transform(X_combined)

# Tách lại
X_pca_before = X_pca[:len(X_before_scaled)]
X_pca_after = X_pca[len(X_before_scaled):]

# Vẽ 2 plot cạnh nhau
fig, axes = plt.subplots(1, 2, figsize=(14,6))

# Plot dữ liệu gốc
axes[0].scatter(X_pca_before[:,0], X_pca_before[:,1], alpha=0.6, color='blue', label='Original')
axes[0].set_title('Original Data')
axes[0].set_xlabel('PC1')
axes[0].set_ylabel('PC2')
axes[0].grid(True)
axes[0].legend()

# Plot dữ liệu SMOTE
axes[1].scatter(X_pca_after[:,0], X_pca_after[:,1], alpha=0.3, color='red', label='SMOTE')
axes[1].set_title('SMOTE Data')
axes[1].set_xlabel('PC1')
axes[1].set_ylabel('PC2')
axes[1].grid(True)
axes[1].legend()

plt.suptitle('PCA Scatter Plot: Original vs SMOTE', fontsize=16)

# Lưu ra file
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("images/pca_scatter_original_vs_smote.png", dpi=300)
plt.show()
