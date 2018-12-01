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

from PySide2.QtCore import QThread
from PySide2.QtCore import QObject, Signal

from xCore.abstract.XenoObject import XenoObject

class UpdateManager(QThread, XenoObject):
    updateStart = Signal(int)

    def __init__(self, kernel, updateGraph):
        QThread.__init__(self)
        XenoObject.__init__(self)
        
        self.setUpdateGraph(updateGraph)

    def __str__(self):
        return "UpdateManager"
        
    ############################################################################
    #                                GETTERS
    ############################################################################

    def getRunStatus(self):
        #logging.debug("Getting run status")
        return self._runStatus
        
    def getUpdateGraph(self):
        return self._updateGraph
    ############################################################################
    #                                SETTERS
    ############################################################################

    def setRunStatus(self, status):
        logging.debug("Setting run status: {}".format(status))
        self._runStatus = status
        
    def setUpdateGraph(self, updateGraph):
        logging.debug("Setting update graph")
        self._updateGraph = updateGraph
        self._updateGraph.updateComplete.connect(self.on_nodeUpdateComplete)
        self.updateStart.connect(self._updateGraph.on_updateSignal)
    ############################################################################
    #                           FUNCTIONAL METHODS
    ############################################################################
    def on_nodeUpdateComplete(self, updated):
        print("recieved response: {}".format(updated))
        self.waiting = False
        self.updated = updated
    
    def run(self):
        logging.debug("Updating all updatables... (continuous)")
        roots, matrix = self.getUpdateGraph().getAdjacencyMatrix()
        self.setRunStatus(True)
        workQueue = queue.Queue()    
        while(self.getRunStatus()):
            for nodeID in roots:
                workQueue.put(nodeID)
            while not workQueue.empty():
                nodeID = workQueue.get()
                self.waiting = True
                self.updated = False
                
                self.updateStart.emit(nodeID)
                while self.waiting:
                    pass
                    
                if self.updated:
                    for i in range(len(matrix[nodeID])):
                        if matrix[nodeID][i] == 1:
                            workQueue.put(i)


