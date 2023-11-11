import numpy as np
import pandas as pd

# Data
# Read .csv with pandas
csv_file_path = 'data/raw/global_people_distribution.csv'
# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path, sep=',')

# Create a boxplot for a specific column, for example, 'total_count'
boxplot_dict = plt.boxplot(df['total_count'])

# Extract the lower quartile (Q1) value
q1_value = boxplot_dict['boxes'][0].get_ydata()[1]

# Create two DataFrames based on the conditions
df_lower_q1 = df[df['total_count'] <= q1_value]
df_higher_q1 = df[df['total_count'] > q1_value]

