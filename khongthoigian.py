import time
import sys
from animation import *

linea = "\t●─ 🩶   ─●"
line1 = "𝄞 Ghì thật chặt bờ môi"
line2 = "♫ Chỉ một lần này thôi"
line3 = "  Anh mong sao"
line3a = "\t\tkhông gian ngừng trôi"
line4 = "   ♪ Đôi tay đi"
line4a = "\t\ttìm hơi ấm"
line5 = "    ♪ Đôi mi đen"
line5a = "\t\t màu vương vấn"
line6 = "Là giây phút"
line6a = "\tanh nhận ra"
line6b = "anh nhận ra"
line7 = "À khi thế gian ngừng xoay vòng"
line8 = "Theo"
line8a = " chiếc kim đồng hồ"
line9 = "Hai ❤️"
line9a = " cùng đan lấy nhau"
line9b = "Mình chưa thấy đau"
line9c = "\t\t bao giờ"
line10 = "Bình yên hóa ra là như thế"
line11 = "     Ngày đêm không còn"
line11a = "\t\t\tvội chia đôi"
line11b = "       Mặt trời"
line11c = "\t\tngưng rơi"
line12 = "    Là giây phút"
line12a = "\t\t bên cạnh em"
line12b = "Không thời gian như ngừng trôi..."

flash_line_fade_in_out_once(line1, 2)
time.sleep(.2)
flash_line_fade_in_out_once(line2, 3)
time.sleep(.5)
fade_in_words_non_del(line3, .02, 2)
time.sleep(.2)
print()
fade_in_and_move_from_right(40, line3a, .03, 20)
time.sleep(.5)
flash_line_fade_in_out_once(linea, .5)

show_each_letter(line4, .06)
time.sleep(.5)
fade_in_text(line4a, .06)
print()
time.sleep(.5)

fade_in_words_non_del(line5, .02, 5)
time.sleep(.5)
fade_in_text(line5a, .06)
print()
time.sleep(1.5)

show_each_letter(line6, .04)
print()
random_flicker(line6a, .04, 10)
time.sleep(.2)
bounce_text(line6b, .05, 10)
time.sleep(.2)
clear_line()
fade_in_text(line6a, .06)
print()
time.sleep(1.)

show_fade_in_and_each_letter(line7, .06)
print()
fade_in_text(line8, .04)
time.sleep(.5)
show_each_letter(line8a, .06)
print()
time.sleep(1)

fade_in_words_non_del(line9, .03, 5)
time.sleep(.2)
show_each_letter(line9a, .05)
print()
time.sleep(.3)

fade_in_words_non_del(line9b, .02, 2)
print()
time.sleep(.2)
fade_in_text(line9c, .06)
time.sleep(1.5)

fade_out_by_char(line10, .05, 10)
time.sleep(.2)
fade_in_words_non_del(line11, .02, 2)
time.sleep(.2)
fade_in_text(line11a, .04)
print()
time.sleep(.5)

fade_in_text(line11b, .04)
time.sleep(.2)
fade_in_text(line11c, .04)
print()
time.sleep(.3)

fade_in_words_non_del(line12, .02, 2)
time.sleep(.2)
fade_in_words_non_del(line12a, .02, 2)
print()
time.sleep(.2)
if line12b.endswith("..."):
    main_text = line12b[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print() 
