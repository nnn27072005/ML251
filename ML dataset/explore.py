import pandas as pd
import matplotlib.pyplot as plt
import os

# Đọc file
df = pd.read_csv("fetal_health.csv")

# Tạo thư mục images nếu chưa có
os.makedirs("images", exist_ok=True)

# Nhóm 1: signal-based features
signal_cols = [
    "baseline value",
    "accelerations",
    "fetal_movement",
    "uterine_contractions",
    "light_decelerations",
    "severe_decelerations",
    "prolongued_decelerations",
    "abnormal_short_term_variability",
    "mean_value_of_short_term_variability",
    "percentage_of_time_with_abnormal_long_term_variability",
    "mean_value_of_long_term_variability",
    "fetal_health"
]

# Nhóm 2: histogram-based features
hist_cols = [
    "histogram_width",
    "histogram_min",
    "histogram_max",
    "histogram_number_of_peaks",
    "histogram_number_of_zeroes",
    "histogram_mode",
    "histogram_mean",
    "histogram_median",
    "histogram_variance",
    "histogram_tendency"
]

# Hàm vẽ histogram grid cho 1 nhóm
def plot_histograms(df, cols, title, filename):
    n_cols = 4
    n_rows = (len(cols) + n_cols - 1) // n_cols
    plt.figure(figsize=(20, 4*n_rows))
    for i, col in enumerate(cols, 1):
        plt.subplot(n_rows, n_cols, i)
        plt.hist(df[col], bins=30, color="skyblue", edgecolor="black")
        plt.title(col, fontsize=10)
    plt.suptitle(title, fontsize=16, y=1.02)
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close()

# Vẽ và lưu nhóm 1
plot_histograms(df, signal_cols, "Signal-based Features", "images/signal_features_before.png")

# Vẽ và lưu nhóm 2
plot_histograms(df, hist_cols, "Histogram-based Features", "images/histogram_features_before.png")
