#!/usr/bin/env python
# Designed for use with boofuzz v0.0.9
from boofuzz import *


def main():
    session = Session(
        target=Target(
            connection=SocketConnection("192.168.1.219", 80, proto='tcp')
        ),
    )

    s_initialize(name="Request")
    with s_block("Request-Line"):
        s_group("Method", ["GET"])
        s_delim(" ", name='space-1')
        s_string("/", name='Request-URI')
        s_delim(" ", name='space-2')
        s_string("HTTP/1.1", name='HTTP-Version')
	s_delim("\r\n", name='return-1', fuzzable = False)
	s_string("Host:", name="Host")
	s_delim(" ", name="space-3")
	s_string("192.168.1.219", name="Host-Value")
	s_delim("\r\n", name="return-2", fuzzable = False)
	s_string("User-Agent:", name="User-Agent")
	s_delim(" ", name="space-4")
	s_string("Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0", name="User-Agent-Value")
	s_delim("\r\n", name="return-3", fuzzable = False)
	s_string("Accept:", name="Accept")
	s_delim(" ", name="space-5")
	s_string("text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", name="Accept-Value")
	s_delim("\r\n", name="return-4", fuzzable = False)
	s_string("Accept-Language:", name="Accept-Language")
	s_delim(" ", name="space-6")
	s_string("en-US,en;q=0.5", name="Accept-Language-Value")
	s_delim("\r\n", name="return-5", fuzzable = False)
	s_string("Accept-Encoding:", name="Accept-Encoding")
	s_delim(" ", name="space-7")
	s_string("gzip, deflate", name="Accept-Encoding-Value", fuzzable = False)
	s_delim("\r\n", name="return-6")
	s_string("If-Modified-Since:", name="If-Modified-Since")
	s_delim(" ", name="space-8")
	s_string("Wed, ", name="If-Modified-Since-Value", fuzzable = False)
	s_string("a", name="If-Modified-Since-Value2")
	s_delim("\r\n", name="return-7", fuzzable = False)
        s_static("\r\n", name="Request-Line-CRLF")
    s_static("\r\n", "Request-CRLF")

    session.connect(s_get("Request"))

    session.fuzz()


if __name__ == "__main__":
    main()
