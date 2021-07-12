#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
x = mydata.getvalue("x")

cmd = "sudo docker start {}".format(x)
output = subprocess.getoutput(cmd)

print(output)
