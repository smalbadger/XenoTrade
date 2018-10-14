import os
import time
from datetime import datetime
from distutils.dir_util import copy_tree

import logging

import GlobalSettings as GS
from User import User
from TaskManager import TaskManager

class Kernel:
    def __init__(self, app, user=None):
        logging.info("Initializing the XenoTrade kernel")
        self.app = app
        self.currentUser = user
        self.taskManager = TaskManager(GS.NUM_THREADS, GS.NUM_PROCESSES)
        self.baseDir     = os.getcwd().replace('\\','/')[:-3]
        self.usersDir    = self.baseDir + 'Users/'
        self.curUser     = None
        
    def __del__(self):
        pass
        
    def __str__(self):
        pass
        
    def getTaskManager(self):
        return self.taskManager
        
        
    ###########################################################################
    #####                           USER METHODS                          #####
    ###########################################################################
    def switchUser(self, username, password):
        logging.info("Attempting to switch user to {}.".format(username))
        newUser = User(self, self.usersDir + username + '/')
        if newUser.verify(password):
            self.curUser = newUser
            logging.info("Current user: {}".format(self.curUser))
            return True
        else:
            logging.info("Current user: {}".format(self.curUser))
            return False
        
    def getAllUsers(self):
        logging.debug("Getting a list of all users on this machine.")
        users = os.listdir(self.baseDir + 'Users/')
        users.remove('.__template__')
        if users == None:
            users = []
        return users
        
    def currentUser(self):
        logging.debug("Fetching the current user")
        return self.curUser
    
    def addUser(self, username, password):
        logging.info("Attempting to add user {}.".format(username))
        err = self.switchUser(username, password)
        if err:
            logging.error(err)
            return err
        else:
            template = self.usersDir + '.__template__/'
            newUserDir = self.usersDir + username + '/'
            os.mkdir(newUserDir)
            copy_tree(template, newUserDir)
            logging.info("User {} was successfully created".format(username))
        
        
    def userExists(self, user):
        logging.debug("Checking for {} in the current users.".format(user))
        if user in self.getAllUsers():
            logging.debug("{} was found".format(user))
            return True
        logging.debug("{} was not found".format(user))

        
if __name__ == '__main__':
    k = Kernel()
    print("-------------------------- KERNEL PROPERTIES --------------------------")
    print("baseDir: {}".format(k.baseDir))
    print("getAllUsers: {}".format(k.getAllUsers()))
