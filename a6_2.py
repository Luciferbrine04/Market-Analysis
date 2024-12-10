import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load the Excel file
file_path = 'dataset.xlsx'
excel_data = pd.ExcelFile(file_path)

# Load the data from the specific sheet
data = excel_data.parse('Form Responses 1')

# Text Analysis on Advice
advice = data['What advice would you give to companies that want to improve their sustainability practices?']

# Combine all advice into a single string, dropping any NaN values
combined_advice = ' '.join(advice.dropna().tolist())

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(combined_advice)

# Plot the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Turn off the axis
plt.title('Advice for Sustainability Practices')
plt.show()
