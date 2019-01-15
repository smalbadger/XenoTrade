'''
Class:      PasswordError
Author(s):  Sam Badger
Date:       January 14, 2019
Description:
            Throw this exception when there is a problem with a password
'''

class PasswordError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
        
