# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a function to convert HbA1c to average blood glucose level in mg/dl
# Source: https://www.diabetes.co.uk/hba1c-to-blood-sugar-level-converter.html
def hba1c_to_glucose(hba1c):
    return (hba1c * 28.7) - 46.7

# Create a pandas dataframe with HbA1c values from 1.6 to 10.5 with increments of 0.1
hba1c = pd.DataFrame({'HbA1c': [round(x, 1) for x in np.arange(1.6, 10.5, 0.1)]})

# Add a column for average blood glucose level in mg/dl using the function
hba1c['Glucose'] = hba1c['HbA1c'].apply(hba1c_to_glucose)

# Plot the dataframe using matplotlib
plt.figure(figsize=(10, 6))
plt.plot(hba1c['HbA1c'], hba1c['Glucose'], color='black', label='Average blood glucose level')
plt.xlabel('HbA1c (%)')
plt.ylabel('Average blood glucose level (mg/dl)')
plt.title('Estimated average blood glucose levels associated with the spectrum of HbA1c')

# Use fill_between method to plot area under curve below 6.0 in blue and area above curve above 7.0 in red
# Source: https://www.dietvsdisease.org/normal-hba1c-range/
plt.fill_between(hba1c['HbA1c'], hba1c['Glucose'], where=hba1c['Glucose'] <= 90, color='red', alpha=0.2, label='Hypoglycemic range')
plt.fill_between(hba1c['HbA1c'], 90, 130, where=((hba1c['Glucose'] >= 90) & (hba1c['Glucose'] <= 130)), color='green', alpha=0.2, label='Normal range') 
plt.fill_between(hba1c['HbA1c'], hba1c['Glucose'], 250, where=hba1c['Glucose'] >= 130, color='blue', alpha=0.2, label='Hyperglycemic range')

# Add a legend
plt.legend()

# Save the plot
plt.savefig('dog.png')
