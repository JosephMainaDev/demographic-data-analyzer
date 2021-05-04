import pandas as pd

def calculate_demographic_data(print_data=True):
    """
    Using pandas to analyse demographic data.

    The demographic data was extracted from the 1994 Census database and saved in a CSV file.
    All floats are rounded to the nearest tenth.
    """
    # Read adult data from the csv file into a pandas DataFrame object
    df = pd.read_csv("adult.data.csv")

    # Q1 : How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    # Select the "race" column and count the values, return a pandas series.
    # df["race"] == df.race
    # df.value_counts(subset=["race"]) will also work.
    race_count = df.value_counts(df["race"])

    # Q2 : What is the average age of men?
    # Select "sex" column with value of "Male", and return mean() of "age" column
    average_age_men = round(df.loc[df["sex"] == "Male", "age"].mean(), 1)

    # Q3 : What is the percentage of people who have a Bachelor's degree?
    # bachelors = df.value_counts(df["education"] == "Bachelors", normalize=True)
    # percentage_bachelors = bachelors[True] * 100
    percentage_bachelors = round(len(df.loc[df["education"] == "Bachelors"]) * 100 / len(df), 1)

    # Q4 : What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # Pick out people with advanced "education", and get the "salary" column.
    higher_education = df[
        (df["education"] == "Bachelors") |
        (df["education"] == "Masters") |
        (df["education"] == "Doctorate")
    ]["salary"]
    # Count people with `Bachelors`, `Masters`, or `Doctorate` and make >50K.
    over_50k = higher_education.value_counts()[">50K"]
    # Percentage of people with advanced education and make >50K
    higher_education_rich = round(over_50k * 100 / len(higher_education), 1)

    # Q5 : What percentage of people without advanced education make more than 50K?
    # All people who make >50K
    total_over_50k = df["salary"].value_counts()[">50K"]

    # People without `Bachelors`, `Masters`, or `Doctorate` and make >50K
    lower_education = total_over_50k - over_50k

    # Percentage of people without advanced education and make >50K
    lower_education_rich = round(lower_education * 100 / (len(df) - len(higher_education)), 1)

    # Q6 : What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = None

    # Q7 : What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    rich_percentage = None

    # Q8 : What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Q9 : Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
