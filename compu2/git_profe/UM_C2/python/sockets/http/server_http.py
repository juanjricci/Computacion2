import http.server
import socketserver

PORT = 1234


socketserver.TCPServer.allow_reuse_address = True
myhttphandler = http.server.SimpleHTTPRequestHandler


httpd = socketserver.TCPServer(("", PORT), myhttphandler)

print(f"Opening httpd server at port {PORT}")

httpd.serve_forever()

httpd.shutdown()
