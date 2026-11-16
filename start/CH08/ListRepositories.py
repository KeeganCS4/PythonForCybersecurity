#!/usr/bin/env python3
# Script that lists repositories in GitHub
# Requires a Personal Access Token to run
# By Keegan 11/16

import os
import requests
import configparser

def get_api_key(keyname):
    # get the location of the secrets file
    home_dir = os.path.expanduser("~")
    secrets_file = os.path.join(home_dir, "secrets.ini")
    # create configparser and load file
    config = configparser.ConfigParser()
    config.read(secrets_file)
    # get api key and return
    api_key = config["APIKeys"][keyname]
    return api_key

def get_repositories(token):
    url = "https://api.github.com/user/repos"
    headers = {"Accept": "application/vnd.github+json", "Authorization": f"Bearer {token}", "X-GitHub-Api-Version": "2026-03-10"}
    response = requests.get(url, headers=headers)
    return response.json()

# get token
token = get_api_key("github")
# get repos
repos = get_repositories(token)
# print name of repos
for repo in repos:
    print(repo["name"])
