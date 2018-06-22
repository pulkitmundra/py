#! /usr/bin/python2

import commands
import time
import webbrowser
import socket
import os
from uuid import getnode as get_mac


menu='''
Press 1 to check date and time:
Press 2 to scan all the mac in your current connected network: 
Press 3 to shutdown your machine after 15 minutes:
Press 4 to print ip address of given website:
Press 5 to search something on Google
Press 6 to Logout current machine'''

print menu
choice=raw_input()


if choice == '1':
	print "current date and time is ",time.ctime()


elif choice == "2":
	print "the mac addresses of this machine :",get_mac()
	

elif choice== '3':
	print "your machine is going to restart in 15 minutes"
	os.system(shutdown -h +15)


elif choice == '4':
	ip_add=raw_input("enter the website :")
	print "ip address of the given website is"
	time.sleep(1)
	print "."
	time.sleep(1)
	print "."
	time.sleep(1)
	print "."
	print socket.gethostbyname(ip_add)
		


elif choice == '5' :
	find = raw_input("enter your query :")
	webbrowser.open_new_tab("https://www.google.com/search?q="+find)


elif choice == '6':
	

else:
	print "wrong choice"
