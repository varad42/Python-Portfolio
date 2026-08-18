# Lesson 28: pip — the universe of other people's toolboxes 🌐

import requests

response = requests.get("https://api.agify.io?name=varad")
data = response.json()
print(data["age"])