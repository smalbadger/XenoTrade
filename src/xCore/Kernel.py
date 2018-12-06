'''
Class:      Kernel
Author:     Sam Badger
Date:       October 15, 2018
Description:
            The Kernel is the core of XenoTrade (I don't actually know what a "kernel" is, but the 
            name sounded right). It links the main components of the XenoTrade architecture while
            providing a simple way to access data from most other parts of the architecture.
'''
import os
import logging
from distutils.dir_util import copy_tree

import xCore.Globals as GS

from xCore.User import User
from xCore.TaskManager import TaskManager
from xCore.UpdateManager import UpdateManager
from xCore.UpdateDependencyGraph import UpdateDependencyGraph
from xCore.abstract import XenoObject

class Kernel(XenoObject):
    def __init__(self, user=None):
        XenoObject.__init__(self)

        self.setCurrentUser(user)
        self.setTaskManager(TaskManager(self, GS.NUM_THREADS, GS.NUM_PROCESSES))
        self.setUpdateGraph(UpdateDependencyGraph(self))
        self.setUpdateManager(UpdateManager(self, self.getUpdateGraph()))
        
    def __del__(self):
        pass
        
    def __str__(self):
        pass
        
    ###############################################################################
    #                                GETTERS
    ###############################################################################

    def getCurrentUser(self):
        return self._currentUser
        
    def getTaskManager(self):
        return self._taskManager
        
    def getUpdateManager(self):
        return self._updateManager
        
    def getUpdateGraph(self):
        return self._updateGraph
        
    def getBaseDir(self):
        return os.getcwd().replace('\\','/')[:-3]
        
    def getUsersDir(self):
        return self.getBaseDir() + 'Users/'
        
    def getAllUsers(self):
        users = os.listdir(self.getUsersDir())
        users.remove('.__template__')
        if users == None:
            users = []
        return users
    
    ###############################################################################
    #                                SETTERS
    ###############################################################################

    def setCurrentUser(self, user):
        self._currentUser = user
        
    def setTaskManager(self, taskManager):
        self._taskManager = taskManager
        
    def setUpdateManager(self, updateManager):
        self._updateManager = updateManager
        
    def setUpdateGraph(self, graph):
        self._updateGraph = graph
        
    ###########################################################################
    #                          USER MANAGEMENT METHODS
    ###########################################################################
    def switchUser(self, username, password):
        newUser = User(self, self.getUsersDir() + username + '/')
        if newUser.verify(password):
            self.setCurrentUser(newUser)
            logging.info("User logged in successfully: {}".format(newUser))
            return True
        else:
            logging.info("User login attempt failed: {}".format(newUser))
            return False
        
    
    def addUser(self, username, password):
        logging.info("Creating new user: {}".format(username))
        if self.switchUser(username, password):
            logging.info("User created successfully: {}".format(self.getCurrentUser()))
            template = self.getUsersDir() + '.__template__/'
            newUserDir = self.getUsersDir() + username + '/'
            os.mkdir(newUserDir)
            copy_tree(template, newUserDir)
            return True
        else:
            logging.info("User creation failed: {}".format(username))
            return False
        
    def userExists(self, user):
        if user in self.getAllUsers():
            return True

if __name__ == '__main__':
    k = Kernel()
    print("-------------------------- KERNEL PROPERTIES --------------------------")
    print("baseDir:      {}".format(k.getBaseDir()))
    print("usersDir:     {}".format(k.getUsersDir()))
    print("App:          {}".format(k.getApp()))
    print("curUser:      {}".format(k.getCurrentUser()))
    print("task manager: {}".format(k.getTaskManager()))
    print("getAllUsers:  {}".format(k.getAllUsers()))
