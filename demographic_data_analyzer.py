import pandas as pd

column_names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 
                'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 
                'hours-per-week', 'native-country', 'salary']


df = pd.read_csv(r'C:\Users\SAM-Tech\Desktop\freecode camp\adult\adult.data', 
                 names=column_names, sep=r'\s*,\s*', engine='python')
print(df.head())



def calculate_race_counts():
    
    return df['race'].value_counts()

def calculate_average_age_men():
   
    return df[df['sex'] == 'Male']['age'].mean()




df_test = pd.read_csv(r'C:\Users\SAM-Tech\Desktop\freecode camp\adult\adult.test', 
                      names=column_names, sep=r'\s*,\s*', engine='python')
print(df_test.head())


race_counts = df['race'].value_counts()
print (race_counts)


average_age_men = df[df['sex'] == 'Male']['age'].mean()
print (average_age_men)


Bachelors_degree_percentage = (df['education'] == 'Bachelors').mean() * 100
print(Bachelors_degree_percentage)


advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
percentage_advanced_education_more_than_50K = (advanced_education['salary'] == '>50K').mean() * 100
print(percentage_advanced_education_more_than_50K)


non_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
percentage_non_advanced_education_more_than_50K = (non_advanced_education['salary'] == '>50K').mean() * 100
print(percentage_non_advanced_education_more_than_50K)


min_hours_per_week = df['hours-per-week'].min()
print(min_hours_per_week)


min_hours_salary_over_50K = df[df['hours-per-week'] == min_hours_per_week]
percentage_min_hours_salary_over_50K = (min_hours_salary_over_50K['salary'] == '>50K').mean()* 100
print(percentage_min_hours_salary_over_50K)


# What country has the highest percentage of people that earn >50K and what is that percentage?
# Ensure that we don't have missing values in 'salary' or 'native-country'

missing_salary = df['salary'].isnull().sum()
missing_native_country = df['native-country'].isnull().sum()

print(f"Missing value in 'salary' : {missing_salary}")
print(f" Missing value in 'native_country' = {missing_native_country}")


if missing_salary > 0 or missing_native_country > 0:
    df = df.dropna(subset=['salary', 'native-country'])
    print("Missing values removed.")
else:
    print("No missing values found.")

country_salary_group = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
country_percentage_over_50K = country_salary_group['>50K'] * 100

highest_percentage_country = country_percentage_over_50K.idxmax()
highest_percentage = country_percentage_over_50K.max()

print(f"The country with the highest percentage of people earning >50K is: {highest_percentage_country}")
print(f"The percentage is: {highest_percentage:.2f}%")



india_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
most_popular_occupation_india = india_earners['occupation'].value_counts().idxmax()
print(most_popular_occupation_india)