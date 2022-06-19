#! /usr/bin/python3
import sys, socket

offset = ""

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.74.133', 9999))
	s.send(('TRUN /.:/' + offset))
	s.close()
	
except:
	print("Err connecting to server")
	sys.exit()
