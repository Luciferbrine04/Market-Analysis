import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textwrap import wrap
from collections import Counter

# Load the Excel file
file_path = 'dataset.xlsx'
excel_data = pd.ExcelFile(file_path)

# Load the data from the specific sheet
data = excel_data.parse('Form Responses 1')

# Handle missing values (dropping rows with NaN in key columns)
data = data.dropna(subset=[
    'Are you willing to pay extra for sustainable products?',
    'How important is sustainability to you personally?',
    'What type of sustainability practices would make you more likely to purchase from a company?',
])

# Extract and split the factors, then flatten into a single list
factors_series = data['What factors influence your decision to purchase a product?'].dropna()
factors_list = [factor.strip() for sublist in factors_series.str.split(',') for factor in sublist]

# Count the frequency of each unique factor
factors_count = Counter(factors_list)

# Convert to a DataFrame for plotting
factors_df = pd.DataFrame(factors_count.items(), columns=['Factor', 'Count']).sort_values(by='Count', ascending=False)

# Wrap long text labels for readability
wrapped_labels = ['\n'.join(wrap(label, 20)) for label in factors_df['Factor']]

# Create the plot with modified settings
plt.figure(figsize=(16, 8))
sns.barplot(x=wrapped_labels, y=factors_df['Count'], palette='viridis')
plt.title('Factors Influencing Purchase Decisions')
plt.xlabel('Factors')
plt.ylabel('Count')
plt.xticks(rotation=30, ha='right')  # Rotate labels by 30 degrees and align them to the right
plt.tight_layout()  # Ensure layout fits well
plt.show()
