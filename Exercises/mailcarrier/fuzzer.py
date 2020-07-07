#!/usr/bin/python

from boofuzz import *

host = '10.250.95.19'	#windows VM
port = 110		#vulnserver port

def main():
	
	session = Session(target = Target(connection = SocketConnection(host, port, proto='tcp')))
	
	s_initialize("user")	#just giving our session a name, "LTER"
    	s_string("USER", fuzzable = False)	#these strings are fuzzable by default, so here instead of blank, we specify 'false'
    	s_delim(" ", fuzzable = False)		#we don't want to fuzz the space between "LTER" and our arg
   	s_string("test",fuzzable = False)			#This value is arbitrary as we did not specify 'False' for fuzzable. Boofuzz will fuzz this string now
        s_static("\r\n")

	s_initialize("pass")	#just giving our session a name, "LTER"
    	s_string("PASS", fuzzable = False)	#these strings are fuzzable by default, so here instead of blank, we specify 'false'
    	s_delim(" ", fuzzable = False)		#we don't want to fuzz the space between "LTER" and our arg
   	s_string("test",fuzzable = False)			#This value is arbitrary as we did not specify 'False' for fuzzable. Boofuzz will fuzz this string now
        s_static("\r\n")

	s_initialize("retr")	#just giving our session a name, "LTER"
    	s_string("RETR", fuzzable = False)	#these strings are fuzzable by default, so here instead of blank, we specify 'false'
    	s_delim(" ", fuzzable = False)		#we don't want to fuzz the space between "LTER" and our arg
   	s_string("FUZZ")			#This value is arbitrary as we did not specify 'False' for fuzzable. Boofuzz will fuzz this string now
        s_static("\r\n")

        session.connect(s_get("user"))		#having our 'session' variable connect following the guidelines we established in "LTER"
	session.connect(s_get("user"), s_get("pass"))
	session.connect(s_get("pass"), s_get("retr"))

    	session.fuzz()				#calling this function actually performs the fuzzing

if __name__ == "__main__":
    main()
