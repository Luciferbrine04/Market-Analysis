import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = 'dataset.xlsx'
excel_data = pd.ExcelFile(file_path)

# Load the data from the specific sheet
data = excel_data.parse('Form Responses 1')

# Gender vs. Responsibility Beliefs
sns.countplot(x='Gender', hue='Do you believe companies have a responsibility to be sustainable?', data=data)
plt.title('Gender vs. Company Responsibility Beliefs')
plt.show()
