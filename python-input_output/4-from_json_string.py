#!/usr/bin/python3
"""A function that returns an object represented by a JSON string"""


import json


def from_json_string(my_str):
    """The function"""
    return json.loads(my_str)
