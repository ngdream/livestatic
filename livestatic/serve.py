"""LIve static - mave your developement cool"""

from colorama import Fore,init# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import time
import mimetypes
import os



init()

commands={}#list of command



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
        if(mimetype!=None and mimetype!='text/html'):
            filename = self.path[1:]
            if os.path.exists(filename):
                file=open(filename, "rb") 
                filestream=file.read()
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
            contentfile=str()
            if self.path =="/":
                if os.path.exists("index.html"):
                    contentfile = open("index.html", 'rb').read()
                else:
                    contentfile="""
                <html>

                </html>
                """
            else:
                filename = self.path[1:]
                if os.path.exists(filename):
                    contentfile=open(filename, "rb") .read()
                    self.send_response(200)
                    self.send_header('Content-type','text/html')
                    print(Fore.GREEN+"success")
                else:
                    self.send_response(400)
                    print(Fore.YELLOW+"bad request : cannot find file %s" %filename)
            self.end_headers()
            self.wfile.write(contentfile)

            print("hey")

        print(Fore.RESET)



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


def launch():
    if(sys.argv.__len__()==1):
        runserver("localhost",8000)
    else:
       
        if sys.argv.__len__()>  1:
            if sys.argv[1] in commands.keys(): 
                c=sys.argv[1]
                sys.argv.pop(0)
                commands[c]()


addcommand("runserver",runserverwithargs)
    
if __name__ == "__main__":        
    launch()