'''
Class:      UsernameError
Author(s):  Sam Badger
Date:       January 14, 2019
Description:
            Throw this exception when there is a problem with a username
'''

class UsernameError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
        
