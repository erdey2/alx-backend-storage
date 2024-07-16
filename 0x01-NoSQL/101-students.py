#!/usr/bin/env python3
""" find and sort """


def top_students(mongo_collection):
    """ returns all students sorted by average score """
    return mongo_collection.find().sort({average: 1})
