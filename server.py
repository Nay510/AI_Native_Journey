#!/usr/bin/env python3
"""
Simple HTTP server to host the Recipe Remix Master
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

def start_server():
    """Start the HTTP server to host the Recipe Remix Master"""
    
    # Get the current directory
    current_dir = Path(__file__).parent.absolute()
    
    # Change to the current directory
    os.chdir(current_dir)
    
    # Set up the server
    PORT = 8000
    
    # Create a custom handler to serve the HTML file
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.path = '/recipe-remix-master.html'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
    
    # Create the server
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print("🌐 Recipe Remix Master Server Started!")
        print(f"📱 Local URL: http://localhost:{PORT}")
        print(f"🌍 Network URL: http://0.0.0.0:{PORT}")
        print("\n📋 Features Available:")
        print("• Find recipes by ingredients")
        print("• Get random recipes")
        print("• Transform recipes to world cuisines")
        print("• Remix recipes with modifications")
        print("\n💡 To access from other devices on your network:")
        print("1. Find your computer's IP address")
        print("2. Use: http://[YOUR_IP]:8000")
        print("\n🔄 Press Ctrl+C to stop the server")
        
        # Open the browser automatically
        try:
            webbrowser.open(f'http://localhost:{PORT}')
        except:
            print(f"\n🌐 Please open your browser and go to: http://localhost:{PORT}")
        
        # Start serving
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Server stopped. Goodbye!")

if __name__ == "__main__":
    start_server() 