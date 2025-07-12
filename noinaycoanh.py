import time
import sys
from animation import *

line1 = "Khép đôi mi thật lâu"  
line2 = "Nguyện mãi bên cạnh nhau"  
line3 = "Yêu say đắm như ngày đầu❤️"  
line4 = "Mùa xuân đến"  
line4a = "bình"  
line4b = "\t\th yên"  
line4c = "Cho anh những giấc mơ"  
line5 = "Hạ lưu giữ"  
line5a = "ngày "  
line5b = "\t\tmưa"  
line5c = "Ngọt ngào nên thơ"  
line6 = "Mùa thu lá vàng"  
line6a = "\t\trơi"  
line6b = "Đông sang anh nhớ em"  
line7c = "Tình yêu bé nhỏ"  
line7d = "\t\txin "  
line7e = "Dành tặng riêng em❤️"  

print('\n\n\n')
show_fade_in_and_each_letter(line1, .03 )
time.sleep(.3)
fade_out_from_sides_left(line2, .05, 20)
fade_in_from_sides(line3, .07, 20)
print()
time.sleep(1)

fade_in_words_non_del(line4, .03, 1)
time.sleep(.2)
show_each_letter(line4a, .07)
time.sleep(.6)
fade_in_text(line4b, .05, 10)
# show_each_letter(line4b, .1)
time.sleep(.5)
print()
show_fade_in_and_each_letter(line4c, .05 )
print()

time.sleep(.5)
fade_in_words_non_del(line5, .03, 2)
time.sleep(.2)
show_each_letter(line5a, .07)
time.sleep(.6)
fade_in_text(line5b, .05, 10)
# show_each_letter(line4b, .1)
time.sleep(.5)
print()
show_fade_in_and_each_letter(line5c, .05 )
print()

time.sleep(1)
fade_in_words_non_del(line6, .04, 2)
time.sleep(.6)
fade_in_text(line6a, .05, 10)
# show_each_letter(line4b, .1)
time.sleep(.8)
print()
show_fade_in_and_each_letter(line6b, .05 )
print()

time.sleep(.3)
fade_in_words_non_del(line7c, .05, 2)
time.sleep(.6)
fade_in_text(line7d, .05, 10)
# show_each_letter(line4b, .1)
time.sleep(.7)
print()
show_fade_in_and_each_letter(line7e, .08 )
print('\n\n\n')