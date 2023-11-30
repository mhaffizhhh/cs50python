import random


def hasil(interval:int,jawab:int):
    if jawab>interval:
            print('Too Large')
    elif jawab<interval:
            print('Too Small')
    else:
            print('Just Right')
    

try:
    angka = int(input('Level: '))

    kuis = random.randint(1,angka)

    while True:
        try:
            tebak = int(input('Guess: '))
            if tebak>kuis:
                print('Too Large')
            elif tebak<kuis:
                print('Too Small')
            else:
                print('Just Right')
                break
        
        except:
            tebak = (input('Guess: '))
            if tebak>kuis:
                print('Too Large')
            elif tebak<kuis:
                print('Too Small')
            else:
                print('Just Right')
                break
except:
    angka = int(input('Level: '))


    kuis = random.randint(1,angka)

    try:
        while True:
            tebak = (input('Guess: '))
            if tebak>kuis:
                print('Too Large')
            elif tebak<kuis:
                print('Too Small')
            else:
                print('Just Right')
                break
        
    except:
        while True:
            tebak = (input('Guess: '))
            if tebak>kuis:
                print('Too Large')
            elif tebak<kuis:
                print('Too Small')
            else:
                print('Just Right')
                break
        
        

    