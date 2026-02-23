#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests

if __name__ == "__main__":
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()

    user_map = {user.get('id'): user.get('username') for user in users}

    all_tasks = {}
    for task in todos:
        user_id = task.get('userId')
        user_id_str = str(user_id)
        if user_id_str not in all_tasks:
            all_tasks[user_id_str] = []
        all_tasks[user_id_str].append({
            "username": user_map[user_id],
            "task": task.get('title'),
            "completed": task.get('completed')
        })

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)
