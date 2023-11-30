import os

os.system("cls")

input_user = input('camel Case: ')

#untuk mecah input_user jadi character yang nantinya di ''.join
list_snake=[]

#untuk insert underscore karena ketika insert char baru(_) index input user nambah panjang 1
iterasi_underscore=0

for i in range(len(input_user)):
    #memasukkan tiap char ke list baru
    list_snake.append(input_user[i])
    if input_user[i].isupper():
        list_snake.insert(i+iterasi_underscore,'_')
        iterasi_underscore += 1

print(f"Snake_Case: {''.join(list_snake).lower()}")