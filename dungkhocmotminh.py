import time
import sys
from animation import *

line1 = "  Lý do"
line1a = "\tchia tay"
line1b = " ai còn biết đâu"
line1c = " Về sau                          "
line1d = "\tchẳng thấy"
line1e = "Để mất đi người mình yêu..."
linea = "          ●─🩶  ─●"
line2 = "Đừng khóc một mình"
line2a = "em ơi..."
line3 = "Vì những câu chuyện"
line3a = "đâu ai hiểu được"
line4a = "Là do ta"
line4 = "\t đã quá yêu thôi mà"
line5 = "\t đã chấp nhận tổn thương"
line6 = "Vì thế gian"
line6a = "đầy ưu tư"
line7 = "Vì thế ta"
line7a = "lạc mất nhau"
line7b = "\t\t\tthật rồi"
line8 = "Anh chẳng thể níu giữ"
line9 = "Anh chẳng thể lau"
line9a = "Những nỗi đau"
line9b = "còn giấu"
line10 = "Từ sâu trong đôi mắt em🩶 ..."

fade_in_text(line1, .06)
time.sleep(.5)
fade_in_text(line1a, .06)
time.sleep(.3)
show_each_letter(line1b,.05)
time.sleep(.3)
fade_in_text(line1c, .06)
time.sleep(.5)
fade_in_text(line1d, .06)
print()
time.sleep(.3)
show_fade_in_and_each_letter(line1e, .08)
print()
flash_line_fade_in_out_once(linea, 1.5)
time.sleep(.3)
fade_in_words_non_del(line2, .01, 10)
if line2a.endswith("..."):
    main_text = line2a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.6)
    print()

time.sleep(.3)
fade_in_words_non_del(line3, .01, 10)
time.sleep(.3)
show_each_letter(line3a,.07)
print()

time.sleep(1)
fade_in_words_non_del(line4a, .01, 10)
time.sleep(.3)
fade_in_from_sides(line4, .06, 30)
print()

time.sleep(.5)
fade_in_words_non_del(line4a, .01, 10)
time.sleep(.3)
fade_in_from_sides(line5, .06, 30)
print()

time.sleep(.5)
fade_in_words_non_del(line6, .01, 10)
time.sleep(.3)
show_each_letter(line6a,.07)
print()

time.sleep(1)
fade_in_words_non_del(line7, .01, 10)
time.sleep(.3)
show_each_letter(line7a,.07)
time.sleep(.5)
fade_in_text(line7b, .09)
print()

time.sleep(.5)
fade_in_from_sides(line8, .06, 30)
print()

time.sleep(.5)
fade_in_and_move_from_right(30, line9, .04, 15)

time.sleep(.3)
fade_in_words_non_del(line9a, .01, 10)
time.sleep(.5)
show_each_letter(line9b,.08)
print()
time.sleep(1)
if line10.endswith("..."):
    main_text = line10[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print()












