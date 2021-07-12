#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
#myx = mydata.getvalue("x")



output = subprocess.getoutput("sudo docker image prune -f")
#It will delete all untagged  images
print(output)
