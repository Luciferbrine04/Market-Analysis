import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

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
# Text Analysis on Challenges
challenges = data['What are the biggest challenges companies face in becoming more sustainable?']

# Combine all challenges into a single string
text = ' '.join(challenges.dropna().tolist())

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Plot the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Turn off the axis
plt.title('Challenges in Sustainability')
plt.show()
