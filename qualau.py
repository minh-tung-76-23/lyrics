import time
import sys
from animation import * 

line1 = "  Em muốn chúng mình là gì?  "  
line2 = "Vì anh muốn chúng mình là hơn"  
line3 = "  Anh muốn chúng mình là hơn  "  
line4 = "Anh muốn chúng ta"  
line4a = "hơn là bạn..."  
line5 = "Đã đến lúc"  
line5a = "chúng ta hạ màn..."  
line6 = "  Anh đã thực sự yêu em"  
line6a = " quá lâu"  
line6b = "\t\t\tquá lâu"  
line7 = "Không giấu em được nữa đâu"  
line8 = "Quá lâu"  
line8a = "\t, quá lâu" 
line9 = ", quá lâu❤️ ..."  



show_fade_in_and_each_letter(line1, .06)
time.sleep(.5)
flash_line_fade_in_out_once(line2, 1)
time.sleep(.5)
flash_line_fade_in_out_once(line3, 1)

time.sleep(.2)
fade_in_words_non_del(line4, .01, 1)
time.sleep(.2)
show_each_letter(line4a, .06)
print()
time.sleep(.5)

fade_in_from_sides(line1, .07, 20)
print()
time.sleep(.5)
fade_in_and_move_from_right(40, line2, .07, 25)
time.sleep(.1)
fade_in_from_sides(line3, .07, 20)

print()
time.sleep(.2)
fade_in_words_non_del(line5, .01, 1)
time.sleep(.2)
show_each_letter(line5a, .06)
print()
time.sleep(.5)

fade_in_from_sides(line6, .07, 20)
time.sleep(.1)
fade_in_text(line6b, .1)
time.sleep(.5)
show_each_letter(line6a, .06)
print()
time.sleep(1)

fade_in_words_non_del(line6, .01, 1)
time.sleep(.2)
show_each_letter(line6a, .06)
print()
time.sleep(.5)
typewriter_effect(line7, .07)
print()
time.sleep(.5)

fade_in_from_sides(line6, .07, 20)
time.sleep(.1)
fade_in_text(line6b, .06)
time.sleep(.5)
show_each_letter(line6a, .06)
print()
time.sleep(.5)

fade_in_from_sides(line8, .07, 20)
time.sleep(.1)
fade_in_text(line8a, .06)
time.sleep(.5)
if line9.endswith("..."):
    main_text = line9[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.09) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print()





