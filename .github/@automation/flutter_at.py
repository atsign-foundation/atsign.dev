#!/usr/bin/env python3
# Details for at_ repos

import os, sys, json, requests, yaml

# Color constants
# Reference: https://gist.github.com/chrisopedia/8754917
COLERR="\033[0;31m"
COLINFO="\033[0;35m"
COLRESET="\033[m"

baseurl = 'https://pub.dev/api'
headers = {"Content-Type": "application/json", "Accept": "application/vnd.pub.v2+json", "accept-encoding" : "gzip"}

list_file = "./.github/@automation/at_flutter.list"
output_file = "./content/en/docs/Packages/flutter.md"

def detail_at_repos(package):
    # Get list of all repos in an org
    response = requests.get(baseurl + "/packages/" + package, 
        headers=headers)
    if response.status_code != 200:
        # An error occured
        print(COLERR + "Error getting package data : " + 
        str(response.status_code) + " " + response.text + COLRESET)

    # Convert repos to YAML
    json_details = json.loads(response.text)
    #print(json_details["latest"])
    f.write(f'### {json_details["latest"]["pubspec"]["name"]}\n\n')
    f.write(f'{json_details["latest"]["pubspec"]["description"]}\n\n')
    f.write(f'[Learn more](https://pub.dev/packages/{json_details["latest"]["pubspec"]["name"]})\n\n')
    

f = open(output_file, 'w')
f.write('---\n')
f.write("title: 'Flutter packages'\n")
f.write("SEOtitle: 'Setup your Flutter (Dart) development environment'\n")
f.write("linkTitle: 'Flutter packages'\n")
f.write("Description: 'Get your environment ready to develop a Flutter app'\n")
f.write("content: 'Get your environment ready to develop a Flutter app'\n")
#f.write('parent: /Functional_Architecture/\n')
f.write('weight: 2\n')
f.write('date: 2021-12-12\n')
f.write('---\n\n\n')
at_list = open(list_file,'r')
while(True):
    package = at_list.readline().strip("\n")
    if not package:
        break
    print(package)
    detail_at_repos(package)
at_list.close
f.close