import matplotlib.pyplot as plt
import pandas as pd

# Function to plot scatter plot from CSV data
def plot_csv_scatter(file_path):
    # Load data from CSV
    data = pd.read_csv(file_path, header=None, names=['x', 'y', 'class'])

    # Define a color map for classes
    color_map = {1: 'green', 2: 'blue', 3: 'red'}

    # Plot each class with its corresponding color
    plt.figure(figsize=(8, 8))
    for class_label, group in data.groupby('class'):
        plt.scatter(group['x'], group['y'], label=f'Class {class_label}', color=color_map.get(class_label, 'black'))

    # Add plot details
    plt.title('Scatter Plot from CSV Data', fontsize=16)
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
plot_csv_scatter('data-vis/data/other_data.csv')