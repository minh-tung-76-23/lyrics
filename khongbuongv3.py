import time
import sys
from animation import * 

line1 = "Anh cố để chi vậy?"
line1a = "Rồi cũng ra như này"
line2 = "   Cứ vun mối tình     "
line2a = "Mặc tấm thân hao gầy"
line3 = "Liệu có phút giây nào"
line3a = "\tNgười xót anh không vậy?"
line4 = "Mọi thứ chỉ để anh gánh lấy..."
line5 = "Chẳng phút giây nào"
line5a = "  Anh hết yêu em   "
line6 = " Mỗi lần ướt mi hoen"
line6a = "Là do anh nhớ em thêm..."
line7 = "Tại sao lại nói yêu anh"
line7a = "Mà lại để mi anh"
line7b = "\t\t ướt nhèm 💔"

show_fade_in_and_each_letter(line1, .08)
time.sleep(.5)
show_fade_in_and_each_letter(line1a, .09)
time.sleep(1)

fade_in_text(line2, .1)
time.sleep(.5)
show_fade_in_and_each_letter(line2a, .07)
time.sleep(1.5)

show_fade_in_and_each_letter(line3, .09)
print()
time.sleep(.5)
fade_in_text(line3a, .1)
print()
time.sleep(1)

show_fade_in_and_each_letter(line4, .09)
print()
time.sleep(.5)

fade_in_words_non_del(line5, .02, 3)
time.sleep(.5)
show_fade_in_and_each_letter(line5a, .08)
time.sleep(.5)

show_fade_in_and_each_letter(line6, .08)
time.sleep(.3)
fade_in_words_non_del(line6a, .02, 3)
print()
time.sleep(.5)

show_fade_in_and_each_letter(line7, .08)
print()
time.sleep(.5)
show_fade_in_and_each_letter(line7a, .08)
time.sleep(1)
fade_in_text(line7b, .3)







