import os
import subprocess
import sys

def main():
    print("Starting Hermes Gateway for Telegram on Render...")
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if token:
        print("Telegram Bot Token loaded successfully.")
    
    try:
        # Dùng lệnh 'gateway run' để chạy trực tiếp trên foreground, tránh lỗi systemd
        subprocess.run(["hermes", "gateway", "run"], check=True)
    except Exception as e:
        print(f"Error running hermes gateway: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
