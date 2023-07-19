#!/usr/bin/env python3
"""
Write a Python function that inserts a new document in a collection
based on kwargs:
Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
"""


def insert_school(mongo_collection, **kwargs):
    """
    Returns the new _id
    """
    insert = mongo_collection.insert_one(kwargs)

    return insert.inserted_id

