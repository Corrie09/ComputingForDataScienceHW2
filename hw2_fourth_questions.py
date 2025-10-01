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


def avg_death_of_all_countries_confirmed_above_threshold(threshold):
    filtered = covid[covid["Active"] > threshold]
    result = filtered["Deaths"].sum() / filtered["Confirmed"].sum()
    return result


"""print(
    "Average death/confirmed for countries with more than 500 active cases:",
    avg_death_of_all_countries_confirmed_above_threshold(500),
)
print(
    "Average death/confirmed for countries with more than 1000 active cases:",
    avg_death_of_all_countries_confirmed_above_threshold(1000),
)
print(
    "Average death/confirmed for countries with more than 5000 active cases:",
    avg_death_of_all_countries_confirmed_above_threshold(5000),
)
"""

# in the end we need three lists and three values for the average death/confirmed
# for countries with more than 500, 1000 and 5000 active cases respectively


list_of_countries_500 = covid[covid["Active"] > 500]["Country"].unique()
list_of_countries_1000 = covid[covid["Active"] > 1000]["Country"].unique()
list_of_countries_5000 = covid[covid["Active"] > 5000]["Country"].unique()
avg_death_confirmed_500 = avg_death_of_all_countries_confirmed_above_threshold(500)
avg_death_confirmed_1000 = avg_death_of_all_countries_confirmed_above_threshold(1000)
avg_death_confirmed_5000 = avg_death_of_all_countries_confirmed_above_threshold(5000)

print("List of countries with more than 500 active cases:", list_of_countries_500)
print(
    "Average death/confirmed for countries with more than 500 active cases:",
    avg_death_confirmed_500,
)
print("List of countries with more than 1000 active cases:", list_of_countries_1000)
print(
    "Average death/confirmed for countries with more than 1000 active cases:",
    avg_death_confirmed_1000,
)
print("List of countries with more than 5000 active cases:", list_of_countries_5000)
print(
    "Average death/confirmed for countries with more than 5000 active cases:",
    avg_death_confirmed_5000,
)
