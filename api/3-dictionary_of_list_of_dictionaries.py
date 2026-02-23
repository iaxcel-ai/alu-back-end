#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests

if __name__ == "__main__":
    base = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(base)).json()
    todos = requests.get("{}/todos".format(base)).json()

    user_map = {}
    for user in users:
        user_map[user["id"]] = user["username"]

    all_tasks = {}
    for task in todos:
        uid = task["userId"]
        uid_str = str(uid)
        if uid_str not in all_tasks:
            all_tasks[uid_str] = []
        all_tasks[uid_str].append({
            "username": user_map[uid],
            "task": task["title"],
            "completed": task["completed"]
        })

    with open("todo_all_employees.json", "w") as f:
        json.dump(all_tasks, f)
