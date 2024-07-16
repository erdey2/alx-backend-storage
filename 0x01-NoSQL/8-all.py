#!/usr/env python3
""" List all documents """


def list_all(mongo_collection):
    """ List all documents in a collection """
    if mongo_collection is None:
        return ({})
    return mongo_collection.find()
