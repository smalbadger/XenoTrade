'''
Class:      UsernameValidator
Author(s):  Sam Badger
Date:       January 14, 2019
Description:
            This tool is used for validating usernames.
'''

from xExceptions.UsernameError import UsernameError

class UsernameValidator:
    def __init__(self, username, silent=False):
        '''
        username -  What we want to validate
        silent   -  If True, we'll catch any UsernameError exceptions and store 
                    them for retrieval later.
                    If False, all raised exceptions will go unhandled.
        '''
        self._username = username
        self._silent = silent
        
        self._exceptions = []
        self.validate()
        
    def validate(self):
        self._exceptions = []
        
        checkFns = [self._checkAvailability,
                    self._checkCapitalLetter,
                    self._checkLength]
        for fn in checkFns:
            try:
                fn()
            except UsernameError as e:
                self._exceptions.append(e)
                if not self._silent:
                    raise e
            except Exception as e:
                self._exceptions.append(e)
                raise e
                
    def _checkAvailability(self):
        if self._username in UserDB().getUserList():
            raise UsernameError("Username already taken.")
            
    def _checkCapitalLetter(self):
        if re.search('[A-Z]', self._username) is None: 
            raise UsernameError("Username must have at least one capital letter.")
            
    def _checkLength(self):
        if len(username) < 2:
            raise UsernameError("Username must be at least 2 characters long.")
            
        if len(username) > 32:
            raise UsernameError("Username must be no more than 32 characters long.")
        
    def setUsername(self, username):
        self._username = username
        self._exceptions = []
        
    def setSilent(self, silent):
        self._silent = silent
        
    def username(self):
        return self._username
        
    def silent(self):
        return self._silent
        
    def exceptions(self):
        return self._exceptions
        
    def numExceptions(self):
        return len(self._exceptions)
