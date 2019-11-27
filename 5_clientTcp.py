from socket import*
serverName=gethostname()
serverPort=12001
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
file1=input("Enter file name and the word : ") #create some txt file on desktop with any 2 words repeating and enter eg. file1.txt hello
clientSocket.send(file1.encode())
wordcount=clientSocket.recv(1024).decode('utf8')
print(wordcount)
clientSocket.close()
