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

styles = """
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
html, boby {
    font-family: 'Poppins', sans-serif;
    background-color: #FFFFFF;
    color: #0F294E;
}
main {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
}
h1 {
    text-align: center;
    text-transform: uppercase;
    font-weight: 200;
    padding: 2rem 0;
}
.container {
    background-color: #5F30E2;
    border-radius: 0.25rem;
    padding: 0.25rem;
    overflow: hidden;
}
table {
    width: 100%;
    border-collapse: collapse;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.08);
}
thead tr {
    background-color: #5F30E2;
    color: #FFFFFF;
    text-align: left;
}
th, td {
    padding: 12px 15px;
}

tbody tr {
    background-color: #FFFFFF;
    border-bottom: 1px solid #EFEEF3;
}
tbody tr:hover {
    font-weight: bold;
    color: #5F30E2;
}
footer {
    padding: 2rem 0;
    text-align: center;
}
a, a:visited {
    color: #5F30E2;
    font-weight: bold;
    text-decoration: none;
}
"""

html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>Programming languages TLDs</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@200;400&display=swap" rel="stylesheet">
    </head>
    <body>
        <style>
            {styles}
        </style>
        <main>
            <h1>Programming languages TLDs</h1>
            <div class="container">
                <table>
                    <thead>
                        <tr>
                            <th>Language</th>
                            <th>TLD</th>
                        </tr>
                    </thead>
                    <tbody>
                        {''.join(f'<tr><td>{lang}</td><td>{tld}</td></tr>' for lang, tld in langTlds)}
                    </tbody>
                </table>
            </div>
        </main>
        <footer>
        Sources:
            <a href="https://gist.github.com/ppisarczyk/43962d06686722d26d176fad46879d41" target="_blank" rel="noreferrer">Programming Languages extensions</a>
            and
            <a href="https://github.com/datasets/top-level-domain-names/blob/master/top-level-domain-names.csv" target="_blank" rel="noreferrer">List of all TLDs</a>
        </footer>
    </body>
</html>
"""

with open('index.html', 'w') as f:
    f.write(html)