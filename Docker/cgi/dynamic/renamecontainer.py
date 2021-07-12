#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
x = mydata.getvalue("x")
y = mydata.getvalue("y")
# x: old container
# y: new container
cmd = "sudo docker rename {0} {1}".format(x,y)
output = subprocess.getoutput(cmd)

print(output)
