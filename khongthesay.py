import time
import sys
from animation import *

line1 = "♪ Cố gắng hết bao nhiêu"
line1a = "\tVà cũng xa nhau"
line1c = " mãi..."
line1b = "          ●─ 💔  ─●"
line2 = "🎧 Đã hơn một"
line2a = "năm trôi qua"
line2b = "♪ Mà mẹ vẫn thế"
line2c = "\t\tcứ tiếc đôi ta"
line3 = "\tXoá cả hình xăm trên da"
line4 = "♪ Chuyện tình mình cũng"
line4a = "\t\tChẳng thể phôi pha"
line5 = "♯ Chắc cũng đã lâu"
line5a = "\tAnh không"
line5b = "\t\tmuốn say mà"
line6 = "♬ Cuối cùng là hôm nay"
line6a = "Anh lại nhớ"
line6b = " tới em"
line7 = "♪ Có thể sẽ phone cho em"
line8 = "Và sẽ lại nói"
line8a = " 'Anh vẫn yêu em'"
line9 = "Bấm chuông nhà em"
line9a = "\t\tm trong"
line9b = "\t\t\tđêm"
line10 = "🎙️ Và hàng ngàn thứ biết chắc không nên"
line11 = "  Hứa trong lòng"
line11a = "\tAnh sẽ không"
line11b = "\t\tuống thêm được"
line12 = "♪ Vì em là lí do số một"
line12a = "Làm cho                           "
line12b = "\tAnh không thể..."
line12d = "𝄞 Anh không thể"
line12e = "\t\tsay💔..."

# time.sleep(.3)
show_each_letter(line1, .04)
print()
time.sleep(.3)
fade_in_text(line1a, .09)
time.sleep(.5)
if line1c.endswith("..."):
    main_text = line1c[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.15) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print() 

flash_line_fade_in_out_once(line1b, 2)

time.sleep(1)
fade_in_words_non_del(line2, .03, 15)
time.sleep(.2)
show_each_letter(line2a, .07)
print()
time.sleep(.5)
show_each_letter(line2b, .05)
time.sleep(.3)
fade_in_text(line2c, .08)
print()
show_fade_in_and_each_letter(line3, .06)
print()

time.sleep(.1)
show_each_letter(line4, .05)
print()
time.sleep(.1)
fade_in_text(line4a, .05)
print()

time.sleep(.3)
show_fade_in_and_each_letter(line5, .045)
print()
fade_in_words_non_del(line5a, .04, 10)
time.sleep(.1)
fade_in_text(line5b, .09)
print()

time.sleep(.5)
fade_in_and_move_from_right(30, line6, .08, 10)
time.sleep(.3)
fade_in_text(line6a, .05)
time.sleep(.5)
show_each_letter(line6b, .07)
print()

time.sleep(.5)
show_fade_in_and_each_letter(line7, .06)
print()
time.sleep(.3)
fade_in_text(line8, .05)
time.sleep(.5)
show_each_letter(line8a, .07)
print()
show_each_letter(line9, .06)
fade_in_text(line9a, .05)
fade_in_text(line9b, .05)
print()

time.sleep(.2)
show_fade_in_and_each_letter(line10, .04)
print()
show_each_letter(line11, .04)
print()
time.sleep(.2)
fade_in_words_non_del(line11a, .04, 5)
time.sleep(.5)
fade_in_text(line11b, .05)
print()

time.sleep(.4)
show_fade_in_and_each_letter(line12, .06)
print()
time.sleep(.5)
flash_line_fade_in_out_once(line12a, 1)
time.sleep(.2)
if line12b.endswith("..."):
    main_text = line12b[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.7)

time.sleep(.3)
show_fade_in_and_each_letter(line12a, .06)
time.sleep(.2)
fade_in_text(line12d, .05)
time.sleep(1)
flash_line_fade_in_out_once(line12e, 1)
















