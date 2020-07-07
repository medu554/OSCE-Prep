#!/usr/bin/python

from boofuzz import *

host = '10.250.80.6'	#windows VM
port = 9999		#vulnserver port

def main():
	
	session = Session(target = Target(connection = SocketConnection(host, port, proto='tcp')))
	
	s_initialize("LTER")	#just giving our session a name, "LTER"

    	s_string("LTER", fuzzable = False)	#these strings are fuzzable by default, so here instead of blank, we specify 'false'
    	s_delim(" ", fuzzable = False)		#we don't want to fuzz the space between "LTER" and our arg
   	s_string("FUZZ")			#This value is arbitrary as we did not specify 'False' for fuzzable. Boofuzz will fuzz this string now
 
        session.connect(s_get("LTER"))		#having our 'session' variable connect following the guidelines we established in "LTER"
    	session.fuzz()				#calling this function actually performs the fuzzing

if __name__ == "__main__":
    main()
