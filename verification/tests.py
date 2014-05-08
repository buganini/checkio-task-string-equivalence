"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Combining sequence": [
        {
            "input": [u"\u00C7", u"\u0043\u0327"],
            "answer": True,
        },
        {
            "input": [u'\u1ef2', u'Y\u0300'],
            "answer": True,
        },
        {
            "input": [u'\u1eb1', u'a\u0306\u0300'],
            "answer": True,
        },
        {
            "input": [u'\u1ec0', u'E\u0302\u0300'],
            "answer": True,
        },
        {
            "input": [u'\u1eea', u'U\u031b\u0300'],
            "answer": True,
        },
        {
            "input": [u'\u0200', u'A\u030f'],
            "answer": True,
        },
        {
            "input": [u'\u015a', u'S\u0301'],
            "answer": True,
        },
        {
            "input": [u'\u1eae', u'A\u0306\u0301'],
            "answer": True,
        },
        {
            "input": [u'\u1ebf', u'e\u0302\u0301'],
            "answer": True,
        },
        {
            "input": [u'\u1eda', u'O\u031b\u0301'],
            "answer": True,
        },
        {
            "input": [u'\u0150', u'O\u030b'],
            "answer": True,
        },
        {
            "input": [u'\u0174', u'W\u0302'],
            "answer": True,
        },
        {
            "input": [u'\u01ee', u'\u01b7\u030c'],
            "answer": True,
        },
        {
            "input": [u'\u0203', u'a\u0311'],
            "answer": True,
        },
        {
            "input": [u'\u011e', u'G\u0306'],
            "answer": True,
        },
        {
            "input": [u'\u0212', u'R\u0311'],
            "answer": True,
        },
        {
            "input": [u'\u026b', u'\u026b'],
            "answer": True,
        },
        {
            "input": [u'\u1eb5', u'a\u0306\u0303'],
            "answer": True,
        },
        {
            "input": [u'\u1ed6', u'O\u0302\u0303'],
            "answer": True,
        },
        {
            "input": [u'\u1eef', u'u\u031b\u0303'],
            "answer": True,
        },
        {
            "input": [u'\u0233', u'y\u0304'],
            "answer": True,
        },
        {
            "input": [u'\u1e27', u'h\u0308'],
            "answer": True,
        },
        {
            "input": [u'\u1e98', u'w\u030a'],
            "answer": True,
        },
        {
            "input": [u'\u1ee2', u'O\u031b\u0323'],
            "answer": True,
        },
        {
            "input": [u'\u1e40', u'M\u0307'],
            "answer": True,
        },
        {
            "input": [u'\u1e88', u'W\u0323'],
            "answer": True,
        },
        {
            "input": [u'\u1e88', u'W\u0307'],
            "answer": False,
        },
    ],
    "Ordering of combining marks": [
        {
            "input": [u"q\u0323\u0307", u"q\u0307\u0323"],
            "answer": True,
        },
        {
            "input": [u"\u0061\uA953\u05B0\u094D\u3099\u0062", u"\u0061\u3099\uA953\u094D\u05B0\u0062"],
            "answer": True,
        },
    ],
    "Hangul": [
        {
            "input": [u"\uB3A9", u"\u1103\u1168"],
            "answer": True,
        },
        {
            "input": [u"\uB3A9", u"\u1168\u1103"],
            "answer": False,
        },
        {
            "input": [u"\uB3A8", u"\u1103\u1168"],
            "answer": False,
        },
    ],
    "Singleton": [
        {
            "input": [u"\u212B", u"\u00C5"],
            "answer": True,
        },
        {
            "input": [u"\u9F8D", u"\uF9C4"],
            "answer": True,
        },
        {
            "input": [u"\uF90A", u"\u91D1"],
            "answer": True,
        },
        {
            "input": [u"\u212B", u"A"],
            "answer": False,
        },
    ],
    "Complex": [
        {
            "input": [u"\u0061\u0315\u0300\u05AE\u1DE6\u0062", u"\u00E0\u05AE\u1DE6\u0315\u0062"],
            "answer": True,
        },
        {
            "input": [u"\u0061\u035D\u035C\u0315\u1DFC\u0062", u"\u0061\u0315\u035C\u1DFC\u035D\u0062"],
            "answer": True,
        },
    ]
}
