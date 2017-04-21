__author__ = 'ronaldbjork'

fr = open("./msdos_orderpage.csv",'r')

fw = open("./clean_orderpage.csv",'w')

for line in fr:
    ar = line.split(",")
    for i in range(5,10):
        v = ar[i]
        try:
            if v != '' or v != None:
                v = round(100 * float(ar[i]))
                ar[i] = str(v)
        except ValueError :
            print("error")

    fw.write(",".join(ar))

fr.close()
fw.close()
