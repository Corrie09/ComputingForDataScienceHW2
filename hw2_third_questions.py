# Now imagine you have a certain data structure that
# contains information about different countries and
# the number of people who was registered with covid
# in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
#       'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the
# number of registered cases is not the same (thus
# the length of the lists can differ)


# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country

"""def total_registered_cases(data : dict, country: str):
if country in data:
    return sum(data[country])
else :
    return 'Country not found'
"""


# this does the same as above, but is more "pythonic" as it uses
# the get method of dictionaries, which allows to specify
# a default value if the key is not found and avoids breaking when
# the key is not present
def total_registered_cases(data: dict, country: str) -> int:
    # Sum the list if present; otherwise sum([]) = 0
    return sum(
        data.get(country, [])
    )  # If the key exists → return its value, if the key doesn’t exist → return the default.


# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
#
def total_registered_cases_per_country(data: dict):
    result = {}
    for country in data:
        result[country] = total_registered_cases(data, country)
    return result


# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases
def country_with_most_cases(data: dict):
    totals = total_registered_cases_per_country(data)
    if not totals:
        return None
        # return 'No data available' #this is another option, but None is safer
    return max(totals, key=totals.get)
