import time
import sys
from animation import *

line1 = "Chính vào ngày hôm đó"  
line1a = "    Gió bấc thật lạnh"  
line2 = "Bên trong anh nhận ra"  
line2a = "Một sự thật khó fine "  
line3 = "Đó chính là cái cách"  
line3a = "   Trái đất vận hành"  
line4 = "Khi"  
line4a = "xung quanh đông người thế"  
line4b = "  Mà mình lại chẳng có ai  "  
line5 = "Nếu như mà em chẳng"  
line5a = "  Muốn nói điều gì"  
line6 = "Không gian kia lặng im"  
line6a = " Như đang nhìn thấu ta"  
line7 = "Anh như đã được thấy"  
line7a = "   Thế giới diệu kì"  
line8 = "thứ anh cho rằng tốt"  
line8a = "  Thì nó lại càng xấu xa"  
linea = "          ●─💔 ─●"


show_fade_in_and_each_letter(line1, .04)
time.sleep(.2)
fade_in_words_non_del(line1a, .02, 3)
print()
time.sleep(.5)
fade_in_words_non_del(line2, .01, 1)
time.sleep(.2)
color_splash_effect(line2a, .02, 15)
print()
time.sleep(.5)

show_fade_in_and_each_letter(line3, .04)
time.sleep(.2)
fade_in_words_non_del(line3a, .02, 3)
fade_in_words_non_del(line4, .01, 1)
time.sleep(.2)
show_each_letter(line4a, .05)
print()
time.sleep(.2)
fade_in_from_sides(line4b, .05, 15)

print()
time.sleep(.2)
show_fade_in_and_each_letter(line5, .04)
time.sleep(.2)
fade_in_words_non_del(line5a, .02, 3)
print()
time.sleep(.3)
fade_in_words_non_del(line6, .01, 1)
print()
time.sleep(.2)
fade_in_and_move_from_right(30, line6a, .05, 20)

time.sleep(.2)
show_fade_in_and_each_letter(line7, .04)
time.sleep(.2)
fade_in_words_non_del(line7a, .02, 3)
fade_in_words_non_del(line4, .01, 1)
time.sleep(.2)
show_each_letter(line8, .04)
print()
time.sleep(.2)
fade_in_words_non_del(line8a, .01, 1)
print()
time.sleep(.2)
flash_line_fade_in_out_once(linea, 2)

