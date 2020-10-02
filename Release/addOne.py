import itertools
import sys

file_name = sys.argv[1]
dimension = sys.argv[2]

f = open(file_name + ".txt",'r')
Lines = f.readlines()
print(type(Lines))
count = 0
for line in Lines:
    line = [ word for word in line.strip().split()]
    if (len(line) == 3): 
        Lines[count] = str("{} {} {}").format(line[0],line[1],line[2])
        count +=1 
        continue 
    #print (line)
    Lines[count] = str("{} {}\r\n").format(( int (line[0]) + 1 ), ( int (line[1]) + 1 ))
    count +=1
    #print (line)
f.close()

f=open("dataset/" + file_name + ".mtx",'w')
f.writelines(["%%MatrixMarket matrix coordinate pattern general\n"])
f.writelines("{} {} {} \n".format(dimension, dimension, len(Lines)))
for line in Lines:
    f.writelines(line)
f.close()

