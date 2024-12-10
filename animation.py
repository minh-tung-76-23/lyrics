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

# Hàm fade-in cho từng từ
def fade_in_words(text, delay, steps=10):
    words = text.split()  
    for word in words:
        for i in range(1, steps + 1):
            brightness = int(255 * i / steps)
            color = f"\033[38;2;{brightness};{brightness};{brightness}m" 

            sys.stdout.write(f"\r{color}{word} ")
            sys.stdout.flush()
            time.sleep(delay)
        time.sleep(0.2)  

    print() 


def show_fade_in_and_each_letter(text, delay, steps=10):
    for i in range(1, len(text) + 1):
        current_text = text[:i]
        
        brightness = int(255 * min(i / len(text), 1) * steps / 10)
        color = f"\033[38;2;{brightness};{brightness};{brightness}m"  

        sys.stdout.write(f"\r{color}{current_text}")
        sys.stdout.flush()
        time.sleep(delay)

    print() 

def fade_in_and_move_from_right(width, text, delay, steps):
    
    for step in range(steps + 1):
        brightness = int(255 * step / steps)
        color = f"\033[38;2;{brightness};{brightness};{brightness}m" 
        
        space = ' ' * (width - len(text) - step)  
        current_text = space + text
        
        sys.stdout.write("\r" + ' ' * width)  
        sys.stdout.flush()

        sys.stdout.write(f"\r{color}{current_text}")
        sys.stdout.flush()
        time.sleep(delay)
    
    print()  
