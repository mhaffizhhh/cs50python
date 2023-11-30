data = []

print('uses ctrl+z to end program\n')

while True:
    try:
        data_input = input('').upper()
        data.append(data_input)
    except EOFError:
        break

#ngebuat data list menjadi unik
data_set = set(data)

#ngitung banyak value di himpunan berdasarkan data asli di list
for i in data_set:
    print(f'{data.count(i)} {i}')