#!/usr/bin/env python3
""" Insert new document module """


def insert_school(mongo_collection, **kwargs):
    docs = mongo_collection.insert_one(kwargs)
    return docs.inserted_id
