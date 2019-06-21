"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key,
    it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {'input': [1084], 'answer': ['Tuesday', 'Wednesday']},
        {'input': [1167], 'answer': ['Sunday']},
        {'input': [1216], 'answer': ['Friday', 'Saturday']},
        {'input': [1492], 'answer': ['Friday', 'Saturday']},
        {'input': [1770], 'answer': ['Monday']},
        {'input': [1785], 'answer': ['Saturday']},
        {'input': [212], 'answer': ['Wednesday', 'Thursday']},
        {'input': [1], 'answer': ['Monday']},
        {'input': [2135], 'answer': ['Saturday']},
        {'input': [3043], 'answer': ['Sunday']},
        {'input': [2001], 'answer': ['Monday']},
        {'input': [3150], 'answer': ['Sunday']},
        {'input': [3230], 'answer': ['Tuesday']},
        {'input': [328], 'answer': ['Monday', 'Sunday']},
        {'input': [2016], 'answer': ['Friday', 'Saturday']},
    ],
    "Extra": [
        {'input': [334], 'answer': ['Monday']},
        {'input': [1986], 'answer': ['Wednesday']},
        {'input': [3361], 'answer': ['Thursday']},
        {'input': [5863], 'answer': ['Thursday']},
        {'input': [1910], 'answer': ['Saturday']},
        {'input': [1968], 'answer': ['Monday', 'Tuesday']},
        {'input': [7548], 'answer': ['Thursday', 'Friday']},
        {'input': [8116], 'answer': ['Wednesday', 'Thursday']},
        {'input': [9137], 'answer': ['Friday']},
        {'input': [1794], 'answer': ['Wednesday']},
        {'input': [1900], 'answer': ['Monday']},
        {'input': [2100], 'answer': ['Friday']},
    ]
}
