# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
from importlib.resources import path
import sys
import time
import mimetypes

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
        if path=="/":
            self.send_response(200)
            self.end_headers()
            self.send_header("Content-type", "text/html")
            contentfile = open("index.html", 'rb').read()
            self.wfile.write(contentfile)

        else:
            print("yo")
            imgname = self.path
            imgname = imgname[1:]
            imgfile = open(imgname, 'rb').read()
            mimetype = mimetypes.MimeTypes().guess_type(imgname)[0]
            self.send_response(200)
            self.send_header('Content-type', 'image')
            self.end_headers()
            self.wfile.write(imgfile)


"""this function lauch the server"""
def runserver(hostname,port:int):
    webserver = HTTPServer((hostname,port),MyServer)
    print("Server started http://%s:%s" % (hostname, port))
    try:
       webserver.serve_forever()
    except:
        pass
    webserver.server_close()
    print("Server stopped.")

          
def launch():
    if(sys.argv.__len__()==1):
        runserver("localhost",8000)
        print("yo")
    else:
       
        if sys.argv.__len__()>  1:
            if sys.argv[1] in commands.keys(): 
                c=sys.argv[1]
                sys.argv.pop(0)
                commands[c]()
        


addcommand("runserver",runserverwithargs)
    
        

if __name__ == "__main__":        
    launch()