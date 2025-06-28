#!/usr/bin/env python3
"""
Simple HTTP server to host the Recipe Remix Master
"""

import http.server
import socketserver
import os
import socket

def get_local_ip():
    """Get the local IP address of the machine"""
    try:
        # Connect to a remote address to determine local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "127.0.0.1"

def create_server():
    """Create and start the HTTP server"""
    PORT = 8000
    
    # Check if port is in use
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', PORT))
    except OSError:
        print(f"⚠️  Port {PORT} is already in use. Trying to kill existing process...")
        os.system(f"lsof -ti:{PORT} | xargs kill -9")
        print(f"✅ Killed process on port {PORT}")
    
    # Set up the server
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        local_ip = get_local_ip()
        
        print("🌐 Recipe Remix Master Server Started!")
        print(f"📱 Local URL: http://localhost:{PORT}")
        print(f"🌍 Network URL: http://0.0.0.0:{PORT}")
        print(f"💻 Your IP: http://{local_ip}:{PORT}")
        print("📋 Features Available:")
        print("• Find recipes by ingredients")
        print("• Get random recipes")
        print("• Transform recipes to world cuisines")
        print("• Remix recipes with modifications")
        print("• Categories and dietary restrictions sidebar")
        print("💡 To access from other devices on your network:")
        print(f"1. Use: http://{local_ip}:{PORT}")
        print("🔄 Press Ctrl+C to stop the server")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped by user")
            httpd.shutdown()

if __name__ == "__main__":
    create_server() 