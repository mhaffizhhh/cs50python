import sys
import csv

try:
    #untuk mecah argv terakhir jadi list
    arg_akhir = sys.argv[1].split(".")
except:
    pass

#kalau argv hanya 1 argumen
if len(sys.argv)<2:
    sys.exit('Too few command-line arguments')
#jika memasukkan file yang bukan regular.csv
elif len(sys.argv)==2 and sys.argv[1]!='regular.csv':
    try:
        with open(sys.argv[1],"r") as file:
                print(file.readline())
    except:
        sys.exit('File does not exist')
elif len(sys.argv)==2 and arg_akhir[1]!="csv":
    sys.exit("Not a CSV file")
else:
    data = []
    with open(sys.argv[1]) as file:
        read = csv.reader(file)

        for kol1,kol2,kol3 in read:
            print(f'| {kol1:<15} | {kol2:<8} | {kol3:<8} |')