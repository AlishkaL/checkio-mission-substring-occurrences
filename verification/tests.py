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
            "input": ["hello world hello", "hello"],
            "answer": 2
        },
        {
            "input": ["Hello World hello", "hello"],
            "answer": 2
        },
        {
            "input": ["hello", "world"],
            "answer": 0
        },
        {
            "input": ["hello world hello world hello", "world"],
            "answer": 2
        },
        {
            "input": ["HELLO", "hello"],
            "answer": 1
        },
        {
            "input": ["HELLO WORLD", "WORLD"],
            "answer": 1
        },
        {
            "input": ["hello world hello", "o w"],
            "answer": 1
        },
        {
            "input": ["apple apple apple", "apple"],
            "answer": 3
        },
        {
            "input": ["apple Apple apple", "apple"],
            "answer": 3
        },
        {
            "input": ["apple", "APPLE"],
            "answer": 1
        },
    ],
    "Extra": [
        {
            "input": ["appleappleapple", "appleapple"],
            "answer": 2
        },
        {
            "input": ["test test test test", "t t"],
            "answer": 3
        },
    ]
}
