import time
import sys
from animation import *

line1 = "🎧  Điều anh luôn giữ kín trong ❤️"  
line2 = "🎙️    Thương em, anh mới xin là      "  
line3 = "Điều anh luôn giữ kín trong tim mình"  
line4 = "🎧   Thương em vì thương thôi mà      "  
line5 = "♪  Điều anh luôn giữ kín trong tim mình"  
line6 = "♬ Có ai thương lắng lo cho em ?"  
line7 = "\t..."  
line7a = "\t\tCho em🩶  ..."  

fade_in_from_sides(line1, .06, 20)
time.sleep(.2)
show_fade_in_and_each_letter(line2, .08)
print()
time.sleep(.4)
 
fade_out_from_sides_left(line3, .06, 25)
time.sleep(.2)
show_fade_in_and_each_letter(line4, .07)
print()
time.sleep(.5)
fade_in_text(line5, .08, 25)

print()
time.sleep(1.5)
show_fade_in_and_each_letter(line6, .08)
print()
time.sleep(.2)
if line7.endswith("..."):
    main_text = line7[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.15) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.8)
    print()
print()
time.sleep(.3)
flash_line_fade_in_out_once(line7a, 1)






