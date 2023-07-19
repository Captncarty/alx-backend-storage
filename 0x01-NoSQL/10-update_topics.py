#!/usr/bin/env python3
"""
Write a Python function that changes all topics of a school
Prototype: def update_topics(mongo_collection, name, topics):
mongo_collection will be the pymongo collection object
name (string) will be the school name to update
topics (list of strings) will be the list 
of topics approached in the school
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    """
    att = { "name" : name }

    new_top = { "$set" : { "topics" : topics } }
    
    update = mongo_collection.update_many(att, new_top)

    return update

