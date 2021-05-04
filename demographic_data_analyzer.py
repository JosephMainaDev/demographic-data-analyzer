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
    min_work_hours = df["hours-per-week"].min()

    # Q7 : What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    # Pick workers who work minimum number of hours, take the "salary" column
    min_workers = df.loc[df["hours-per-week"] == min_work_hours, "salary"]
    num_min_workers = min_workers.count()
    # Percentage of the people who work the minimum number of hours per week and make >50K.
    rich_percentage = round(min_workers.value_counts()[">50K"] * 100 / num_min_workers, 1)

    # Q8 : What country has the highest percentage of people that earn >50K?
    country_over50k = df
    highest_earning_country = None

    # Q9 : What is the highest percentage of rich people in the country?
    highest_earning_country_percentage = None

    # Q10 : Identify the most popular occupation for those who earn >50K in India.
    # Pick people who work in India, getting their "occupation" and "salary".
    indians = df.loc[df["native-country"] == "India", ["occupation", "salary"]]
    # Get "occupation" of Indians who make >50K
    over50k_indians = indians.loc[indians["salary"] == ">50K", "occupation"]
    top_IN_occupation = over50k_indians.value_counts().idxmax()

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
