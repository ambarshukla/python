import requests

pep8 = requests.get("https://python.org/dev/peps/pep-0008")
print(pep8.content)
