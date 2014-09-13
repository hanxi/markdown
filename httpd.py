#!/usr/bin/python
# coding : utf-8

import os
import sys
import BaseHTTPServer

wwwpath = sys.argv[1]

actions = {
    "/editor":"/html/editor.html",
    "/":"/html/index.html",
}

class WebRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        fn = self.path
        if self.path in actions.keys():
            fn = "%s%s" % (wwwpath, actions[self.path])
        else:
            fn = "%s%s" % (wwwpath, self.path)

        fn = fn.replace("/",os.sep)
        print(fn)

        self.send_response(200)
        if fn[-3:]==".js":
            self.send_header("Content-type","application/x-javascript")
        elif fn[-4:]==".css":
            self.send_header("Content-type","text/css")
        self.end_headers()

        if os.path.isfile(fn):
            self.wfile.write(open(fn, "rb").read())
        else:
            self.wfile.write("")

server = BaseHTTPServer.HTTPServer(("0.0.0.0", 8080), WebRequestHandler)
server.serve_forever()

