#!/usr/bin/env python
# Designed for use with boofuzz v0.0.1-dev3
from boofuzz import *
import time

def main():
	session = Session(target=Target(connection=SocketConnection("192.168.1.218", 21, proto='tcp')))    

	s_initialize("user")
	s_string("USER", fuzzable = False)
	s_delim(" ", fuzzable = False)
	s_string("anonymous")
	s_static("\r\n")    

	s_initialize("pass")
	s_string("PASS", fuzzable = False)
	s_delim(" ", fuzzable = False)
	s_string("test")
	s_static("\r\n")    

#	s_initialize("stor")
#	s_string("STOR", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")    

#	s_initialize("retr")
#	s_string("RETR", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("abor")
#	s_string("ABOR", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("acct")
#	s_string("ACCT", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("adat")
#	s_string("ADAT", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("allo")
#	s_string("ALLO", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("appe")
#	s_string("APPE", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("auth")
#	s_string("AUTH", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("avbl")
#	s_string("AVBL", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")   

	
#	s_initialize("ccc")
#	s_string("CCC", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("cdup")
#	s_string("CDUP", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("conf")
#	s_string("CONF", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("csid")
#	s_string("CSID", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

	s_initialize("cwd")
	s_string("CWD", fuzzable = False)
	s_delim(" ", fuzzable = False)
	s_string("AAAA")
	s_static("\r\n")

#	s_initialize("dele")
#	s_string("DELE", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("dsiz")
#	s_string("DSIZ", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("enc")
#	s_string("ENC", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("eprt")
#	s_string("EPRT", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("epsv")
#	s_string("EPSV", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("feat")
#	s_string("FEAT", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")


#	s_initialize("host")
#	s_string("HOST", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("lang")
#	s_string("LANG", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("list")
#	s_string("LIST", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("lprt")
#	s_string("LPRT", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("lpsv")
#	s_string("LPSV", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("mdtm")
#	s_string("MDTM", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("mfct")
#	s_string("MFCT", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("mff")
#	s_string("MFF", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("mfmt")
#	s_string("MFMT", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("mic")
#	s_string("MIC", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("mkd")
#	s_string("MKD", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("mlsd")
#	s_string("MLSD", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("mlst")
#	s_string("MLST", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("mode")
#	s_string("MODE", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("nlst")
#	s_string("NLST", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("noop")
#	s_string("NOOP", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("opts")
#	s_string("OPTS", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("pasv")
#	s_string("PASV", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("pbsz")
#	s_string("PBSZ", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("port")
#	s_string("PORT", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("prot")
#	s_string("PROT", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("rest")
#	s_string("REST", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("retr")
#	s_string("RETR", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("rmd")
#	s_string("RMD", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("rmda")
#	s_string("RMDA", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("rnfr")
#	s_string("RNFR", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("rnto")
#	s_string("RNTO", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("site")
#	s_string("SITE", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("size")
#	s_string("SIZE", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("smnt")
#	s_string("SMNT", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("spsv")
#	s_string("SPSV", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("stat")
#	s_string("STAT", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("stor")
#	s_string("STOR", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("stou")
#	s_string("STOU", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("stru")
#	s_string("STRU", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("syst")
#	s_string("SYST", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("thmb")
#	s_string("THMB", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("type")
#	s_string("TYPE", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("xcup")
#	s_string("XCUP", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("xmkd")
#	s_string("XMKD", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("xpwd")
#	s_string("XPWD", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("xrcp")
#	s_string("XRCP", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("xrmd")
#	s_string("XRMD", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("xrsq")
#	s_string("XRSQ", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("xsem")
#	s_string("XSEM", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")

#	s_initialize("xsen")
#	s_string("XSEN", fuzzable = False)
#	s_delim(" ", fuzzable = False)
#	s_string("AAAA")
#	s_static("\r\n")
	session.connect(s_get("user"))
	session.connect(s_get("user"), s_get("pass"))
	#session.connect(s_get("pass"), s_get("stor"))
	#session.connect(s_get("pass"), s_get("retr")) 
	#session.connect(s_get("pass"), s_get("abor"))
	#session.connect(s_get("pass"), s_get("acct"))
	#session.connect(s_get("pass"), s_get("adat"))
	#session.connect(s_get("pass"), s_get("allo"))
	#session.connect(s_get("pass"), s_get("appe"))
	#session.connect(s_get("pass"), s_get("auth"))
	#session.connect(s_get("pass"), s_get("avbl"))
	#session.connect(s_get("pass"), s_get("ccc"))
	#session.connect(s_get("pass"), s_get("cdup"))
	#session.connect(s_get("pass"), s_get("conf"))
	#session.connect(s_get("pass"), s_get("csid"))
	session.connect(s_get("pass"), s_get("cwd"))
	#session.connect(s_get("pass"), s_get("dele"))
	#session.connect(s_get("pass"), s_get("dsiz"))
	#session.connect(s_get("pass"), s_get("enc"))
	#session.connect(s_get("pass"), s_get("eprt"))
	#session.connect(s_get("pass"), s_get("epsv"))
	#session.connect(s_get("pass"), s_get("feat"))
	#session.connect(s_get("pass"), s_get("host"))
	#session.connect(s_get("pass"), s_get("lang"))
	#session.connect(s_get("pass"), s_get("list"))
	#session.connect(s_get("pass"), s_get("lprt"))
	#session.connect(s_get("pass"), s_get("lpsv"))
	#session.connect(s_get("pass"), s_get("mdtm"))
	#session.connect(s_get("pass"), s_get("mfct"))
	#session.connect(s_get("pass"), s_get("mff"))
	#session.connect(s_get("pass"), s_get("mfmt"))
	#session.connect(s_get("pass"), s_get("mic"))
	#session.connect(s_get("pass"), s_get("mkd"))
	#session.connect(s_get("pass"), s_get("mlsd"))
	#session.connect(s_get("pass"), s_get("mlst"))
	#session.connect(s_get("pass"), s_get("mode"))
	#session.connect(s_get("pass"), s_get("nlst"))
	#session.connect(s_get("pass"), s_get("noop"))
	#session.connect(s_get("pass"), s_get("opts"))
	#session.connect(s_get("pass"), s_get("pasv"))
	#session.connect(s_get("pass"), s_get("pbsz"))
	#session.connect(s_get("pass"), s_get("port"))
	#session.connect(s_get("pass"), s_get("prot"))
	#session.connect(s_get("pass"), s_get("rest"))
	#session.connect(s_get("pass"), s_get("retr"))
	#session.connect(s_get("pass"), s_get("rmd"))
	#session.connect(s_get("pass"), s_get("rmda"))
	#session.connect(s_get("pass"), s_get("rnfr"))
	#session.connect(s_get("pass"), s_get("rnto"))
	#session.connect(s_get("pass"), s_get("site"))
	#session.connect(s_get("pass"), s_get("size"))
	#session.connect(s_get("pass"), s_get("smnt"))
	#session.connect(s_get("pass"), s_get("spsv"))
	#session.connect(s_get("pass"), s_get("stat"))
	#session.connect(s_get("pass"), s_get("stor"))
	#session.connect(s_get("pass"), s_get("stou"))
	#session.connect(s_get("pass"), s_get("stru"))
	#session.connect(s_get("pass"), s_get("syst"))
	#session.connect(s_get("pass"), s_get("thmb"))
	#session.connect(s_get("pass"), s_get("type"))
	#session.connect(s_get("pass"), s_get("xcup"))
	#session.connect(s_get("pass"), s_get("xmkd"))
	#session.connect(s_get("pass"), s_get("xpwd"))
	#session.connect(s_get("pass"), s_get("xrcp"))
	#session.connect(s_get("pass"), s_get("xrmd"))
	#session.connect(s_get("pass"), s_get("xrsq"))
	#session.connect(s_get("pass"), s_get("xsem"))
	#session.connect(s_get("pass"), s_get("xsen"))
	
	session.fuzz()

if __name__ == "__main__":
	main()
