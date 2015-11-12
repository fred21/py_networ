import os    
import signal    


pid_s=raw_input("type pid:")
pid=int(pid_s)
     
os.kill(pid,signal.SIGTERM)    

