import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = 'dataset.xlsx'
excel_data = pd.ExcelFile(file_path)

# Load the data from the specific sheet
data = excel_data.parse('Form Responses 1')

# Awareness vs. Willingness to Pay
data['Willingness to Pay'] = data['If yes, how much more would you be willing to pay?'].str.extract('(\d+)').astype(float)
plt.figure(figsize=(10, 6))
sns.violinplot(x='How aware are you of the environmental impact of different products?', 
               y='Willingness to Pay', 
               data=data, inner='quartile')
plt.title('Violin Plot of Willingness to Pay by Awareness Level')
plt.xlabel('Awareness Level')
plt.ylabel('Willingness to Pay')
plt.xticks(rotation=45)
plt.show()
