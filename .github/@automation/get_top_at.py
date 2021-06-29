#!/usr/bin/env python3
# Find pub.dev repos starting with at_

import os, sys, json, requests, yaml

# Color constants
# Reference: https://gist.github.com/chrisopedia/8754917
COLERR="\033[0;31m"
COLINFO="\033[0;35m"
COLRESET="\033[m"

baseurl = 'https://pub.dev/api'
headers = {"Content-Type": "application/json", "accept-encoding" : "gzip"}

list_file = "./.github/@automation/at_pubdev.list"

def list_at_repos():
    # Get list of all repos in an org
    response = requests.get(baseurl + "/package-name-completion-data", 
        headers=headers)
    if response.status_code != 200:
        # An error occured
        print(COLERR + "Error getting package name completion data : " + str(response.status_code) + " " + response.text
        + COLRESET)

    # Convert repos to YAML
    json_repos = json.loads(response.text)
    #print(json.dumps(json_cards, indent=4, sort_keys=True))
    f = open(list_file, 'w')
    for package in json_repos['packages']:
        if package.startswith("at_"):
            f.write(f"{package}\n")
            print(package)
    f.close

list_at_repos() 