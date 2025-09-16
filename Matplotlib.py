"""Assignment: Data Analysis and Visualization with Pandas and Matplotlib

Objective:
- Load and analyze the Iris dataset
- Perform basic statistical analysis
- Create and customize visualizations
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

def main():
    try:
         # --------------------------
        # Task 1: Load and explore dataset
        # --------------------------

        # Load the iris dataset
        iris = load_iris(as_frame=True)
        df = iris.frame  # Convert to pandas DataFrame

        print("\n--- First 5 Rows ---")
        print(df.head())

        print("\n--- Data Info ---")
        print(df.info())

        print("\n--- Missing Values ---")
        print(df.isnull().sum())

        # Clean dataset: fill missing values if any
        df = df.fillna(df.mean(numeric_only=True))

        # --------------------------
        # Task 2: Basic Data Analysis
        # --------------------------
        print("\n--- Basic Statistics ---")
        print(df.describe())

        # Grouping: average petal length per species
        print("\n--- Average Petal Length by Species ---")
        group_mean = df.groupby("target")["petal length (cm)"].mean()
        print(group_mean)

        # Finding: Differences in petal length among species
        print("\nObservation: Iris-virginica has the highest average petal length.")

        # --------------------------
        # Task 3: Data Visualization
        # --------------------------

        # 1. Line Chart (trend of sepal length for first 50 samples)
        plt.figure(figsize=(8,5))
        plt.plot(df.index[:50], df["sepal length (cm)"][:50], label="Sepal Length")
        plt.title("Sepal Length Trend (First 50 Samples)")
        plt.xlabel("Sample Index")
        plt.ylabel("Sepal Length (cm)")
        plt.legend()
        plt.grid(True)
        plt.show()

        # 2. Bar Chart (average petal length per species)
        plt.figure(figsize=(8,5))
        group_mean.plot(kind="bar", color=["skyblue","orange","green"])
        plt.title("Average Petal Length per Species")
        plt.xlabel("Species (0=setosa, 1=versicolor, 2=virginica)")
        plt.ylabel("Average Petal Length (cm)")
        plt.show()

        # 3. Histogram (distribution of sepal width)
        plt.figure(figsize=(8,5))
        plt.hist(df["sepal width (cm)"], bins=20,
        color="purple", alpha=0.7)
        plt.title("Distribution of Sepal Width")
        plt.xlabel("Sepal Width (cm)")
        plt.ylabel("Frequency")
        plt.show()

        # 4. Scatter Plot (sepal length vs petal length)
        plt.figure(figsize=(8,5))
        sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="target", palette="Set2")
        plt.title("Sepal Length vs Petal Length")
        plt.xlabel("Sepal Length (cm)")
        plt.ylabel("Petal Length (cm)")
        plt.legend(title="Species")
        plt.show()

    except FileNotFoundError:
        print("❌ Error: Dataset file not found.")
    except Exception as e:
        print(f"⚠ An error occurred: {e}")
        
    if _name_ == "_main_":
        main() 
