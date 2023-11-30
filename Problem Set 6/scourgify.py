import sys
import csv

if len(sys.argv)<3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv)>3:
    sys.exit('Too many command-line arguments')
elif len(sys.argv)==3:
    try:
    #jika argv[1] == before.csv
        with open(sys.argv[1]) as file:
            read = csv.DictReader(file,delimiter=",")

            for i in read:
                print(f'{i["name"]} {i["house"]}')
    except:
        sys.exit(f'Could not read {sys.argv[1]}')
    #jika argv[1] == before.csv, maka akan append argv[2] yaitu after.csv
    else:
        with open(sys.argv[2],"a",newline="") as file:
            print('\n')
            first = input('First name: ')
            last = input('Last name: ')
            house = input('House: ')

            writer = csv.DictWriter(file,fieldnames=['first','last','house'],)

            writer.writerow({'first':first,'last':last,'house':house})