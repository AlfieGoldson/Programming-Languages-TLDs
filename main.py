import requests

languagesUrl = 'https://gist.githubusercontent.com/ppisarczyk/43962d06686722d26d176fad46879d41/raw/211547723b4621a622fc56978d74aa416cbd1729/Programming_Languages_Extensions.json'
languagesData = requests.get(languagesUrl).json()

tldsUrl = 'https://raw.githubusercontent.com/datasets/top-level-domain-names/master/top-level-domain-names.csv'
tldsData = requests.get(tldsUrl).text

langTlds = []

for lang in languagesData:
    if 'extensions' not in lang:
        continue
    for tld in tldsData.split('\n'):
        ext = tld.split(',')[0]
        if ext in lang['extensions']:
            langTlds.append([lang['name'], ext])

template = ""

with open('template.html', 'r') as templateFile:
    template = templateFile.read()

template = template.replace('{langTlds}', str(langTlds))

with open('index.html', 'w') as f:
    f.write(template)