Python 2.5.4 (r254:67916, Dec 23 2008, 15:10:54) [MSC v.1310 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.

    ****************************************************************
    Personal firewall software may warn about the connection IDLE
    makes to its subprocess using this computer's internal loopback
    interface.  This connection is not visible on any external
    interface and no data is sent to or received from the Internet.
    ****************************************************************
    
IDLE 1.2.4      
>>> x=3
>>> 5x
SyntaxError: invalid syntax
>>> x*5
15
>>> import math
>>> math.floor(9.9)
9.0
>>> what is your name?
SyntaxError: invalid syntax
>>> name=input("what is your name")
what is your name

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    name=input("what is your name")
  File "<string>", line 0
    
   ^
SyntaxError: unexpected EOF while parsing
>>> name=input("what's your name?")
what's your name?

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    name=input("what's your name?")
  File "<string>", line 0
    
   ^
SyntaxError: unexpected EOF while parsing
>>> name=raw_input("waht' your name")
waht' your name
>>> name=input("what's your name?");print "hello"+name+"!"

