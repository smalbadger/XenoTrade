from threading import Lock
'''
    This class should be inherited by any class that will be accessed in multiple threads.
    It allows us to limit the reading and writing priviledges between threads.
'''

class XenoObject():
    def __init__(self):
        self.locks = {}
        self.xeno_AddLock('readLock')
        self.xeno_AddLock('writeLock')
        
    
    def xeno_AddLock(self, name):
        if name in self.locks:
            print("ERROR: {} lock already exists.".format(name))
        self.locks[name] = Lock()
    
    def xeno_Lock(self, name):
        if name not in self.locks:
            self.addLocks(name)   
        self.locks[name].acquire()
        
    def xeno_LockForReading(self):
        self.locks['writeLock'].acquire() # lock writing priviledges
        
    def xeno_LockForWriting(self):
        self.locks['readLock'].acquire() # lock reading priviledges
        
    def xeno_UnlockAll(self):
        for lock in self.locks:
            if self.locks[lock].locked():
                self.locks[lock].release()
                '''
                try:
                    self.locks[lock].release()
                finally:
                    print('ERROR: could not release lock '.format(lock))
                '''
                    
    def xeno_Unlock(self, name):
        if name in self.locks:
            if self.locks[name].locked():
                self.locks[lock].release()
                '''
                try:
                    self.locks[name].release()
                finally:
                    print('ERROR: could not release lock '.format(name))
                '''
        else:
            print('ERROR: {} lock does not exist.'.format(name))
                 
            
