import time
import sys
from colorama import Fore, Style, init
from animation import show_each_letter, fade_in_text, show_fade_in_and_each_letter
# Nội dung
print("\n")
line1 = "▶  Phiêu du mây xanh \n"
line2 = "♬ Thôi đem giấc mơ ấy cho người yêu em thay anh"
line3 = "♪ Anh cũng biết đau trái tim kia"
line3a = "\t\t\t\t đâu"
line3b = "\t\t\t\t đâu phải"
line3c = "\t\t\t\t đâu phải cỗ"
line3d = "\t\t\t\t đâu phải cỗ máy"
line4 = "♪ Mà giấu suy tư từng giây"
line5 = "          ●─🩶  ─●"
line0 = "♫ Vì đời vốn là đâu như trông mong"
line6 = "♫ Ta là câu chuyện song song\n"
line7 = "♫ Nên đành giấu suy tư này trong lòng"
line8 = "♩ Em đánh mất đi người bạn tồi"
line9 = "♩ Còn anh đánh mất đi cả bầu trời..."

# Thực thi
time.sleep(.5)  
show_each_letter(line1, delay=0.04)     
time.sleep(.7)  
show_fade_in_and_each_letter(line2, delay=0.06)
print()    
time.sleep(.7)   
show_each_letter(line3, delay=0.045)
fade_in_text(line3a, delay=0.07)
fade_in_text(line3b, delay=0.07)
fade_in_text(line3c, delay=0.07)
fade_in_text(line3d, delay=0.07)
print()
time.sleep(.5)  
fade_in_text(line4, delay=0.05)  
print() 
time.sleep(.7)  
fade_in_text(line5, delay=0.05)  
print()    
time.sleep(.7)  
fade_in_text(line0, delay=0.05)
print() 
time.sleep(1.2)  
show_each_letter(line6, delay=0.04)      
time.sleep(.7)  
show_fade_in_and_each_letter(line7, delay=0.08)
print()  
time.sleep(.9)  
fade_in_text(line8, delay=0.2)      
time.sleep(1)  
print() 

if line9.endswith("..."):
    main_text = line9[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.09) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print() 



