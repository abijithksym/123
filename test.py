import base64
import requests
from github import Github
from pprint import pprint
import os
username = "abijithksym"
url = f"https://api.github.com/users/{username}"
g = Github()
user=g.get_user(username)
for repo in user.get_repos():
	pprint(repo)

user_data = requests.get(url).json()
print(user_data)

os.system('git init')
os.system('git add .')
os.system('git status')
print("status")
os.system('git commit -m "trail"')
print("commit")
os.system('git remote set-url origin '+ url)
print("url")
os.system('git push -f origin master')
print('\n',10*'==','completed.....',10*'==')