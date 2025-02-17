#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch posts")


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Corde: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        posts_data = [{"id": post["id"], "title": post["title"],
                       "body": post["body"]} for post in posts]

        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            write = csv.DictWriter(csvfile, fieldnames=fieldnames)
            write.writeheader()
            write.writerows(posts_data)
        print("Posts saved in posts.csv")
    else:
        print("Failed to fetch posts")
