#!/usr/bin/python
#Simple Python script to parse values out of FING network scans into a pipe delimited txt file specified via command line aguments
# 1st arg is input file name 2nd Arg is output file name
# this script outputs | delimited data
# This script assumes output from https://www.fing.io apple app

import re, sys, os, datetime
from datetime import datetime

finglog = open(sys.argv[1],"r")

# Open Parsed results file
fingresults = open(sys.argv[2],"w")

#Create Header row 
fingresults.write("Network Name|IP Address|MAC Address|Vendor|Type\n")



MACAddrVal = ""
IPNumVal = ""
VendorVal = ""
TypeVal = ""

#loop through fing data
for line in finglog:
	
	#find record types
	# get source of value			
	if re.search(r"Network: ",line):
		Network=re.search(r"Network: \w+\s+\S+",line)
		NetworkVal=Network.group()[9:]

	if re.search(r"IP Address:",line):
		IPNum=re.search(r"IP Address:\s+\d+\.\d+\.\d+\.\d+",line)
        	IPNumVal = IPNum.group()[12:]

	if re.search(r"MAC Address:",line):
		MACAddr =re.search(r"MAC Address:\s+\w+\:\w+\:\w+\:\w+\:\w+\:\w+",line)
		MACAddrVal = MACAddr.group()[13:]

	if re.search(r"Vendor:",line):
		Vendor = re.search(r"Vendor:\s+\S+",line)
		VendorVal =Vendor.group()[8:]

	if re.search(r"Type:",line):
		Type=re.search(r"Type:\s+\w+",line)
		TypeVal=Type.group()[6:]
		# Output results to file
		fingresults.write(NetworkVal + "|" + IPNumVal + "|" + MACAddrVal + "|" + VendorVal + "|" + TypeVal + "\n")


#Close files
finglog.close()
fingresults.close()



