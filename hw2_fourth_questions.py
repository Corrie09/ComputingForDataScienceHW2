###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
#


import pandas as pd

covid = pd.read_csv("covid.csv")
print(covid.head())


def avg_death_of_all_country_confirmed_above_threshold(threshold):
    filtered = covid[covid["Active"] > threshold]
    result = filtered["Deaths"].sum() / filtered["Confirmed"].sum()
    return result


print(
    "Average death/confirmed for countries with more than 500 active cases:",
    avg_death_of_all_country_confirmed_above_threshold(500),
)
print(
    "Average death/confirmed for countries with more than 1000 active cases:",
    avg_death_of_all_country_confirmed_above_threshold(1000),
)
print(
    "Average death/confirmed for countries with more than 5000 active cases:",
    avg_death_of_all_country_confirmed_above_threshold(5000),
)


# list_of_countries = covid["Country"].unique()
# covid["avg_death_confirmed"] = covid["Deaths"] / covid["Confirmed"]
# print(covid.head())


"""
def avg_death_confirmed_above_threshold(threshold):
    filtered = covid[covid["Active"] > threshold]
    result = filtered.groupby("Country")["avg_death_confirmed"].mean()
    return result


print("Countries with more than 500 active cases:")
print(avg_death_confirmed_above_threshold(500))
print("Countries with more than 1000 active cases:")
print(avg_death_confirmed_above_threshold(1000))
print("Countries with more than 5000 active cases:")
print(avg_death_confirmed_above_threshold(5000))
"""
