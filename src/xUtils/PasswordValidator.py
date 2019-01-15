'''
Class:      PasswordValidator
Author(s):  Sam Badger
Date:       January 14, 2019
Description:
            This tool is used for validating passwords.
'''

from xExceptions.PasswordError import PasswordError

class PasswordValidator:
    def __init__(self, password, confirmation=None, silent=False):
        '''
        password     - What we want to validate
        confirmation - supposed to match password if provided. If it does not match
                       an exception is raised.
        silent       - If True, we'll catch any PasswordError exceptions and store 
                       them for retrieval later.
                       If False, all raised exceptions will go unhandled.
        '''
        self._password = password
        self._confirmation = confirmation
        self._silent = silent
        
        self._exceptions = []
        self.validate()
        
    def validate(self):
        self._exceptions = []
        
        checkFns = [self._checkCapitalLetter,
                    self._checkNumber,
                    self._checkConfirmationMatches,
                    self._checkLength,
                    self._checkStrength]
        for fn in checkFns:
            try:
                fn()
            except PasswordError as e:
                self._exceptions.append(e)
                if not self._silent:
                    raise e
            except Exception as e:
                self._exceptions.append(e)
                raise e
                
    def _checkCapitalLetter(self):
        if re.search('[A-Z]', self._password) is None: 
            raise PasswordError("Password must have at least one capital letter.")
            
    def _checkNumber(self):
        if re.search('[1-9]', self._password) is None:
            raise PasswordError("Password must contain at least one number")
            
    def _checkConfirmationMatches(self):
        if self._confirmation == None:
            return
            
        if self._password != self._confirmation:
            raise PasswordError("Passwords don't match")
            
    def _checkLength(self):
        if len(password) < 8:
            raise PasswordError("Password must be at least 8 characters long.")
            
        if len(password) > 32:
            raise PasswordError("Password must be no more than 32 characters long.")
        
    def _checkStrength(self):
        pass
        
    def setPassword(self, password, confirmation=None):
        self._password = password
        self._confirmation = confirmation
        self._exceptions = []
        
    def setSilent(self, silent):
        self._silent = silent
        
    def password(self):
        return self._password
        
    def silent(self):
        return self._silent
        
    def exceptions(self):
        return self._exceptions
        
    def numExceptions(self):
        return len(self._exceptions)
