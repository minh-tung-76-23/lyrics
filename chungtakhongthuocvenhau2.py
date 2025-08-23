import time
import sys
from animation import *

line1 = "Phía trước bây giờ"  
line1a = "Ai đang nắm chật bàn tay"  
line1b = "\t\t\t của em vậy?"  
line2 = "Mông lung như một trò đùa"  
line3 = "Anh xin giơ tay"  
line3a = "rút lui thôi"  
line4 = "Trách ai bây giờ đây?"  
linea = "      ●─🩶 ─●"
line5 = "Chúng ta không thuộc về nhau"  
line5a = "Chúng ta không thuộc về nhau💔"  
line8 = "Em hãy"  
line8a = "cứ đi bên người mà em cần"  
line9 = "Trái tim không thuộc về nhau"  
line10 = "Giấc mơ không là của nhau"  
line11 = "Xoá câu ca buồn chiều mưa"  
line12 = "Anh lỡ"  
line12a = "xóa luôn yêu thương ngày xưa rồi"  


color_splash_effect(line1, .02, 5)
time.sleep(.2)
fade_in_words_non_del(line1a, .01, 1)
time.sleep(.2)
fade_in_text(line1b, .09)
print()
time.sleep(.5)
show_fade_in_and_each_letter(line2, .06)
print()
time.sleep(.5)
fade_in_words_non_del(line3, .01, 1)
time.sleep(.2)
show_each_letter(line3a, .05)
print()
time.sleep(1)
flash_line_fade_in_out_once(line4, 2)
fade_in_from_sides(linea, .06, 20)

fade_in_words_non_del(line5, .01, 1)
time.sleep(.5)
fade_out_by_char(line5, .05, 10)
time.sleep(.5)
fade_in_from_sides(line5, .06, 20)
print()
time.sleep(.5)

fade_in_words_non_del(line8, .01, 1)
time.sleep(.3)
show_each_letter(line8a, .05)
print()
time.sleep(.5)

fade_in_words_non_del(line9, .01, 1)
time.sleep(.3)
flash_line_fade_in_out_once(line10, 2)
time.sleep(.5)
fade_in_from_sides(line11, .06, 20)
print()
time.sleep(.5)
fade_in_words_non_del(line12, .01, 1)
time.sleep(.3)
show_each_letter(line12a, .05)
print()
flash_line_fade_in_out_once(line5a, 2)









