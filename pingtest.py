import os
import re
import time
from subprocess import *
import threading

ip_magic=r'^\s*?Pinging\s*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
status_magic=r'\s*?Packets:\s*?Sent\s*?=\s*?(\d),\s*?Received\s*?=\s*?(\d),\s*?Lost\s*?=\s*?(\d)'

def test_ping():
	procs=[]
	result=[]
	pa_ip=re.compile(ip_magic)
	pa_status=re.compile(status_magic)
	for ip_4 in range(101,255):
		ping_cmd='ping -n 4 10.118.4.%s'%(str(ip_4))
		p=Popen(ping_cmd,stdout=PIPE,stderr=PIPE)
		procs.append(p)

	for p in procs:
		p.wait();
		out=p.stdout.read()
		if out == '':
			print "none."
			continue
		print out
		ip=pa_ip.findall(out)
		status=pa_status.findall(out)
		if len(status) == 0:
			continue
		result.append(ip)
		result[-1:][-1].append(status[0])

	for d in result:
		print d

test_ping()
