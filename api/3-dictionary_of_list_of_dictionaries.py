#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

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
            for t in todos if str(t.get("userId")) == user_id
        ]

    with open("todo_all_employees.json", "w") as f:
        json.dump(all_data, f)