import http.server, socketserver
PORT = 8080
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()
with socketserver.TCPServer(("", PORT), H) as httpd:
    print(f"Serving at http://localhost:{PORT} (no-cache)")
    httpd.serve_forever()
