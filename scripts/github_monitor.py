import requests
import os
from dotenv import load_dotenv

load_dotenv()

print(f"Username from env: {os.environ.get('GITHUB_USERNAME')}")
def call_api(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raises exception for 4xx/5xx codes
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.ConnectionError:
        print("Connection error")
    except requests.exceptions.Timeout:
        print("Request timed out")
    return None

username = os.environ.get("GITHUB_USERNAME")

# build the URL with your username
profile_url = f"https://api.github.com/users/{username}"

# call the function
profile = call_api(profile_url)

if profile is None:
    print("Failed to get profile")
# print the results
else:
    print(f"Username: {profile['login']}")
    print(f"Public repos: {profile['public_repos']}")
    print(f"Created: {profile['created_at']}")

repo_url = f"https://api.github.com/users/{username}/repos"
repos = call_api(repo_url)

if repos:
    for repo in repos:
        print(repo['name'])

if repo is None:
    print("Failed to get repo")
else:
    print(f"\nRepo: {repo['full_name']}")
    print(f"Stars: {repo['stargazers_count']}")
    print(f"Open issues: {repo['open_issues_count']}")
    print(f"Last updated: {repo['updated_at']}")

webhook=os.environ.get("SLACK_WEBHOOK")

def send_slack(message):
    payload = {"text": message}
    response = requests.post(webhook, json=payload)
    if response.status_code == 200:
        print("Alert sent to Slack!")
    else:
        print(f"Failed to send alert: {response.status_code}")

send_slack("Test alert from Python.")