import os
import json

DIR = "Law"
courses = ["q_law101.json", "q_law200.json"]

print(f"{'Course':<15} | {'Posts':<8} | {'Comments':<10}")
print("-" * 38)
total_posts = 0
total_comments = 0

for c in courses:
    path = os.path.join(DIR, c)
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                posts = len(data)
                comments = sum(len(p.get("comments", [])) for p in data)
                print(f"{c:<15} | {posts:<8} | {comments:<10}")
                total_posts += posts
                total_comments += comments
        except Exception as e:
            print(f"{c:<15} | err: {e}")
    else:
        print(f"{c:<15} | {'-':<8} | {'-':<10}")

print("-" * 38)
print(f"{'Total':<15} | {total_posts:<8} | {total_comments:<10}")
