import http
from importlib.resources import path
from colorama import Fore,init# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
from cefpython3 import cefpython as cef
import sys
import time
import mimetypes
import os
import threading
import platform
init()
_urldata={

}

_namebind={

}
def  add(url:str,view,name=None):
    _namebind[name]=url
    _urldata[url]=view


def default_index_view():
    return """
    <h1>thanks for using </h1>
    """.encode()
add("/",default_index_view)

def view():
    return render("index.html")
add("/junior",view)
commands={}#list of command
template={
   "directories":["cc"] 
}


def render(htmlfile):
    for dir in template["directories"]:
        tdir=os.path.join(dir,htmlfile)
        print(tdir)
        if  os.path.exists(tdir):
            file=open(tdir, "rb")
            print("yoll")
            filestream=file.read()
            return filestream
    




def runserverwithargs():
    if sys.argv[1]:
        servedata=sys.argv[1].split(":")
        print(servedata)
        runserver(servedata[0],int(servedata[1]))


def addcommand(commandname:str,operation):
    """
    This function adds a command to the server.
    """
    commands[commandname]=operation
class MyServer(BaseHTTPRequestHandler):
    """server class"""    
    def do_GET(self):
        mimetype = mimetypes.MimeTypes().guess_type(self.path)[0]
        print(mimetype);
        if(mimetype!=None ):
            filename = self.path[1:]
            if os.path.exists(filename):
                filestream=open(filename).read()
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(filestream)
                print(Fore.GREEN+"success")
            else:
                self.send_response(400)
                print(Fore.YELLOW+"bad request : cannot find file %s" %filename)
                
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            httpcontent=str()
            if  self.path in _urldata.keys():
                print("yo")
                httpcontent=_urldata[self.path]()

            self.end_headers()
            self.wfile.write(httpcontent)

            print("hey")

        print(Fore.RESET)

def main(url):
    check_versions()
    sys.excepthook = cef.ExceptHook   
    cef.CreateBrowserSync(url=url,
                          window_title="",)
    cef.MessageLoop()
    cef.Shutdown()


def check_versions():
    ver = cef.GetVersion()
    print("[hello_world.py] CEF Python {ver}".format(ver=ver["version"]))
    print("[hello_world.py] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[hello_world.py] CEF {ver}".format(ver=ver["cef_version"]))
    print("[hello_world.py] Python {ver} {arch}".format(
           ver=platform.python_version(),
           arch=platform.architecture()[0]))
    assert cef.__version__ >= "57.0", "CEF Python v57.0+ required to run this"

def runserver(hostname,port):
    """this function lauch the server"""
    webserver = HTTPServer((hostname,port),MyServer)
    print("%d/%d/%d\n" %(time.localtime().tm_year,time.localtime().tm_mon,time.localtime().tm_mday)
        ,"Server started http://%s:%s" % (hostname, port))
    try:
       webserver.serve_forever()
    except:
        pass
    webserver.server_close()
    print("Server stopped.")


def launch(localhost="localhost",port=8000):

    if(sys.argv.__len__()==1):
        serve = threading.Thread(target=runserver, args=(localhost,port))
        serve.start()
        print("server is launch")
        #main("localhost:8000")
        serve.join()
    else:
       
        if sys.argv.__len__()>  1:
            if sys.argv[1] in commands.keys(): 
                c=sys.argv[1]
                sys.argv.pop(0)
                commands[c]()


addcommand("runserver",runserverwithargs)
    
if __name__ == "__main__":        
    launch()