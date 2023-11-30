import os

os.system("cls")

harga=50
while True:
    print(f"Harga: {harga}")

    coin = int(input('Masukkan Koin: '))

    if (coin==5 or coin==10 or coin==25) and harga-coin>=0:
        harga -= coin
        if harga==0:
            print(f"Harga: {harga}")
            break
    else:
        pass