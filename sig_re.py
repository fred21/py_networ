import os    
import signal    
from time import sleep    
# comment add by hwfred21     
def onsignal_term(a,b):    
	print 'get SIGTERM'    
     
signal.signal(signal.SIGTERM,onsignal_term)    
     

while 1:    
	print 'my pid:',os.getpid()    
	sleep(10)    

