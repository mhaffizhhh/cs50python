import sys
import function

try:
    arg_akhir = sys.argv[1].split(".")
except:
    pass

#argumen terlalu dikit
if len(sys.argv)<2:
    sys.exit('Too few command-line arguments')
#argumen terlalu banyak
elif len(sys.argv)>2:
    sys.exit('Too many command-line arguments')
#argumen bukan file yang diinginkan
elif len(sys.argv)==2 and sys.argv[1]!='function.py':
    #jika argumen kedua tanpa (jenis file)
    b = sys.argv[1].find(".")
    if b==-1:
        sys.exit('Invalid input')
    #jika dengan jenis file namun bukan .py
    elif arg_akhir[1]!='py':
        sys.exit('Not a Python file')
    #jika jenis file py namun bukan file yang tersedia
    else:
        sys.exit('File does not exist')
#argumen sesuai yang diinginkan
elif sys.argv[1]=='function.py':
    sys.argv[1]
else:
    pass