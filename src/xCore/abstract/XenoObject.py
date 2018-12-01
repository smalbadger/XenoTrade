import threading
import logging
'''
    This class should be inherited by any class that will be accessed in multiple threads.
    It allows us to limit the reading and writing priviledges between threads.
'''

class XenoObject():
    def __init__(self):
        self.locks = {}
    
    def addLock(self, name):
        if name in self.locks:
            pass
        self.locks[name] = threading.RLock()
    
    def acquireLock(self, name):
        if name not in self.locks:
            self.addLock(name)   
        self.locks[name].acquire()
        
    def releaseLock(self, name):
        if name not in self.locks:
            return 
        self.locks[name].release()
        
    def releaseAllLocks(self):
        for lock in self.locks:
            self.releaseLock(lock)
            
    def printThread(self):
        print("Thread of {:20}:{}({})".format(self.__str__(), threading.currentThread().getName(), threading.get_ident()))
    
