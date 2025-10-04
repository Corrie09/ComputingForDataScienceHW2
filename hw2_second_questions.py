#
# 4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.

cvs = [
    {"user": "john", "jobs": ["analyst", "engineer"]},
    {"user": "jane", "jobs": ["finance", "software"]},
    {"user": "jane", "jobs": ["finance", "cashier"]},
]


def has_experience_as(cvs, job_title):
    l = []
    for cv in cvs:
        if job_title in cv["jobs"]:
            l.append(cv["user"])
    return l


print(has_experience_as(cvs, "analyst"))  # ['john']
print(has_experience_as(cvs, "finance"))  # ['jane', 'jane']
print(has_experience_as(cvs, "doctor"))  # []
#
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.


def job_counts(cvs):
    d = {}
    for cv in cvs:
        for job in cv["jobs"]:
            try:
                d[job] += 1
            except KeyError:
                d[job] = 1
    return d


#
# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.


def most_popular_job(cvs):
    counts = job_counts(cvs)
    max_title = max(counts, key=counts.get)
    return (max_title, counts[max_title])
