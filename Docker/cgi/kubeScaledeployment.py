#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

dname = mydata.getvalue("dname")
scale = mydata.getvalue("scale")
#print(vol)
#print(mount)

if (dname and scale)==None:
        output2 = subprocess.getoutput(" Deployment Name or Image Name is missing")

else:
        cmd2 = "kubectl scale deployment {0} --replicas {1}".format(dname,scale)
        output2 = subprocess.getoutput(cmd2)

print(output2)

 