import re
import os

os.system("cls")

um = input("Input: ")

matches = re.findall(r"um",um,re.IGNORECASE)

print(len(matches))