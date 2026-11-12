import time
import sys
from animation import *

line1 = "Anh vui"  
line1a = "   Sao nước mắt cứ tuôn trào"  
line2 = "Chẳng phải như thế"  
line2a = "quá tốt hay sao"  
line3 = "Anh ta đáng giá nhường nào"  
line4 = "Ngược lại nhìn anh"  
line4a = "trông chẳng ra sao"  
line4b = "\tCũng đúng thôi..."  
line5 = "Anh làm gì"  
line6 = "\tXứng đáng với em🩶..."  

fade_in_words_non_del(line1, .01, 1)
print()
time.sleep(.2)
random_flicker(line1a, .07, 20)
print()
time.sleep(.5)
fade_in_words_non_del(line2, .02, 2)
time.sleep(.3)
show_each_letter(line2a, .06)
print()
time.sleep(.5)
fade_in_words_non_del(line3, .03, 3)
print()
time.sleep(1)
fade_in_words_non_del(line4, .03, 2)
time.sleep(.2)
show_each_letter(line4a, .07)
print()
time.sleep(.5)
flash_line_fade_in_out_once(line4b, 1)
time.sleep(.5)
fade_in_from_sides(line5, .07, 20)
print()
time.sleep(.8)
if line6.endswith("..."):
    main_text = line6[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08) 
    for dot in range(3):
        sys.stdout.write(".") 
        sys.stdout.flush()
        time.sleep(1)
    print()



