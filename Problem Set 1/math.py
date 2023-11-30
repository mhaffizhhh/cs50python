user_input = input('Expresion: ')


def mathh(tanda_operasi,indeks):    
    #jika tanda operasi penjumlahan
    if tanda_operasi=='+':
        #jika ekpresi tanpa spasi
        if user_input[indeks-1]!=' ' and user_input[indeks+1]!=' ':
            hasil = float(user_input[:indeks])+float(user_input[indeks+1:])
            print(hasil)
        #jika ekspresi dengan spasi
        elif user_input[indeks-1]==' ' and user_input[indeks+1]==' ':
            hasil = float(user_input[:indeks-1])+float(user_input[indeks+2:])
            print(hasil)
        #jika spasi sesudah tanda operasi
        elif user_input[indeks-1]!=' ' and user_input[indeks+1]==' ':
            hasil = float(user_input[:indeks])+float(user_input[indeks+2:])
            print(hasil)
        #jika spasi sebelum tanda operasi
        elif user_input[indeks-1]==' ' and user_input[indeks+1]!=' ':
            hasil = float(user_input[:indeks-1])+float(user_input[indeks+1:])
            print(hasil)
        else:
            pass
    #pengurangan
    elif tanda_operasi=='-':
        #jika ekpresi tanpa spasi
        if user_input[indeks-1]!=' ' and user_input[indeks+1]!=' ':
            hasil = float(user_input[:indeks])-float(user_input[indeks+1:])
            print(hasil)
        #jika ekspresi dengan spasi
        elif user_input[indeks-1]==' ' and user_input[indeks+1]==' ':
            hasil = float(user_input[:indeks-1])-float(user_input[indeks+2:])
            print(hasil)
        #jika spasi sesudah tanda operasi
        elif user_input[indeks-1]!=' ' and user_input[indeks+1]==' ':
            hasil = float(user_input[:indeks])-float(user_input[indeks+2:])
            print(hasil)
        #jika spasi sebelum tanda operasi
        elif user_input[indeks-1]==' ' and user_input[indeks+1]!=' ':
            hasil = float(user_input[:indeks-1])-float(user_input[indeks+1:])
            print(hasil)
        else:
            pass
    #perkalian
    elif tanda_operasi=='*':
        #jika ekpresi tanpa spasi
        if user_input[indeks-1]!=' ' and user_input[indeks+1]!=' ':
            hasil = float(user_input[:indeks])*float(user_input[indeks+1:])
            print(hasil)
        #jika ekspresi dengan spasi
        elif user_input[indeks-1]==' ' and user_input[indeks+1]==' ':
            hasil = float(user_input[:indeks-1])*float(user_input[indeks+2:])
            print(hasil)
        #jika spasi sesudah tanda operasi
        elif user_input[indeks-1]!=' ' and user_input[indeks+1]==' ':
            hasil = float(user_input[:indeks])*float(user_input[indeks+2:])
            print(hasil)
        #jika spasi sebelum tanda operasi
        elif user_input[indeks-1]==' ' and user_input[indeks+1]!=' ':
            hasil = float(user_input[:indeks-1])*float(user_input[indeks+1:])
            print(hasil)
        else:
            pass
    #pembagian
    elif tanda_operasi=='/':
        #jika ekpresi tanpa spasi
        if user_input[indeks-1]!=' ' and user_input[indeks+1]!=' ':
            hasil = float(user_input[:indeks])/float(user_input[indeks+1:])
            print(hasil)
        #jika ekspresi dengan spasi
        elif user_input[indeks-1]==' ' and user_input[indeks+1]==' ':
            hasil = float(user_input[:indeks-1])/float(user_input[indeks+2:])
            print(hasil)
        #jika spasi sesudah tanda operasi
        elif user_input[indeks-1]!=' ' and user_input[indeks+1]==' ':
            hasil = float(user_input[:indeks])/float(user_input[indeks+2:])
            print(hasil)
        #jika spasi sebelum tanda operasi
        elif user_input[indeks-1]==' ' and user_input[indeks+1]!=' ':
            hasil = float(user_input[:indeks-1])/float(user_input[indeks+1:])
            print(hasil)
        else:
            pass
    else:
        pass

for i in range(len(user_input)):
    if user_input[i]=='+' or user_input[i]=='-' or user_input[i]=='*' or user_input[i]=='/':
        a = user_input[i]
        b = i

mathh(a,b)