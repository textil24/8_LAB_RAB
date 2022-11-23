from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader
from users import get_users_in_bytes
import time

HOST = "localhost"
PORT = 2000
PATH = 'templates/layout.html'.split('/')

def load_templates(users):
    env = Environment(loader=FileSystemLoader(PATH[0]))
    template = env.get_template(PATH[1])

    return template.render(name=users)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        users = get_users_in_bytes()

        self.wfile.write(bytes(load_templates(users), "utf-8"))

    # def do_POST(self):
    #     self.send_response(200)
    #     self.send_header("Content-type", 'application/json')
    #     self.end_headers()

    #     date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    #     self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
print("Server now running...")

server.serve_forever()
server.server_close()
print("server stop!")