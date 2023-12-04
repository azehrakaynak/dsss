
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('census_income_dataset.csv')
# Convert column names to lowercase
df.columns = df.columns.str.lower()

# use lowercase column names in the code
sns.histplot(df['age'], bins=20, kde=False, color='skyblue', edgecolor='black')

# Plot 1: Age distribution of respondents (Histogram)
plt.figure(figsize=(10, 6))
sns.histplot(df['age'], bins=20, kde=False, color='skyblue', edgecolor='black')
plt.title('Age Distribution of Respondents', fontsize=16)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.show()

# Plot 2: Relationship status distribution (Bar plot)
plt.figure(figsize=(10, 6))
sns.countplot(x='relationship', data=df, palette='viridis')
plt.title('Distribution of Relationship Status', fontsize=16)
plt.xlabel('Relationship Status', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.show()

# Plot 3: Salary distribution within each educational level (Bar plot)
plt.figure(figsize=(12, 8))
sns.countplot(x='education', hue='salary', data=df, palette='Set1')
plt.title('Salary Distribution within Each Educational Level', fontsize=16)
plt.xlabel('Educational Level', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.legend(title='Salary', labels=['<=50k', '>50k'])
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('census_income_dataset.csv')

# Plot the age distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['AGE'], bins=20, kde=False, color='skyblue', edgecolor='black')
plt.title('Age Distribution of Respondents', fontsize=16)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Count', fontsize=14)

# Save the plot as SVG
plt.savefig('age_distribution.svg', format='svg')

# Show the plot
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('census_income_dataset.csv')

# Plot 2: Relationship status distribution
plt.figure(figsize=(10, 6))
sns.countplot(x='RELATIONSHIP', data=df, palette='viridis')
plt.title('Distribution of Relationship Status', fontsize=16)
plt.xlabel('Relationship Status', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility

# Save the plot as SVG
plt.savefig('relationship_distribution.svg', format='svg')

# Show the plot
plt.show()

# Plot 3: Salary distribution within each educational level
plt.figure(figsize=(12, 8))
sns.countplot(x='EDUCATION', hue='SALARY', data=df, palette='Set1')
plt.title('Salary Distribution within Each Educational Level', fontsize=16)
plt.xlabel('Educational Level', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.legend(title='Salary', labels=['<=50k', '>50k'])

# Save the plot as SVG
plt.savefig('salary_education_distribution.svg', format='svg')

# Show the plot
plt.show()


