#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests


if __name__ == "__main__":
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    ).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    ).json()

    all_data = {}
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        all_data[user_id] = [
            {
                "username": username,
                "task": t.get("title"),
                "completed": t.get("completed")
            }
            for t in todos if t.get("userId") == user.get("id")
        ]

    with open("todo_all_employees.json", "w") as f:
        json.dump(all_data, f)
