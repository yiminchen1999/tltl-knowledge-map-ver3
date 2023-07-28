import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Path to the folder containing the text files
folder_path = 'assets/Y2023/Y2023_Student_01.csv'

# Read text data from files in the folder
data = []
for filename in os.listdir(folder_path):
    with open(os.path.join(folder_path, filename), 'r') as file:
        text = file.read()
        data.append(text)

# Convert data to numerical values (if applicable)
numeric_data = pd.to_numeric(data, errors='coerce')

# Create a DataFrame from the numeric data
heatmap_data = pd.DataFrame({'Data': numeric_data})

# Check if the DataFrame contains valid numeric values
if heatmap_data['Data'].notnull().any():
    # Create a heatmap using seaborn
    sns.heatmap(heatmap_data)

    # Display the heatmap
    plt.show()
else:
    print("No valid numeric data found.")

