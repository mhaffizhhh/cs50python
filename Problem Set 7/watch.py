import re
import os

os.system("cls")

html = input("HTML: ")

matches = re.search(r'"https?://www\.youtube\.com/embed/(\w+)"',html,re.IGNORECASE)
if matches:
    print(f"https://youtu.be/{matches.group(1)}")
else:
    print(None)