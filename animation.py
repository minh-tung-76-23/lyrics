import time
import sys
from colorama import Fore, Style, init

# Khởi tạo Colorama
init(autoreset=True)

#Hàm chạy từng chữ
def show_each_letter(text, delay):
    for char in text:
        sys.stdout.write(char)  
        sys.stdout.flush()      
        time.sleep(delay)  

# Hàm fade-in 
def fade_in_text(text, delay, steps=10):
    for i in range(1, steps + 1):
        brightness = int(255 * i / steps)
        color = f"\033[38;2;{brightness};{brightness};{brightness}m" 
        sys.stdout.write(f"\r{color}{text}") 
        sys.stdout.flush()
        time.sleep(delay)

# Hàm fade-in cho từng từ không xóa
def fade_in_words_non_del(text, delay, steps=10):
    words = text.split()  

    for word_index, word in enumerate(words):
        for i in range(1, steps + 1):
            brightness = int(255 * i / steps)
            color = f"\033[38;2;{brightness};{brightness};{brightness}m" 
            
            sys.stdout.write(f"\r{color}{' '.join(words[:word_index+1])} ")  
            sys.stdout.flush()
            time.sleep(delay)

        time.sleep(0.2)  

# Hàm fade-in cho từng từ
def fade_in_words(text, delay, steps=10):
    words = text.split()
    for word in words:
        for i in range(1, steps + 1):
            brightness = int(255 * i / steps)
            color = f"\033[38;2;{brightness};{brightness};{brightness}m" 

            sys.stdout.write(f"\r{color}{word} " + '   ')
            sys.stdout.flush()
            time.sleep(delay)
        time.sleep(0.2) 

# Hàm fade-out
def fade_out_text(text, delay, steps=10):
    for i in range(steps, 0, -1):
        brightness = int(255 * i / steps)  
        color = f"\033[38;2;{brightness};{brightness};{brightness}m"  
        sys.stdout.write(f"\r{color}{text}")  
        sys.stdout.flush()  
        time.sleep(delay)  

# Hàm nháy với fade-in và fade-out
def flash_line_fade_in_out_forever(line, delay):
    while True:  # Chạy vĩnh viễn
        sys.stdout.write("\033[1;1H") 
        sys.stdout.write("\033[K")  
        fade_in_text(line, 0.03, 10)  
        time.sleep(delay)  
        sys.stdout.write("\033[1;1H") 
        sys.stdout.write("\033[K")  
        fade_out_text(line, 0.02, 10)  
        time.sleep(delay)  
        
# Hàm nháy với fade-in và fade-out một lần
def flash_line_fade_in_out_once(line, delay, fade_steps=10):
    fade_in_text(line, 0.03, fade_steps)  
    
    time.sleep(delay)
    fade_out_text(line, 0.02, fade_steps)  

    sys.stdout.write("\r" + " " * len(line))  
    sys.stdout.flush() 

# Hàm hiển thị và fade-in từng chữ
def show_fade_in_and_each_letter(text, delay, steps=10):
    for i in range(1, len(text) + 1):
        current_text = text[:i]
        
        brightness = int(255 * min(i / len(text), 1) * steps / 10)
        color = f"\033[38;2;{brightness};{brightness};{brightness}m"  

        sys.stdout.write(f"\r{color}{current_text}")
        sys.stdout.flush()
        time.sleep(delay)

    print() 

# Hàm fade-in và move từ bên phải
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
