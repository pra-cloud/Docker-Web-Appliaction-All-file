#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
name = mydata.getvalue("name")

cmd = "sudo docker inspect {}".format(name)
output = subprocess.getoutput(cmd)

print(output)
