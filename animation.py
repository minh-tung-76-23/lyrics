import time
import sys
from colorama import Fore, Style, init

# Khởi tạo Colorama
init(autoreset=True)

def show_each_letter(text, delay):
    for char in text:
        sys.stdout.write(char)  
        sys.stdout.flush()      
        time.sleep(delay)       

def fade_in_text(text, delay, steps=10):
    for i in range(1, steps + 1):
        brightness = int(255 * i / steps)
        color = f"\033[38;2;{brightness};{brightness};{brightness}m" 
        sys.stdout.write(f"\r{color}{text}") 
        sys.stdout.flush()
        time.sleep(delay)

def show_fade_in_and_each_letter(text, delay, steps=10):
    for i in range(1, len(text) + 1):
        # Lấy đoạn văn bản từ đầu đến vị trí hiện tại
        current_text = text[:i]
        
        # Tính độ sáng từ mờ đến rõ
        brightness = int(255 * min(i / len(text), 1) * steps / 10)
        color = f"\033[38;2;{brightness};{brightness};{brightness}m"  # Mã màu RGB

        # In với màu thay đổi và hiển thị từng ký tự
        sys.stdout.write(f"\r{color}{current_text}")
        sys.stdout.flush()
        
        # Chờ giữa các ký tự
        time.sleep(delay)

    print()  # Xuống dòng sau khi hoàn tất

