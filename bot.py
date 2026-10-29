import os
import subprocess
import sys
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# Tạo một server web giả lập để Render nhận diện có port mở (tránh bị lỗi timeout)
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_dummy_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    print(f"Dummy web server running on port {port}")
    server.serve_forever()

def main():
    print("Starting Hermes Gateway for Telegram on Render...")
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if token:
        print("Telegram Bot Token loaded successfully.")
    
    # Chạy web server giả lập ở một luồng riêng (background thread)
    t = threading.Thread(target=run_dummy_server, daemon=True)
    t.start()
    
    # Chạy lệnh gateway của Hermes
    try:
        subprocess.run(["hermes", "gateway", "run"], check=True)
    except Exception as e:
        print(f"Error running hermes gateway: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
