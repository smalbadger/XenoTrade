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

import xCore.GlobalSettings as GS
from xCore.User import User
from xCore.TaskManager import TaskManager
from xCore.UpdateManager import UpdateManager
from xCore.abstract import XenoObject

class Kernel(XenoObject):
    def __init__(self, app, user=None):
        logging.info("Initializing the XenoTrade kernel")
        XenoObject.__init__(self)

        self.setApp(app)
        self.setCurrentUser(user)
        self.setTaskManager(TaskManager(self, GS.NUM_THREADS, GS.NUM_PROCESSES))
        self.setUpdateManager(UpdateManager(self))
        
    def __del__(self):
        pass
        
    def __str__(self):
        pass
        
    def getTaskManager(self):
        return self.taskManager
    
    ###############################################################################
    #                                GETTERS
    ###############################################################################
    def getApp(self):
        return self._app
        
    def getCurrentUser(self):
        return self._currentUser
        
    def getTaskManager(self):
        return self._taskManager
        
    def getUpdateManager(self):
        return self._updateManager
        
    def getBaseDir(self):
        return os.getcwd().replace('\\','/')[:-3]
        
    def getUsersDir(self):
        return self.getBaseDir() + 'Users/'
        
    def getAllUsers(self):
        logging.debug("Getting a list of all users on this machine.")
        users = os.listdir(self.getUsersDir())
        users.remove('.__template__')
        if users == None:
            users = []
        return users
    
    ###############################################################################
    #                                SETTERS
    ###############################################################################
    def setApp(self, app):
        logging.debug("Setting the kernel's application.")
        self._app = app
        
    def setCurrentUser(self, user):
        logging.info("Setting the kernel's current user.")
        self._currentUser = user
        
    def setTaskManager(self, taskManager):
        logging.debug("Setting the kernel's task manager.")
        self._taskManager = taskManager
        
    def setUpdateManager(self, updateManager):
        logging.debug("Setting the kernel's update manager.")
        self._updateManager = updateManager
        
        
    ###########################################################################
    #                          USER MANAGEMENT METHODS
    ###########################################################################
    def switchUser(self, username, password):
        logging.info("Attempting to switch user to {}.".format(username))
        newUser = User(self, self.getUsersDir() + username + '/')
        if newUser.verify(password):
            self.setCurrentUser(newUser)
        logging.info("Current user: {}".format(self.getCurrentUser()))
        return self.getCurrentUser() == newUser
        
    
    def addUser(self, username, password):
        logging.info("Attempting to add user {}.".format(username))
        if self.switchUser(username, password):
            template = self.getUsersDir() + '.__template__/'
            newUserDir = self.getUsersDir() + username + '/'
            os.mkdir(newUserDir)
            copy_tree(template, newUserDir)
            logging.info("User {} was successfully created".format(username))
        else:
            logging.info("creation of user {} failed.".format(username))
        
        
    def userExists(self, user):
        logging.debug("Checking for {} in the current users.".format(user))
        if user in self.getAllUsers():
            logging.debug("{} was found".format(user))
            return True
        logging.debug("{} was not found".format(user))

if __name__ == '__main__':
    k = Kernel()
    print("-------------------------- KERNEL PROPERTIES --------------------------")
    print("baseDir:      {}".format(k.getBaseDir()))
    print("usersDir:     {}".format(k.getUsersDir()))
    print("App:          {}".format(k.getApp()))
    print("curUser:      {}".format(k.getCurrentUser()))
    print("task manager: {}".format(k.getTaskManager()))
    print("getAllUsers:  {}".format(k.getAllUsers()))
