from time import sleep
from datetime import datetime
 
 
class Sleeper:
    def __init__(self, secs):
        self.__secs = secs
 
    def __call__(self, fn):
        def wrapped(*args, **kwargs):
            #print(*args,**kwargs)
            sleep(self.__secs)
            return fn(*args, **kwargs)
 
        return wrapped
 
 
@Sleeper(10)
def  send_message(name):
    print("Hi {}, it is now: {}".format(name, datetime.now()))
 
for x in range(5):
    send_message("Important")
    
    
    
    
    
    
    