'''
Class:      UpdateManager
Author(s):  Sam Badger
Date:       October 20, 2018
Description:
            The Update Manager class allows us to keep track of all objects in XenoTrade and update
            them appropriately.
            
How it works:
            Each updatable object has a list of parents and children. The parents of an updatable
            object (current) are other updatable objects that need to be updated BEFORE current can 
            be updated. The children are objects that should be updated IF current gets updated.
            Note that each updatable object can have multiple parents, so this isn't a dependency
            tree, but is a DEPENDENCY GRAPH. This graph should also follow the properties of a DAG
            (Directed Acyclic Graph)
            
            If an updatable object has no parents, it is considered to be a ROOT. In this sense, we
            treat the graph as a bunch of overlapping trees. To do the updating, we iterate over all
            of the root nodes and perform a breadth-first search where we update a nodes children if
            and only if the node has been updated.
'''
import queue
import logging

from xCore.abstract.XenoObject import XenoObject

class UpdateManager(XenoObject):
    def __init__(self, kernel):
        XenoObject.__init__(self)
        
        self.setKernel(kernel)
        self.resetUpdateGraph()

    def __del__(self):
        pass
        
    def __str__(self):
        return ""
        
    ###############################################################################
    #                                GETTERS
    ###############################################################################
    def getUpdateGraph(self):
        logging.debug("Getting all update graph root nodes")
        return self._updatableRoots
        
    def getRunStatus(self):
        logging.debug("Getting run status")
        return self._runStatus
        
    def setKernel(self):
        logging.debug("Getting the UpdateManager's kernel")
        return self._kernel
    
    ###############################################################################
    #                                SETTERS
    ###############################################################################
    def addUpdatable(self, newUpdatable):
        if newUpdatable.getParents() == []:
            logging.debug("Adding new updatable to the update graph as ROOT")
            self.getUpdateGraph().append(newUpdatable)
        else:
            logging.debug("Adding new updatable to the update graph as CHILD")
            for parent in newUpdatable.getParents():
                parent.addChild(newUpdatable)
    
    def resetUpdateGraph(self):
        logging.debug("Resetting the update graph.")
        self._updatableRoots = []
        
    def setRunStatus(self, status):
        logging.debug("Setting run status: {}".format(status))
        self._runStatus = status
        
    def setKernel(self, kernel):
        logging.debug("Setting the UpdateManager's kernel")
        self._kernel = kernel
    
    ###############################################################################
    #                           FUNCTIONAL METHODS
    ###############################################################################
    def updateAllUpdatables(self):
        logging.debug("Updating all updatables... (continuous)")
        self.setRunStatus(True)
        workQueue = queue.Queue()    
        while(self.getRunStatus()):
            for node in self.getUpdateGraph():
                workQueue.put(node)
            while not workQueue.empty():
                node = workQueue.get()
                updated = node.update()
                if updated:
                    for child in node.children():
                        workQueue.put(child)
                
