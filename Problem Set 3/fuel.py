try:
    fraction = input('Fraction: ')

    #mecah jadi list
    fraction_list = list(fraction)

    #ngebuat angka yang awalnya str menjadi int
    i0 = int(fraction_list[0])
    i_last = int(fraction_list[-1])

    #input hanya pecahan int seperti 1/4
    if len(fraction_list)>3:
        print('Value Error')
    else:
        hasil = (i0/i_last)*100
        #hasil gaboleh lebih dari 100
        while hasil>100:
            fraction = input('Fraction: ')

            fraction_list = list(fraction)

            i0 = int(fraction_list[0])
            i_last = int(fraction_list[-1])
            hasil = (i0/i_last)*100

        if hasil==100:
            print('F')
        elif hasil==0:
            print('E')
        else:
            print(f'{int(hasil)}%')
#jika dibagi nol atau input berupa str
except:
    print('Value Error')