import pandas as pd
from imblearn.over_sampling import SMOTE

# Đọc file gốc (đúng tên file)
file_path = "fetal_health.csv"
df = pd.read_csv(file_path)

# Thống kê số lượng mẫu theo class trước SMOTE
class_counts_before = df["fetal_health"].value_counts()

# Áp dụng SMOTE để cân bằng
X = df.drop(columns=["fetal_health"])
y = df["fetal_health"]

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Gộp lại thành dataframe mới
df_after = pd.concat(
    [pd.DataFrame(X_resampled, columns=X.columns),
     pd.Series(y_resampled, name="fetal_health")],
    axis=1
)

# Thống kê số lượng mẫu sau SMOTE
class_counts_after = df_after["fetal_health"].value_counts()

# Lưu file mới
output_path = "fetal_health_after.csv"
df_after.to_csv(output_path, index=False)

(class_counts_before, class_counts_after, output_path)
