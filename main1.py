import pandas as pd
from demographic_data_analyzer import demographic_data_analyzer

# Assuming you have loaded the data into a DataFrame
data = pd.read_csv('your_data.csv')

results = demographic_data_analyzer(data)

# Print the results or use them as needed
print(results['race_counts'])
print(results['average_age_men'])
