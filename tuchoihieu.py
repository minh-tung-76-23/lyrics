import time
import sys
from animation import *

line1 = "\t▶ Lại là DG House"
line2 = "\t\t ♫ Rhyder"
line3 = "▶  Có những lúc anh nghĩ"
line3a = "\t anh chẳng thoát ra được đâu"
line4 = "♫ Nhưng vẫn cố bước tiếp"
line4a = "\t vì chuyện đã qua từ lâu"
line5 = "♪ Dẫu vẫn biết tất cả"
line5a = "\t\tcũng đều giống như màn cược"
line6 = "♫ Nhưng anh vẫn luôn tin rằng"
line6a = "\t\tchắc chắn anh làm được"
line7 = "▶  Mây lang thang cuốn lấy ký ức kia"
line7a = "       \t\t\t\t xé đôi"
line8 = "   ♫ Và anh vẫn sẽ đứng rap như"
line8a = "\t\t\t\tthế thôi"
line8b = "\t\t\t\tthế thôi..."


time.sleep(1)
flash_line_fade_in_out_once(line1, 3)
time.sleep(.08)
flash_line_fade_in_out_once(line2, 2)
print()

time.sleep(1)
show_each_letter(line3, delay=0.06)
print()
time.sleep(.05)
fade_in_text(line3a, 0.2)
print()

time.sleep(.2)
show_each_letter(line4, delay=0.06)
print()
fade_in_text(line4a, .3)
time.sleep(.08)
print()

fade_in_text(line5, .1)
time.sleep(.08)
print()
fade_in_and_move_from_right(20,line5a, 0.1, 20) 

time.sleep(.2)
fade_in_and_move_from_right(35,line6, 0.1, 20) 
show_fade_in_and_each_letter(line6a, 0.07)

time.sleep(1)
show_each_letter(line3, delay=0.06)
print()
time.sleep(.05)
fade_in_text(line3a, 0.2)
print()

time.sleep(.2)
show_each_letter(line4, delay=0.06)
print()
fade_in_text(line4a, .3)
time.sleep(.08)
print()

show_each_letter(line7, delay=0.05)
flash_line_fade_in_out_once(line7a, 1)
fade_in_text(line7a, delay=0.06)
print()

time.sleep(1)
show_each_letter(line8, delay=0.05)
flash_line_fade_in_out_once(line8a, 1)
fade_in_text(line8b, delay=0.06)
print()