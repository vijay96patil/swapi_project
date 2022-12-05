"""The Star Wars API lists 82 main characters in the Star Wars saga. For the first task, we w
ould like you to use a random number generator that picks a number between 1-82. Using the
se random numbers you will be pulling 15 characters from the API using Python."""


"""

TASK / PROBLEM STATEMENT

THe star wars API lists 82 characters in stars wars series. For the first task
we have to create a random number generator. The random number generator should
fetch numbers between 1-82. Using these random numbers we have to fetch random
15 characters from API using `requests` lib.
"""

import requests
from utils.randgen import ProduceChars

start = 1
stop = 83




def get_chars(obj_: ProduceChars):
    characters = []  # [1, 4, 5, 13, ....]
    for i in obj_:
        characters.append(i)

    return characters


if __name__ == "__main__":
    print(__name__)
    print("current module getting executed")

    home_url = "https://swapi.dev"
    relative = "/api/people/{0}"  # magic string

    print(f"[ INFO ] producing random 15 characters...")
    obj = ProduceChars(start, stop)
    characters = get_chars(obj)

    # import pdb                     ### Debugging
    # pdb.set_trace()                  ## acts as the break point and stop the code execution at the middle of execution

    print(f"[ INFO ] done - producing random 15 characters")

    for num_ in characters:
        absolute_url = home_url + relative.format(num_)               ### str formating
        print(f"fetching details using - {absolute_url}  =>\n")
        response = requests.get(absolute_url)
        response = response.json()                    ## get the data in to json format
        print(response)
        print("######" * 25)



