"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [8],
            "answer": True,
        },
        {
            "input": [42],
            "answer": False,
        },
        {
            "input": [441],
            "answer": True,
        },
        {
            "input": [469097433],
            "answer": True,
        },
        {
            "input": [12**34],
            "answer": True,
        },
    ],
    "Extra": [
        {
            "input": [9],
            "answer": True,
        },
        {
            "input": [12**34 - 1],
            "answer": False,
        },
        {
            "input": [440],
            "answer": False,
        },
    ]
}
