import sys
import socket
import time
import random

sendingPort = int(sys.argv[1])
receivingPort = int(sys.argv[2])
buffer = int(sys.argv[3])
isHead = int(sys.argv[4])
nodeNum = sys.argv[5]

def incomingPacketQ():
   global buffer
   if (random.random() <= 0.25): 
        buffer = buffer + 1   
        print("Buffer Increased: packet was received") 
   
def join_ring():
   global buffer
   
   while (True):
      time.sleep(2)
   
      token = clientSocket.recvfrom(1024)
      time.sleep(2)
      print()
      print("Node " + str(nodeNum) + " received token")
          
      if (buffer == 0):
         print("Buffer Empty: sending token to next node")
         clientSocket.sendto(str("token").encode(),(host,sendingPort))
         print("Token sent to next node")
         incomingPacketQ()
         print("Idle: waiting for token")
         
      else:
         buffer = buffer - 1
         print("Packet Sent: buffer size is now " + str(buffer))
         
         clientSocket.sendto(str("token").encode(),(host,sendingPort))
         print("Token sent to next node")

         incomingPacketQ()
         print("Idle: waiting for token")    

# start of logic
host = socket.gethostname()
connection = (host,receivingPort)

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientSocket.bind( connection )

print("Node " + str(nodeNum) + " has started up")

if (isHead == 1):
   print("Node " + str(nodeNum) + " is the head node")
   buffer = buffer - 1
   print("Packet Sent: buffer size is " + str(buffer))
         
   clientSocket.sendto(str("token").encode(),(host,sendingPort))
   print("Token sent to next node")

   incomingPacketQ
   print("Idle: waiting for token")

   join_ring()
     
else:
   join_ring()  


