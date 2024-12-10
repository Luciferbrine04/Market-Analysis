import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = 'dataset.xlsx'
excel_data = pd.ExcelFile(file_path)

# Load the data from the specific sheet
data = excel_data.parse('Form Responses 1')

# Handle missing values (dropping rows with NaN in key columns)
data = data.dropna(subset=[
    'How important is sustainability to you personally?',
])
# Age vs. Importance of Sustainability
sns.boxplot(x='Age', y='How important is sustainability to you personally?', data=data)
plt.title('Age vs. Importance of Sustainability')
plt.show()
