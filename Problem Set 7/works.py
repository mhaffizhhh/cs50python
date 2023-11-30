import re
import os

os.system("cls")

works = input("Hours: ").strip()

matches = re.search(r"9(?::|\.)(\d\d)[a-z\s]*5(?::|\.)?(\d{2})[a-z\s]*",works,re.IGNORECASE)
                    #9   :/.     ##    am to 5   :/.       ##     pm
                    # (#) artinya angka

if matches:
    print(f"9:{matches.group(1)} to 17:{matches.group(2)}")
else:
    print("Invalid")