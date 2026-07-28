# from datetime import date
#
# today = date.today()
# print(today)               # 2026-07-23 (or whenever you run it)
#
# deadline = date(2026, 7, 25)         # year, month, day — a real date object
# print(deadline > today)              # True — dates COMPARE! It's in the future
# print((deadline - today).days)
#
#
# d = date.fromisoformat("2026-07-25")     # text → date (must be YYYY-MM-DD)
# s = d.isoformat()                        # date → text (for JSON — JSON can't hold date objects!)

# from datetime import date
#
# today = date.today()
# print(today)
# birthday = date(2026, 7 , 24)
# print((birthday - today).days)
# date.fromisoformat("25-05-2026")

# import requests
#
# response = requests.get("https://api.github.com")
# print(response.status_code)      # 200 means "OK!"
# print(response.json())           # the response, as a DICTIONARY

import requests

response = requests.get("https://api.agify.io?name=varad")
data = response.json()
print(data["age"])