'''
Class:      UpdateDependencyGraph
Author(s):  Sam Badger
Date:       November 29, 2018
Description:
            Keeps dependencies between updatable objects in XenoTrade clear. 
            This is important because if something in the program is updated,
            other things may need to be updated as well, but we don't want to
            update everything. We just want to update when we need to.
            
            This graph should follow all rules and restrictions that a 
            Directed Acyclic Graph should follow (indeed it is a DAG). Some of
            the nodes in the graphs are held as "Roots" - these are nodes that 
            are periodically updated. All other nodes in the graph are updated
            as a result of the roots being updated.
            
            There should be NO CYCLES in the graph.
'''
import queue
import logging
import numpy as np

from PySide2.QtCore import QObject, Signal

from xCore.abstract.XenoObject import XenoObject

class UpdateDependencyGraph(XenoObject, QObject):
    updateComplete = Signal(bool)

    def __init__(self, kernel):
        XenoObject.__init__(self)
        QObject.__init__(self)
        
        self.setKernel(kernel)
        self.resetUpdateGraph()
        

    def __del__(self):
        pass
        
    def __str__(self):
        return "UpdateDependencyGraph"
        
    ############################################################################
    #                                GETTERS
    ############################################################################
    def getUpdateGraphRoots(self):
        logging.debug("Getting all update graph root nodes")
        return self._updatableRoots
        
    def getKernel(self):
        logging.debug("Getting the UpdateManager's kernel")
        return self._kernel
    
    ############################################################################
    #                                SETTERS
    ############################################################################
    def addUpdatable(self, newUpdatable):
        if newUpdatable.getParents() == []:
            logging.debug("Adding new updatable to the update graph as ROOT")
            self.getUpdateGraphRoots().append(newUpdatable)
        else:
            logging.debug("Adding new updatable to the update graph as CHILD")
            for parent in newUpdatable.getParents():
                parent.addChild(newUpdatable)
    
    def resetUpdateGraph(self):
        logging.debug("Resetting the update graph.")
        self._updatableRoots = []
        
    def setKernel(self, kernel):
        logging.debug("Setting the UpdateManager's kernel")
        self._kernel = kernel
    
    ############################################################################
    #                           FUNCTIONAL METHODS
    ############################################################################
    def generateIDMapping(self):
        # create mapping from references to unique IDs
        self._ref_to_id = {}
        self._id_to_ref = {}
        counter = 0
        workQueue = queue.Queue()  
        for node in self.getUpdateGraphRoots():
            workQueue.put(node)
        while not workQueue.empty():
            node = workQueue.get()
            if node not in self._ref_to_id:
                self._ref_to_id[node] = counter
                self._id_to_ref[counter] = node
                counter += 1
            for child in node.getChildren():
                workQueue.put(child)
    
    def getAdjacencyMatrix(self):
        self.generateIDMapping()
    
        # create adjacency matrix
        size = max(self._id_to_ref.keys()) + 1
        self._adjMat = np.zeros((size, size))
        workQueue = queue.Queue()  
        for node in self.getUpdateGraphRoots():
            workQueue.put(node)
        while not workQueue.empty():
            node = workQueue.get()
            fromNode = self._ref_to_id[node]
            for child in node.getChildren():
                toNode = self._ref_to_id[child]
                self._adjMat[fromNode][toNode] = 1
                workQueue.put(child)
        
        #get list of roots
        roots = [self._ref_to_id[root] for root in self.getUpdateGraphRoots()]
        
        return roots, self._adjMat
        
    def toDotFile(self):
        # write graph to dot file for visualization
        pass
                      
    def printAllUpdatables(self):
        logging.info("Printing the Update Dependency Graph")
        print("Printing all nodes in update graph:")
        workQueue = queue.Queue()    
        for node in self.getUpdateGraphRoots():
            workQueue.put(node)
        while not workQueue.empty():
            node = workQueue.get()
            print([node])
            print("    Parents:  {}".format(node.getParents()))
            print("    Children: {}".format(node.getChildren()))
            for child in node.getChildren():
                workQueue.put(child)
                
    ############################################################################
    #                           SLOTS
    ############################################################################
    def on_updateSignal(self, nodeID):   
        nodeToUpdate = self._id_to_ref[nodeID]
        nodeToUpdate.updateComplete.connect(self.on_nodeUpdateComplete)
        nodeToUpdate.runUpdates()
        nodeToUpdate.updateComplete.disconnect()
        
    def on_nodeUpdateComplete(self, updated):
        # slot for signal from the node that's begin updated.
        # just re-emit the signal. It will be caught by the UpdateManager
        self.updateComplete.emit(updated)
        
