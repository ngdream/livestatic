import sys
from cefpython3 import cefpython as cef
def runwebapp(url):
    sys.excepthook = cef.ExceptHook   
    cef.CreateBrowserSync(url=url,
                          window_title="",)
    cef.MessageLoop()
    cef.Shutdown()