import requests
import sys

for word in sys.stdin:
    res = requests.get(url=f"https://cuib-cameroon.org/{word}")
    print(res)
    data = res.json()
    print(data)