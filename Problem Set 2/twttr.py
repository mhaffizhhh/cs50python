import os

os.system("cls")

input_user = input('Input: ')

list_konsonan = []

for i in range(len(input_user)):
    if input_user[i].lower()=='a' or input_user[i].lower()=='i' or input_user[i].lower()=='u' or input_user[i].lower()=='e' or input_user[i].lower()=='o':
        pass
    else:
        list_konsonan.append(input_user[i])

print(f"Output: {''.join(list_konsonan)}")