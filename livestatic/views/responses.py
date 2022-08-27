

import mimetypes
import os
import config
from views import exceptions 


class response():
    def __init__(self,contenttype:str,data):
        self.TYPE=contenttype
        e=False
        for dir in config.template["directories"]:
            tdir=os.path.join(dir,data)
            if  os.path.exists(tdir):
                file=open(tdir, "rb")
                filestream=file.read()
                self.content=filestream
                e=True
                break
        if not e:
            raise exceptions.Error404("cannot find template")

        
class htmlresponse(response):
    def __init__(self,data):
        super().__init__(mimetypes.types_map[".html"],data)
    
class jsonresponse(response):
    def __init__(self,data):
        super().__init__(mimetypes.types_map[".json"],data)
class pngresponse(response):
    def __init__(self,data):
        super().__init__(mimetypes.types_map[".png"],data)

class svgresponse(response):
    def __init__(self,data):
        super().__init__(mimetypes.types_map[".svg"],data)



