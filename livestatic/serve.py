from colorama import Fore,init# Python 3 server example
from http.server import  BaseHTTPRequestHandler, HTTPServer
from views import responses,exceptions
import webapp

import config
import sys
import time
import mimetypes
import os
import threading
import urls

init()

def default_index_view():
    
    return responses.htmlresponse("index.html")

urls.add("/",default_index_view)

commands={}#list of command


def addcommand(commandname:str,operation):
    """
    This function adds a command to the server.
    """
    commands[commandname]=operation
class defaultserver(BaseHTTPRequestHandler):
    """server class"""    
    def do_GET(self):
        
        mimetype = mimetypes.MimeTypes().guess_type(self.path)[0]
        if(self.path not in urls._urldata.keys() ):
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
                
        elif self.path in urls._urldata.keys():
            try:
                self.send_response(200)
                response=urls._urldata[self.path]()
                self.send_header("Content-type", response.TYPE)
                self.end_headers()
                self.wfile.write(response.content)
            except exceptions.Error404 as error:
                self.send_response(400)
                print(Fore.YELLOW+"bad request")
            except exceptions.Error403 as error:
                self.send_response(300)
                print(Fore.RED+"access denied")


        print(Fore.RESET)

def runserver(hostname,port):
    #launch server
    webserver = HTTPServer((hostname,port),defaultserver)
    print("%d/%d/%d\n"%(time.localtime().tm_year,time.localtime().tm_mon,time.localtime().tm_mday)
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
        if config.make_app:
            
            webapp.runwebapp("%s:%s"%(localhost,port))
        serve.join()
    else:
       
        if sys.argv.__len__()>  1:
            if sys.argv[1] in commands.keys(): 
                c=sys.argv[1]
                sys.argv.pop(0)
                commands[c]()
    
if __name__ == "__main__":        
    launch()