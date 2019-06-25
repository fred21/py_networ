import os    
import signal    
from time import sleep  

# comment add by hwfred21 2019-6-24 
# comment add by fred21 2019-5-24_2    
# comment add by fred21 2019-5-24_1    
# comment add by fred21 2019-5-24    
# comment add by hwfred21     
#comment : add by fred21 2019-5-23
#comment : add by fred21 2019-6-23
#comment : add by fred21 2019-6-24
#comment : add by fred21 2019-6-24_1
#comment : add by fred21 2019-6-24_2
#comment : add by fred21 2019-6-25

def onsignal_term(a,b):    
	print 'get SIGTERM'    
     
signal.signal(signal.SIGTERM,onsignal_term)    
     

while 1:    
	print 'my pid:',os.getpid()    
	sleep(10)    

