# -*- coding: utf-8 -*-
# CoreException
class CoreException(RuntimeError):
    """ Core Error """

class CoreError(CoreException):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)

# DatabaseException
class DatabaseException(RuntimeError):
    """ DatabaseError """

class DatabaseError(DatabaseException):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)