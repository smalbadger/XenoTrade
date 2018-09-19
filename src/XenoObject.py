from threading import Lock
import logging
'''
    This class should be inherited by any class that will be accessed in multiple threads.
    It allows us to limit the reading and writing priviledges between threads.
'''

class XenoObject():
    def __init__(self):
        logging.debug("Initializing underlying Xeno Object")
        self.locks = {}
        self.xeno_AddLock('readLock')
        self.xeno_AddLock('writeLock')
    
    def xeno_AddLock(self, name):
        logging.debug("Adding new lock to the the Xeno Object: {}".format(name))
        if name in self.locks:
            logging.warning("{} lock already exists.".format(name))
        self.locks[name] = Lock()
    
    def xeno_Lock(self, name):
        logging.info("Acquiring the {} lock.".format(name))
        if name not in self.locks:
            self.addLocks(name)   
        self.locks[name].acquire()
        
    def xeno_LockForReading(self):
        logging.debug("Locking the XenoObject for reading.")
        self.locks['writeLock'].acquire() # lock writing priviledges
        
    def xeno_LockForWriting(self):
        logging.debug("Locking the XenoObject for writing.")
        self.locks['readLock'].acquire() # lock reading priviledges
        
    def xeno_UnlockAll(self):
        logging.debug("Unlocking all Xeno locks.")
        for lock in self.locks:
            if self.locks[lock].locked():
                self.locks[lock].release()
                    
    def xeno_Unlock(self, name):
        logging.debug("Unlocking Xeno lock: {}".format(name))
        if name in self.locks:
            if self.locks[name].locked():
                self.locks[lock].release()
        else:
            logging.error('ERROR: {} lock does not exist.'.format(name))
                 
            
