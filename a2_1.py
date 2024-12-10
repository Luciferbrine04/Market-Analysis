import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'dataset.xlsx'
excel_data = pd.ExcelFile(file_path)

# Load the data from the specific sheet
data = excel_data.parse('Form Responses 1')

# Handle missing values (dropping rows with NaN in key columns)
data = data.dropna(subset=[
    'Are you willing to pay extra for sustainable products?',
])

# Define income ranges and labels
income_bins = [0, 50000, 100000, 200000, 500000, 1000000]  # Example ranges in your currency
income_labels = ['0-50k', '50k-100k', '100k-200k', '200k-500k', '500k-1M']

# Bin income levels into defined ranges
data['Income Range'] = pd.cut(data['Income level'], bins=income_bins, labels=income_labels)

# Count occurrences of "Yes" and "No" responses for each income range
yes_no_counts = data.groupby(['Income Range', 'Are you willing to pay extra for sustainable products?']).size().unstack(fill_value=0)

# Plot the results as grouped bars
yes_no_counts.plot(kind='bar', figsize=(10, 6), color=['#4CAF50', '#FFC107'])
plt.title('Willingness to Pay Extra by Income Range')
plt.xlabel('Income Range')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title='Willing to Pay Extra', labels=['No', 'Yes'])
plt.show()
