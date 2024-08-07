########################################
## Data Analysis Project with Python ##
########################################

# We will use these three Python packages during this project

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Import the job postings dataset
postings = pd.read_csv("C:/Users/Admin/Desktop/BDEEM/Sem2/Introduction to Python/Python Project/job_postings_linkedin_dataset.csv")
print(postings)

# Data Cleaning
# Renaming some of the variables
postings = postings.rename(columns={'job_link': 'job_url', 'job level': 'job_level'})

# Group by 'job_title', count occurrences, and filter counts greater than 100
filtered_postings = postings.groupby('job_title').size().reset_index(name='counts')
filtered_postings = filtered_postings[filtered_postings['counts'] > 100]

# Sort data for better visualization
filtered_postings = filtered_postings.sort_values('counts', ascending=False)

# Plot 1 - Bar chart showing the most common job titles
plt.figure(figsize=(10, 8))
sns.barplot(x='counts', y='job_title', data=filtered_postings, palette='viridis')
plt.title('Top Data Engineering Jobs')
plt.xlabel('Number of Postings')
plt.ylabel('Job Titles')
plt.xticks(rotation=45)
plt.show()


# Plot 2 - Showing countries with the most data engineering job postings
# Group by 'search_country', count occurrences, and reset index to make 'search_country' a column again
country_counts = postings.groupby('search_country').size().reset_index(name='counts')

# Sort data by 'counts' for better visualization
country_counts = country_counts.sort_values('counts', ascending=True)

plt.figure(figsize=(10, 8))
plt.barh(country_counts['search_country'], country_counts['counts'], color='turquoise')
plt.title('Geographical Distribution of Data Engineering Job Opportunities')
plt.xlabel('Number of Postings')
plt.ylabel('Countries')
plt.show()


# Data Cleaning
# The 'job_skills' variable is a string of comma-separated values, and it has to be converted to a list
postings['job_skills'] = postings['job_skills'].str.split(',')

# To expand the 'job_skills' lists into separate rows
expanded_postings = postings.explode('job_skills')


# Plot 3 - Top skills for data engineeering postions
# Count the occurrences of each skill and filter by a threshold
skill_counts = expanded_postings['job_skills'].value_counts().reset_index()
skill_counts.columns = ['job_skills', 'counts']  

# Filter skills with counts greater than 1000
filtered_skills = skill_counts[skill_counts['counts'] > 1000]

# Sort data for better visualization (important for horizontal bar plot readability)
filtered_skills = filtered_skills.sort_values('counts', ascending=True)

# Plotting
plt.figure(figsize=(10, 8))
plt.barh(filtered_skills['job_skills'], filtered_skills['counts'], color='orange')
plt.title('Most In-Demand Skills for Data Engineering Positions')
plt.xlabel('Number of Times Listed')
plt.ylabel('Skills')
plt.show()


# Plot 4 - Compares in demand skills across countries
# Group by 'search_country' and 'job_skills', count occurrences, and reset index
country_skill_counts = expanded_postings.groupby(['search_country', 'job_skills']).size().reset_index(name='counts')

# Filter out skills with counts less than 415 to limit the amount of data displayed
filtered_skills = country_skill_counts[country_skill_counts['counts'] > 415]

# Sort data for better visualization
filtered_skills = filtered_skills.sort_values(['search_country', 'counts'], ascending=[True, False])
print(filtered_skills)

# Plotting
plt.figure(figsize=(14, 10))
sns.barplot(x='counts', y='job_skills', hue='search_country', data=filtered_skills, palette='viridis')
plt.title('Top Demanded Skills by Country')
plt.xlabel('Number of Times Listed')
plt.ylabel('Skills')
plt.legend(title='Country', loc='upper right')
plt.show()
