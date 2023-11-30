def main():
    waktu = str(input('Jam Berapa Sekarang? '))
    makan = convert_time(waktu)
    if makan>=7 and makan<=8:
        print('Breakfast Time')
    elif makan>=12 and makan<=13:
        print('Lunch Time')
    elif makan>=18 and makan<=19:
        print('Dinner Time')
    else:
        None

def convert_time(time):
    menit = int(time[-1:-3:-1])/60
    if len(time)==5:
        jam=int(time[:2])
    else:
        jam=int(time[:1])
    return jam+menit


if __name__ =='__main__':
    main()