import pandas as pd

def demographic_data_analyzer(data):
    # 1. How many people of each race are represented in this dataset?
    race_counts = data['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = data[data['sex'] == 'Male']['age'].mean()

    # 3. What is the percentage of people who have a Bachelor's degree?
    bachelors_percentage = (data[data['education'] == 'Bachelors'].shape[0] / data.shape[0]) * 100

    # 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    advanced_education_high_salary_percentage = (data[(data['education'].isin(advanced_education)) & (data['salary'] == '>50K')].shape[0] / data[data['education'].isin(advanced_education)].shape[0]) * 100

    # 5. What percentage of people without advanced education make more than 50K?
    non_advanced_education = data[~data['education'].isin(advanced_education)]
    non_advanced_education_high_salary_percentage = (non_advanced_education[non_advanced_education['salary'] == '>50K'].shape[0] / non_advanced_education.shape[0]) * 100

    # 6. What is the minimum number of hours a person works per week?
    min_hours_per_week = data['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_hours_high_salary_percentage = (data[(data['hours-per-week'] == min_hours_per_week) & (data['salary'] == '>50K')].shape[0] / data[data['hours-per-week'] == min_hours_per_week].shape[0]) * 100

    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    country_salary_percentage = data.groupby('native-country').apply(lambda x: (x[x['salary'] == '>50K'].shape[0] / x.shape[0]) * 100)
    highest_salary_country = country_salary_percentage.idxmax()
    highest_salary_percentage = country_salary_percentage.max()

    # 9. Identify the most popular occupation for those who earn >50K in India.
    india_high_salary = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]
    most_popular_occupation_india = india_high_salary['occupation'].mode()[0]

    # Returning all the calculated results as a dictionary
    return {
        'race_counts': race_counts,
        'average_age_men': average_age_men,
        'bachelors_percentage': bachelors_percentage,
        'advanced_education_high_salary_percentage': advanced_education_high_salary_percentage,
        'non_advanced_education_high_salary_percentage': non_advanced_education_high_salary_percentage,
        'min_hours_per_week': min_hours_per_week,
        'min_hours_high_salary_percentage': min_hours_high_salary_percentage,
        'highest_salary_country': highest_salary_country,
        'highest_salary_percentage': highest_salary_percentage,
        'most_popular_occupation_india': most_popular_occupation_india
    }
