import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Global Settings
sns.set_theme(style="whitegrid")  # Default Seaborn theme
plt.rcParams["figure.figsize"] = (10, 8)  # Default figure size
plt.rcParams["font.size"] = 12  # Default font size for readability
plt.rcParams["axes.titlesize"] = 16  # Title font size
plt.rcParams["axes.labelsize"] = 14  # Axis label font size
plt.rcParams["xtick.labelsize"] = 10  # X-tick label size
plt.rcParams["ytick.labelsize"] = 10  # Y-tick label size

# Load the Excel file
file_path = 'dataset.xlsx'
excel_data = pd.ExcelFile(file_path)

# Load the data from the specific sheet
data = excel_data.parse('Form Responses 1')

# Create a pivot table for the heatmap
heatmap_data = data.pivot_table(index='What sources do you rely on for information about sustainability?', 
                                columns='How aware are you of the environmental impact of different products?', 
                                aggfunc='size', fill_value=0)

# Plot the heatmap with global configurations
plt.figure(figsize=(10, 8))  # Set figure size
sns.heatmap(heatmap_data, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Heatmap of Information Sources vs. Awareness Levels')
plt.xlabel('Awareness Level')
plt.ylabel('Sources of Information')

# Adjust layout to shift left
plt.gcf().subplots_adjust(left=0.42)

plt.show()
