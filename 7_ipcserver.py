import os
import sys

path = "/Users/apple/Desktop/ab.txt" #change path according to systems(to find type "pwd")
path2 ="/Users/apple/Desktop/bc.txt"
#li=[]
os.mkfifo(path)
fifo = open(path, "r")
for line in fifo:
    print ("Received: " + line)
    #li.append(line)

fifo.close()
print()
print("sending data to client....")
fifo2=open(path2,"w")
fifo2.write("fifo based ipc!")
fifo2.close()
