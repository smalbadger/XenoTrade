from threading import RLock
import logging
'''
    This class should be inherited by any class that will be accessed in multiple threads.
    It allows us to limit the reading and writing priviledges between threads.
'''

class XenoObject():
    def __init__(self):
        logging.debug("Initializing underlying Xeno Object")
        self.locks = {}
    
    def addLock(self, name):
        logging.debug("Adding new lock to the the Xeno Object: {}".format(name))
        if name in self.locks:
            logging.warning("{} lock already exists.".format(name))
        self.locks[name] = RLock()
    
    def acquireLock(self, name):
        logging.info("Acquiring the {} lock.".format(name))
        if name not in self.locks:
            logging.warning("{} lock does not exist. Creating a new lock and acquiring it.".format(name))
            self.addLock(name)   
        self.locks[name].acquire()
        
    def releaseLock(self, name):
        logging.info("Releasing the {} lock.".format(name))
        if name not in self.locks:
            logging.error("{} lock does not exist, so it cannot be released. check your lock names")
            return 
        self.locks[name].release()
        
    def releaseAllLocks(self):
        logging.info("Releasing all locks")
        for lock in self.locks:
            self.releaseLock(lock)
            
            
