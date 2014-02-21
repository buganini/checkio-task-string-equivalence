"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [u"\u212B", u"\u00C5"],
            "answer": True,
            "explanation": "compare(U+212B, U+00C5)=?"
        },
        {
            "input": [u"\u212B", u"A"],
            "answer": False,
            "explanation": 'compare(U+212B,"A")=?'
        }
    ],
    "Extra": [
        {
            "input": [u"\u212B", u"\u00C5"],
            "answer": True,
            "explanation": "compare(U+212B, U+00C5)=?"
        },
        {
            "input": [u"\u212B", u"A"],
            "answer": False,
            "explanation": 'compare(U+212B,"A")=?'
        }
    ]
}
