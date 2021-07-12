#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
#mydata1 = cgi.FieldStorage()
myx = mydata.getvalue("x")

#myy = mydata.getvalue("y")


output = subprocess.getoutput("sudo " + myx)
print(output)
#outputy = subprocess.getoutput("sudo " + imyy)
#print(outputy)
