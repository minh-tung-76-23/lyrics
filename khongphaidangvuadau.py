import time
import sys
from animation import *

line1 = "      Một điều tôi kiếm tìm"  
line1a = "     Một loài hoa khác biệt"  
line1b = "Mùi hương chẳng giống"  
line1ba = " theo một ai"  
line1c = "\tTôi là tôi"  
line1d = "\t Ai là ai"  
line1e = "    Tôi mặc kệ thôi!    "  
line2 = "  Cuối con đường kia   "  
line2a = "  Thênh thang muôn lối"  
line3 = "Cuối chân trời kia"  
line3a = "  Không xa tôi tới"  
line4 = "Có cơn mưa hoà tan"  
line4a = " Nỗi niềm thế gian"  
line5 = "  Có ai đang cùng tôi"  
line5a = "Sống trọn từng phút giây"  

fade_in_words_non_del(line1, .01, 1)
time.sleep(.5)
color_splash_effect(line1a, .02, 10)
time.sleep(.5)
random_flicker(line1b, .05, 10)
show_each_letter(line1ba, .04)
print()
fade_in_words_non_del(line1c, .01, 1)
fade_in_words_non_del(line1d, .01, 1)
fade_in_from_sides(line1e, .02, 10)
show_fade_in_and_each_letter(line2, .03)
fade_in_words_non_del(line2a, .02, 2)

print()
time.sleep(.2)
show_fade_in_and_each_letter(line3, .03)
time.sleep(.2)
fade_in_words_non_del(line3a, .02, 2)

print()
time.sleep(.2)
show_fade_in_and_each_letter(line4, .06)
time.sleep(.2)
fade_in_from_sides(line4a, .04, 10)

time.sleep(.2)
fade_in_words_non_del(line5, .02, 1)
time.sleep(.2)
flash_line_fade_in_out_once(line5a, .6)
time.sleep(.5)
show_fade_in_and_each_letter(line2, .03)
fade_in_words_non_del(line2a, .02, 2)

print()
time.sleep(.3)
show_fade_in_and_each_letter(line3, .03)
time.sleep(.3)
fade_in_words_non_del(line3a, .02, 2)

print()
time.sleep(.2)
show_fade_in_and_each_letter(line4, .06)
time.sleep(.2)
fade_in_from_sides(line4a, .04, 10)

print()
time.sleep(.2)
fade_in_words_non_del(line5, .02, 1)
time.sleep(.2)
fade_in_from_sides(line5a, .05, 20)

