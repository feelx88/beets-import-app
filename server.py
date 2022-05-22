from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import os.path
import shutil
import cgi
import string
import tempfile
import argparse


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(index)

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type'],
            }
        )

        with tempfile.TemporaryDirectory() as tempDir:
            zipFileName = '{0}/upload.zip'.format(tempDir)
            with open(zipFileName, mode='wb') as file:
                file.write(form['file'].file.read())

            shutil.unpack_archive(zipFileName, tempDir)
            os.remove(zipFileName)

            os.system('beet import {0}'.format(tempfile.tempdir))

        self.send_response(200)
        self.end_headers()


with open('index.html', mode='rb') as file:
    index = file.read()

parser = argparse.ArgumentParser(description='beets import ui backend.')
parser.add_argument('--ip',  type=str, default='127.0.0.1',
                    help='IP address to bind the server to (default: 127.0.0.1)')
parser.add_argument('--port', type=int, default=18888,
                    help='Port to bind the server to (default: 18888)')

args = parser.parse_args()

httpd = HTTPServer((args.ip, args.port), handler)
httpd.serve_forever()
