import time
import sys
from animation import *

line1 = "Chúng ta không thuộc về nhau"  
line2 = "Chúng ta không thuộc về"  
line2a = "\t\t\tnơi này💔"  
line3 = "Niềm tin đã mất"  
line4 = "Giọt nước mắt"  
line4a = "Cuốn ký ức anh chìm sâu"  
line5 = "Tìm về nơi đâu"  
line6 = "Cô đơn đôi chân"  
line6a = "Lạc trôi giữa bầu trời"  
line7 = "Màn đêm che dấu "  
line8 = "Từng góc tối"  
line8a = "Khuất lấp phía sau bờ môi"  
line9 = "Tại vì anh thôi"  
line10 = "Yêu say mê"  
line10a = " nên đôi khi"  
line10b = "\t\tQuá dại khờ..."  

fade_out_by_char(line1, .07, 20)
time.sleep(1.5)
fade_in_words_non_del(line2, .03, 2)
time.sleep(1)
fade_in_text(line2a, .09)
print()
time.sleep(1.5)
fade_in_from_sides(line3, .06, 20)
print()
time.sleep(.3)
fade_in_words(line4, .01, 1)
time.sleep(.2)
show_fade_in_and_each_letter(line4a, .07)
print()
time.sleep(1)
fade_in_words(line5, .05, 1)
time.sleep(.5)
show_fade_in_and_each_letter(line6, .07)
print()
time.sleep(.2)
fade_in_and_move_from_right(40, line6a, .06, 20)
time.sleep(.5)
bounce_text(line7, .08, 7)
print()
time.sleep(.5)
fade_in_words(line8, .05, 1)
time.sleep(.2)
show_fade_in_and_each_letter(line8a, .07)
print()
time.sleep(.2)

fade_in_words(line9, .01, 1)
time.sleep(.5)
random_flicker(line10, .05, 10)
time.sleep(.2)
show_each_letter(line10a, .07)
print()
time.sleep(.2)
fade_in_from_sides(line10b, .06, 20)








