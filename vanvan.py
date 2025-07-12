import time
import sys
from animation import *

line1 = "Thiên thần"  
line1a = "\t\tsa ngã"  
line1b = "\tĐêm mờ"  
line1c = " trôi"  
line2 = "Em có"  
line2a = "\tma thuật"  
line2b = "Trên bờ"   
line2c = " môi"  
line3 = "Spicy fancy"  
line3b = "Kiêu kì"  
line3c = "        ôi thôi rồi      "  
line4 = "So let’s make"  
line4a = "\t\tit rain"  
line4b = "Như tờ"  
line4c = " rơi..."  
line5 = "Muốn hôn em thật sâu"  
line5a = "Baby"  
line5b = " nhìn anh thật lâu"  
line6 = "Lấy một K ra Dot"  
line6a = "Em chill nhạc J cả câu"  
line7 = "Lại rủ anh ra đằng sau"  
line7a = "Xinh gái ơi"  
line7b = "em ở đâu?"  
line8 = "Em muốn review đập hộp"  
line8a = "Muốn công nghệ var"  
line8b = "\t\tvào đâu???"  

time.sleep(2)
fade_in_words_non_del(line1, .01, 1)
time.sleep(.5)
fade_in_text(line1a, .045, 10)
print()  
time.sleep(.4)
fade_in_text(line1b, .04, 10)
time.sleep(.2)
show_each_letter(line1c, .05)
print()
time.sleep(.5)

fade_in_words_non_del(line2, .01, 1)
time.sleep(.5)
fade_in_text(line2a, .05, 10)
print()  
time.sleep(.5)
fade_in_text(line2b, .05, 10)
time.sleep(.5)
show_each_letter(line2c, .05)
print()
time.sleep(.5)

fade_in_words_non_del(line3, .05, 10)
print()    
time.sleep(.3)
fade_in_text(line3b, .03, 5)
print()
time.sleep(.2)
random_flicker(line3c, .04, 10)
print()
time.sleep(.2)

wave_text(line4, .02, 5)
time.sleep(.2)
fade_in_text(line4a, .05, 10)
print()
time.sleep(.5)
random_flicker(line4b, .05, 5)
time.sleep(.5)
show_each_letter(line4c, .05)
print()
time.sleep(.5)

fade_in_words_non_del(line5, .01, 1)
print()
time.sleep(.5)
fade_in_text(line5a, .01, 1)
time.sleep(.1)
show_each_letter(line5b, .05)

print()
time.sleep(.5)
fade_in_words_non_del(line6, .01, 4)
print()
time.sleep(.5)
random_flicker(line6a, .06, 20)

print()
time.sleep(.5)
color_splash_effect(line7, .06, 10)
print()
time.sleep(.5)
fade_in_words_non_del(line7a, .01, 1)
time.sleep(.2)
show_each_letter(line7b, .05)

print()
time.sleep(.5)
fade_in_from_sides(line8, .05, 20)
print()
time.sleep(.1)
fade_in_words_non_del(line8a, .01, 1)
print()
time.sleep(.1)
color_splash_effect(line8b, .04, 10)









