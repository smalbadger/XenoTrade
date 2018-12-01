'''
Class:      TaskManager
Author:     Sam Badger
Date:       October 13, 2018
Description:
            This class will manage many tasks that need to be done in Parallel. It is particularly
            useful for making network requests that have a significant delay. To execute a task in
            parallel, you need to decide if it's computationally heavy or a network task. Network
            Tasks are sent to a thread pool, whereas computing tasks are sent to a process pool.
'''
import logging
from time import time
from queue import Queue
from pprint import pprint
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from xCore.abstract.XenoObject import XenoObject

class TaskManager(XenoObject):
    def __init__(self, kernel, numThreads=10, numProcesses=5):
        XenoObject.__init__(self)
        
        self._threadPool = None
        self._processPool = None
        
        self.setKernel(kernel)
        self.setNetworkWorkQueue(Queue())
        self.setNumThreads(numThreads)
        self.setNumActiveThreads(0)
        self.resetThreadPool()
        self.resetNetworkTaskHistory()
        
        self._waitingTasks = {} # PRIVATE- don't touch this (that's why there's no setter or getter)

    def __del__(self):
        pass
        
        
    def __str__(self):
        return ""
    ###############################################################################
    #                                GETTERS
    ###############################################################################
    def getKernel(self):
        self.acquireLock("self._kernel")
        self.releaseLock("self._kernel")
        return self._kernel
        
    
    def getNumActiveThreads(self):
        self.acquireLock("self._activeThreadCounter")
        self.releaseLock("self._activeThreadCounter")
        return self._activeThreadCounter
        
        
    def getNumThreads(self):
        self.acquireLock("self._numThreads")
        self.releaseLock("self._numThreads")
        return self._numThreads
        
        
    def getThreadPool(self):
        self.acquireLock("self._threadPool")
        self.releaseLock("self._threadPool")
        return self._threadPool
        
        
    def getNetworkWorkQueue(self):
        self.acquireLock("self._networkWorkQueue")
        self.releaseLock("self._networkWorkQueue")
        return self._networkWorkQueue
        
    def getNextNetworkTaskFromQueue(self):
        self.acquireLock("self._networkWorkQueue")
        task = self._networkWorkQueue.get()
        self.releaseLock("self._networkWorkQueue")
        return task
        
        
    def getNumUnprocessedNetworkTasks():
        self.acquireLock("self._networkWorkQueue")
        self.releaseLock("self._networkWorkQueue")
        return self._networkWorkQueue.qsize()
        
        
    def getNetworkTaskHistory(self):
        self.acquireLock("self._networkTaskHistory")
        self.releaseLock("self._networkTaskHistory")
        return self._networkTaskHistory

    ###############################################################################
    #                                SETTERS
    ###############################################################################
    def setKernel(self, kernel):
        self.acquireLock("self._kernel")
        self._kernel = kernel
        self.releaseLock("self._kernel")
    
    def setNumActiveThreads(self, num):
        self.acquireLock("self._activeThreadCounter")
        self._activeThreadCounter = num
        self.releaseLock("self._activeThreadCounter")
        
    def incrementNumActiveThreads(self):
        self.acquireLock("self._activeThreadCounter")
        self._activeThreadCounter += 1
        self.releaseLock("self._activeThreadCounter")
        
    def decrementNumActiveThreads(self):
        self.acquireLock("self._activeThreadCounter")
        self._activeThreadCounter -= 1
        self.releaseLock("self._activeThreadCounter")
            
    def setNetworkWorkQueue(self, queue):
        self.acquireLock("self._networkWorkQueue")
        if (type(queue) != Queue):
            pass
        self._networkWorkQueue = queue   
        self.releaseLock("self._networkWorkQueue")
            
    def addNetworkTaskToQueue(self, task):
        self.acquireLock("self._networkWorkQueue")
        self._networkWorkQueue.put(task)
        self.releaseLock("self._networkWorkQueue")
    
    def setNumThreads(self, num):
        self.acquireLock("self._numThreads")
        self._numThreads = num
        self.releaseLock("self._numThreads")
            
    def resetThreadPool(self):
        self.acquireLock("self._threadPool")
        if self._threadPool != None:
            self._threadPool.shutdown()
        max_workers = self.getNumThreads()
        self._threadPool = ThreadPoolExecutor(max_workers=max_workers)
        self.releaseLock("self._threadPool")
    
    def resetNetworkTaskHistory(self):
        self.acquireLock("self._networkTaskHistory")
        self._networkTaskHistory = []
        self.releaseLock("self._networkTaskHistory") 
        
    def addTaskToWaitingList(self, future, task):
        self.acquireLock("self._waitingTasks")
        self._waitingTasks[future] = task
        self.releaseLock("self._waitingTasks")
        
    def retrieveTaskFromWaitingList(self, future):
        self.acquireLock("self._waitingTasks")
        task = self._waitingTasks[future]
        self.releaseLock("self._waitingTasks")
        return task
        
    def removeTaskFromWaitingList(self, future):
        self.acquireLock("self._waitingTasks")
        del self._waitingTasks[future]
        self.releaseLock("self._waitingTasks")
        
        
    def submitTaskToThreadPool(self, task):
        self.acquireLock("self._threadPool")
        future = self.getThreadPool().submit(task["targetFn"], *task["args"], **task["kwargs"])
        self.releaseLock("self._threadPool")
        return future
   
    ###############################################################################
    #                          NETWORK TASK FUNCTIONAL METHODS
    ###############################################################################
    # These methods are working as far as I know.
    
    def addNetworkTask(self, targetFn, callbackFn, *args, **kwargs):
        newTask = {}
        newTask["targetFn"] = targetFn
        newTask["callbackFn"] = callbackFn
        newTask["args"] = args
        newTask["kwargs"] = kwargs
        newTask["start_time"] = time()
        self.addNetworkTaskToQueue(newTask)
        if (self.getNumActiveThreads() < self.getNumThreads()):
            self.feedThreadPool()
            
    def feedThreadPool(self):
        if self.getNetworkWorkQueue().empty():
            return
        task = self.getNextNetworkTaskFromQueue()
        future = self.submitTaskToThreadPool(task)
        print(future)
        self.addTaskToWaitingList(future, task)
        self.incrementNumActiveThreads()
        future.add_done_callback(self.onNetworkTaskCompleted)
        
    def onNetworkTaskCompleted(self, future):
        #self.acquireLock("onNetworkTaskCompleted")
        self.decrementNumActiveThreads()
        if (self.getNumActiveThreads() < self.getNumThreads()):
            self.feedThreadPool()
        task = self.retrieveTaskFromWaitingList(future)
        task["callbackFn"](future)
        task["end_time"] = time()
        self.getNetworkTaskHistory().append(task)
        self.removeTaskFromWaitingList(future)
        #self.releaseLock("onNetworkTaskCompleted")

