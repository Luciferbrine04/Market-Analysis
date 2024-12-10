import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = 'dataset.xlsx'
excel_data = pd.ExcelFile(file_path)

# Load the data from the specific sheet
data = excel_data.parse('Form Responses 1')

# Belief in Company Responsibility vs. Purchase Frequency
sns.countplot(x='Do you believe companies have a responsibility to be sustainable?', 
              hue='Have you purchased a product from a company known for its sustainability practices?', 
              data=data)
plt.title('Company Responsibility vs. Purchase Frequency')
plt.show()
