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
from queue import Queue
from pprint import pprint
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

from XenoObject import XenoObject

class TaskManager(XenoObject):
    def __init__(self, numThreads=10, numProcesses=5):
        logging.debug("Initializing Task Manager")
        XenoObject.__init__(self)
        
        self._threadPool = None
        self._processPool = None
        
        self.setNetworkWorkQueue(Queue())
        self.setComputationWorkQueue(Queue())
        self.setNumThreads(numThreads)
        self.setNumProcesses(numProcesses)
        self.setNumActiveThreads(0)
        self.setNumActiveProcesses(0)
        self.resetThreadPool()
        self.resetProcessPool()
        
        self._waitingTasks = {} # PRIVATE

    def __del__(self):
        pass
        
        
    def __str__(self):
        return ""
    ###############################################################################
    #                                GETTERS
    ###############################################################################
    def getNumActiveThreads(self):
        logging.debug("Getting number of active threads")
        return self._activeThreadCounter
        
    def getNumActiveProcesses(self):
        logging.debug("Getting number of active processes")
        return self._activeProcessCounter
        
    def getNumThreads(self):
        logging.debug("Getting number of threads")
        return self._numThreads
        
    def getNumProcesses(self):
        logging.debug("Getting number of processes")
        return self._numProcesses
        
    def getThreadPool(self):
        logging.debug("Getting thread pool")
        return self._threadPool
        
    def getProcessPool(self):
        logging.debug("Getting process pool")
        return self._processPool
        
    def getNetworkWorkQueue(self):
        logging.debug("Getting network work queue")
        return self._networkWorkQueue
        
    def getComputationWorkQueue(self):
        logging.debug("Getting computation work queue")
        return self._computingWorkQueue
        
    def getNumUnprocessedNetworkTasks():
        logging.debug("Getting number of unprocessed network tasks")
        return self._networkWorkQueue.qsize()
        
    def getNumUnprocessedComputationTasks():
        logging.debug("Getting number of unprocessed computation tasks")
        return self._computationWorkQueue.qsize()
        
    def getNetworkTaskHistory():
        return self._networkTaskHistory
        
    ###############################################################################
    #                                SETTERS
    ###############################################################################
    def setNumActiveThreads(self, num):
        logging.debug("Setting number of active threads: " + str(num))
        self._activeThreadCounter = num
        
    def setNumActiveProcesses(self, num):
        logging.debug("Setting number of active processes: " + str(num))
        self._activeProcessCounter = num
        
    def setNetworkWorkQueue(self, queue):
        logging.debug("Setting network work queue")
        if (type(queue) != Queue):
            logging.critical("Must provide a Queue to set as the network work queue")
        self._networkWorkQueue = queue
        
    def setComputationWorkQueue(self, queue):
        logging.debug("Setting computation work queue")
        if (type(queue) != Queue):
            logging.critical("Must provide a Queue to set as the computation work queue")
        self._computationWorkQueue = queue
    
    def setNumThreads(self, num):
        logging.info("Setting number of threads in task manager: " + str(num))
        self._numThreads = num
        
    def setNumProcesses(self, num):
        logging.info("Setting number of processes in task manager: " + str(num))
        self._numProcesses = num
    
    def resetThreadPool(self):
        logging.info("Resetting the task manager's thread pool")
        if self.getThreadPool():
            self.getThreadPool().shutdown()
        self._threadPool = ThreadPoolExecutor(max_workers=self.getNumThreads())
        
    def resetProcessPool(self):
        logging.info("Resetting the task manager's process pool")
        if self.getProcessPool():
            self.getProcessPool().shutdown()
        self._processPool = ProcessPoolExecutor(max_workers=self.getNumProcesses())
    
    ###############################################################################
    #                          NETWORK TASK FUNCTIONAL METHODS
    ###############################################################################
    # These methods are working as far as I know.
    
    def addNetworkTask(self, targetFn, callbackFn, *args, **kwargs):
        logging.info("New network task: targetFn="+str(targetFn)+" callbackFn="+str(callbackFn))
        newTask = {}
        newTask["targetFn"] = targetFn
        newTask["callbackFn"] = callbackFn
        newTask["args"] = args
        newTask["kwargs"] = kwargs
        newTask["start_time"] = time()
        self.getNetworkWorkQueue().put(newTask)
        if (self.getNumActiveThreads() < self.getNumThreads()):
            self.feedThreadPool()
            
    def feedThreadPool(self):
        logging.debug("Feeding the thread pool.")
        if self.getNetworkWorkQueue().empty():
            logging.debug("Nothing to feed the thread pool.")
            return
        task = self.getNetworkWorkQueue().get()
        future = self.getThreadPool().submit(task["targetFn"], *task["args"], **task["kwargs"])
        print(future)
        self._waitingTasks[future] = task
        self.setNumActiveThreads(self.getNumActiveThreads()+1)
        future.add_done_callback(self.onNetworkTaskCompleted)
        
    def onNetworkTaskCompleted(self, future):
        logging.debug("Network task completed.")
        self.acquireLock("onNetworkTaskCompleted")
        print(future.result())
        self.setNumActiveThreads(self.getNumActiveThreads()-1)
        if (self.getNumActiveThreads() < self.getNumThreads()):
            self.feedThreadPool()
        self._waitingTasks[future]["callbackFn"](future)
        self._waitingTasks[future]["end_time"] = time()
        self._getNetworkTaskHistory().append(self._waitingTasks[future])
        del self._waitingTasks[future]
        self.releaseLock("onNetworkTaskCompleted")
           
    ###############################################################################
    #                          COMPUTATION TASK FUNCTIONAL METHODS
    ###############################################################################
    # This methods are untested and most likely will not work if you use it, so don't.
    
    def addComputationTask(self, targetFn, callbackFn, *args, **kwargs):
        # Note: only "Picklable" objects can be handed off to a process.
        logging.info("New network task: targetFn="+str(targetFn)+" callbackFn="+str(callbackFn))
        newTask = {}
        newTask["targetFn"] = targetFn
        newTask["callbackFn"] = callbackFn
        newTask["args"] = args
        newTask["kwargs"] = kwargs
        self.getComputationWorkQueue().put(newTask)
        if (self.getNumActiveProcesses() < self.getNumProcesses()):
            self.feedProcessPool()
        
    def feedProcessPool(self):
        logging.debug("Feeding the process pool.")
        task = self.getComputationWorkQueue().get()
        if self.getComputationWorkQueue().empty():
            logging.debug("Nothing to feed the thread pool.")
            return
        future = self.getProcessPool().submit(task["targetFn"], *task["args"], **task["kwargs"])
        self._waitingTasks[future] = task
        self.setNumActiveProcesses(self.getNumActiveProcesses()+1)
        future.add_done_callback(self.onComputationTaskCompleted)
        
    def onComputationTaskCompleted(self):
        logging.debug("Computation task comleted")
        self.acquireLock("onComputationTaskCompleted")
        self.setNumActiveProcesses(self.getNumActiveProcesses()-1)
        if (self.getNumActiveProcesses() < self.getNumProcesses()):
            self.feedProcessPool()
        self._waitingTasks[future]["callbackFn"](future)
        del self._waitingTasks[future]
        self.acquireLock("onComputationTaskCompleted")
