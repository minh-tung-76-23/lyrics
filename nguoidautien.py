import time
import sys
from animation import *

line1 = "    Cớ sao ông trời"
line2 = "   Lấy đi"
line2a = " cả thế giới 💔"
line3 = "Em đừng trông mong theo anh đến nơi"
line4 = "Em còn thanh xuân"
line4a = "\t\tn còn cả quãng đời"
line5 = "Anh được ngắm em"
line6 = "\tCười trong"
line6a = " năm tháng đôi mươi"
line7 = "Đã được nói ra lời yêu"
line8 = "\tAnh sẽ mang theo suốt đời"
line9 = "Là người đầu tiên cầm tay"
line10 = "Là người đầu tiên"
line11 = "\tÔm em dưới bầu trời này"
line12 = "Là người đầu tiên chạm môi"
line13 = "Là người đầu tiên"
line14 = "\tEm dâng cả cuộc đời🩶..."


flash_line_fade_in_out_once(line1, 3)
time.sleep(.5)
fade_in_text(line2, .15)
time.sleep(.8)
show_each_letter(line2a, .12)
time.sleep(.3)
print()

show_fade_in_and_each_letter(line3, .08)
time.sleep(.5)
print()
show_fade_in_and_each_letter(line4, .08)
time.sleep(.8)
fade_in_text(line4a, .08)
time.sleep(.7)
print()
fade_in_text(line5, .08)
time.sleep(.5)
print()
fade_in_text(line6, .06)
time.sleep(.5)
show_each_letter(line6a, .08)
time.sleep(.5)
print()
show_fade_in_and_each_letter(line7, .07)
time.sleep(.5)
print()
fade_in_from_sides(line8, .15, 30)
time.sleep(.5)
print()

flash_line_fade_in_out_once(line9, 2)
time.sleep(.5)
show_fade_in_and_each_letter(line10, .06)
time.sleep(.5)
print()

fade_in_text(line11, .04)
time.sleep(2)
print()

flash_line_fade_in_out_once(line12, 2)
time.sleep(.5)
fade_in_text(line13, .07)
print()
time.sleep(.5)
if line14.endswith("..."):
    main_text = line14[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print() 
