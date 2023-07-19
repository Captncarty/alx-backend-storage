#!/usr/bin/env python3
"""
Improve 12-log_stats.py by adding the top 10 of the most
present IPs in the collection nginx of the database logs:
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    database = client["logs"]
    collection = database["nginx"]

    total_logs = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents(
        {"method": method}) for method in methods}

    status_logs = collection.count_documents({"method": "GET", "path": "/status"})

    ip_counts = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print(f"{total_logs} logs where {total_logs} is the number of \
        documents in this collection")

    print("Methods:")

    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")

    print(f"method=GET\npath=/status: {status_logs}")

    print("IPs:")

    for ip in ip_counts:
        print(f"\t{ip['_id']}: {ip['count']}")

