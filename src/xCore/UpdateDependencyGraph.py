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

from xCore.abstract.XenoObject import XenoObject

class UpdateDependencyGraph(XenoObject):

    def __init__(self, kernel):
        XenoObject.__init__(self)
        self.setKernel(kernel)
        self.resetUpdateGraph()

    def __del__(self):
        pass
        
    def __str__(self):
        return "UpdateDependencyGraph"
        
    ###############################################################################
    #                                GETTERS
    ###############################################################################
    def getUpdateGraphRoots(self):
        logging.debug("Getting all update graph root nodes")
        return self._updatableRoots
        
    def getKernel(self):
        logging.debug("Getting the UpdateManager's kernel")
        return self._kernel
    
    ###############################################################################
    #                                SETTERS
    ###############################################################################
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
        
    def setRunStatus(self, status):
        logging.debug("Setting run status: {}".format(status))
        self._runStatus = status
        
    def setKernel(self, kernel):
        logging.debug("Setting the UpdateManager's kernel")
        self._kernel = kernel
    
    ###############################################################################
    #                           FUNCTIONAL METHODS
    ###############################################################################
    
    def on_nodeUpdateComplete(self, updated):
        print("recieved response: {}".format(updated))
        self.waiting = False
        self.updated = updated
    
    def run(self):
        try:
            logging.debug("Updating all updatables... (continuous)")
            self.printAllUpdatables()
            self.setRunStatus(True)
            workQueue = queue.Queue()    
            while(self.getRunStatus()):
                for node in self.getUpdateGraphRoots():
                    workQueue.put(node)
                while not workQueue.empty():
                    node = workQueue.get()
                    
                    try:
                        self.updateStart.disconnect()
                    except:
                        pass
                        
                    #updated = node.runUpdates()
                    self.waiting = True
                    self.updated = False
                    self.updateStart.connect(node.runUpdates)
                    
                    node.updateComplete.connect(self.on_nodeUpdateComplete)
                    print("sending signal to update {}".format(node))
                    self.updateStart.emit()
                    
                    while self.waiting:
                        pass
                        
                    node.updateComplete.disconnect()
                    
                    print("did we update? {}".format(self.updated))
                    logging.debug("Did we update? {}".format(self.updated))
                    if self.updated:
                        for child in node.getChildren():
                            workQueue.put(child)
        except Exception as e:
            print(e)
                      
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
