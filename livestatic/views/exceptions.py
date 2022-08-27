

class Viewexception(Exception):
    def __init__(self,message=""):
        self.message=message
        print(message)


class Error404(Viewexception):
    def __init__(self, message=""):
        super().__init__(message)

class Error403(Viewexception):
    def __init__(self, message=""):
        super().__init__(message)
    