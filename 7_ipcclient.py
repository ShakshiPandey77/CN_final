import os
import sys

path = "/Users/apple/Desktop/ab.txt"
path2= "/Users/apple/Desktop/bc.txt"


fifo = open(path, "w")
fifo.write("fifo based ipc!")
fifo.close()
os.mkfifo(path2)
fifo2=open(path2,"r")
for l in fifo2:
    print(l)
fifo2.close()
