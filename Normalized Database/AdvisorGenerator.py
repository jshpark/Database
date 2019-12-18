import random

AdvisorDict = {
    "Roberto Coronel": 1,
    "Joe Barrett": 2,
    "Dina Bartoloni Mai": 3,
    "Jessica Chavez": 4,
    "Crystal De La Riva": 5,
    "Natalie Figueroa": 6,
    "Heather Garcia": 7,
    "James Mateik": 8,
    "Nicole Nungaray": 9,
    "Irene Quinlan": 10
}


def randomAdvisor():
    advisor = random.choice(list(AdvisorDict.keys()))
    advisor_id = AdvisorDict.get(advisor, "")
    return advisor, advisor_id
