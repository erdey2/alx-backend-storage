#!/usr/bin/env python3
""" Update documents module """


def update_topics(mongo_collection, name, topics):
    """Update documents """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
