from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

# Change to the directory containing the HTML file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create and start the server
def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Server running at http://localhost:8000")
    print("Open your web browser and go to: http://localhost:8000/HTML%20Hello%20World%20Phase3.html")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server() 