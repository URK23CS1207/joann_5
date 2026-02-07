import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_visuals(df):
    os.makedirs("reports", exist_ok=True)

    # Histogram
    df.hist(figsize=(8,6))
    plt.tight_layout()
    plt.savefig("reports/histograms.png")
    plt.close()

    # Boxplot
    df.select_dtypes(include='number').plot(kind='box')
    plt.tight_layout()
    plt.savefig("reports/boxplot.png")
    plt.close()
