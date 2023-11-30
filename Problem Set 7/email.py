import re
import os

os.system("cls")

email = input("Email: ").strip()

matches = re.search(r"^[^@\s]+@[^@\s\.]+[^@\s\.]*\.(com|org|edu)$",email)

if matches:
    print("Valid")
else:
    print("Invalid")