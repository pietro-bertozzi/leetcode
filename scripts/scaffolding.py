import os
import json
import re
import sys
import time
import requests

GRAPHQL_URL = "https://leetcode.com/graphql"

def to_slug(name: str) -> str:
    slug = name.lower()
    slug = re.sub(r"[^a-z0-9 \-]+", "", slug)
    slug = slug.replace(" ", "-")
    slug = re.sub(r"-+", "-", slug)
    return slug

def fetch_problem_details(name: str) -> dict:
    title_slug = to_slug(name)
    query = """
    query getQuestionDetail($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionFrontendId
        title
        titleSlug
        difficulty
        topicTags { name }
      }
    }
    """
    variables = {"titleSlug": title_slug}
    response = requests.post(GRAPHQL_URL, json={"query": query, "variables": variables},
                             headers={"Content-Type": "application/json"})
    response.raise_for_status()
    data = response.json()
    if "errors" in data:
        raise Exception(data["errors"])
    q = data["data"]["question"]
    return {
        "id": q["questionFrontendId"],
        "title": q["title"],
        "slug": q["titleSlug"],
        "difficulty": q["difficulty"],
        "tags": [t["name"] for t in q.get("topicTags", [])]
    }

def normalize_filename(problem_id, title, ext=".py"):
    safe = re.sub(r'[^a-z0-9]', '_', title.lower())
    safe = re.sub(r'_+', '_', safe).strip('_')
    return f"lc_{str(problem_id).zfill(4)}_{safe}{ext}"

def create_problem_file(base_dir: str, problem: dict):
    os.makedirs(base_dir, exist_ok=True)
    filepath = os.path.join(base_dir, normalize_filename(problem["id"], problem["title"]))
    if not os.path.exists(filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {problem['title']} (https://leetcode.com/problems/{problem['slug']}/)\n")
            f.write(f"# Difficulty: {problem['difficulty']}\n")
            if problem.get("tags"):
                f.write(f"# Tags: {', '.join(problem['tags'])}\n")
    return filepath

def main():
    if len(sys.argv) < 2:
        print("Usage: python leetcode_scaffold.py <input_names.json>")
        sys.exit(1)

    input_file = sys.argv[1]
    group_name = os.path.splitext(os.path.basename(input_file))[0]

    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_repo = os.path.join(root_dir, "problems", group_name)

    with open(input_file, encoding="utf-8") as f:
        problem_names = json.load(f)["problems"]

    problems = []
    for name in problem_names:
        try:
            problems.append(fetch_problem_details(name))
            time.sleep(0.2)
        except Exception as e:
            print(f"Error fetching '{name}': {e}")

    os.makedirs(base_repo, exist_ok=True)
#    details_file = os.path.join(base_repo, f"{group_name}-details.json")
    details_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{group_name}-details.json")
    with open(details_file, "w", encoding="utf-8") as f:
        json.dump(problems, f, indent=2)

    for problem in problems:
        create_problem_file(base_repo, problem)

    print(f"Scaffolding completed: {len(problems)} problems in {base_repo}")
    print(f"Details saved in: {details_file}")

if __name__ == "__main__":
    main()
