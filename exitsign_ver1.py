import time
import sys
from animation import *

line1 = "🎙️ Anh từng mong em hạnh phúc"
line2 = "    Tới khi em nở nụ cười"
line3 = "   Anh như bị *** mười nhát"
line4 = "♪ Khi anh đứng trên sân khấu một mình"
line5 = "\tCòn em đứng cạnh             "
line6 = "    Cùng với một người khác"
line = "Anh mất em rồi 🩶 ..."
line7 = "♪ Em hiểu rằng"
line8 = "       Chúng ta"
line8a = "\t\tkhông ai là sai"
line9 = "   ♪ Chỉ là em không muốn"
line10 = "Em mãi sẽ là lựa chọn thứ hai"
line11 = "♪ Mãi sau những điều"
line12 = "   Anh cho là lý do"
line13 = "\tĐể anh tồn tại"
line14 = "   Vậy đâu còn lý do"
line15 = "\tĐể em ở lại"
line16 = "♪ Đây sẽ là lý do"
line17 = "\tEm sẽ thôi đắn đo      "
line18 = "\tCứ ôm mộng hoài"
line19 = "♪ So thanks for showing me the exit sign..."

show_each_letter(line1, 0.03)
print()
time.sleep(.2)
show_each_letter(line2, 0.03)
print()
time.sleep(.2)
fade_in_text(line3, .05)
print()

time.sleep(.2)
show_each_letter(line4, 0.02)
time.sleep(.2)
fade_in_and_move_from_right(30, line5, .06, 10)
fade_in_text(line6, .08)
print()
fade_in_words(line, .025, 10)

time.sleep(.2)
flash_line_fade_in_out_once(line7, .5)
show_each_letter(line8, 0.02)
fade_in_text(line8a, .1)
print()

time.sleep(1)
flash_line_fade_in_out_once(line9, 1)
flash_line_fade_in_out_once(line10, 2)

time.sleep(.2)
show_each_letter(line11, 0.07)
time.sleep(.4)
fade_in_and_move_from_right(30, line12, .09, 10)
time.sleep(1.5)
fade_in_text(line13, 0.09)
print()

time.sleep(.2)
fade_in_and_move_from_right(30, line14, .09, 10)
time.sleep(1.2)
fade_in_text(line15, .09)
print()

time.sleep(.2)
show_each_letter(line16, 0.09)
print()
time.sleep(.7)
fade_in_and_move_from_right(30, line17, .07, 10)
time.sleep(.2)
fade_in_text(line18, .08)
print()

time.sleep(.2)
if line19.endswith("..."):
    main_text = line19[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print() 

