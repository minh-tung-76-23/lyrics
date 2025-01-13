import time
import sys
from animation import * 
red = '\033[95m'  # Mã đỏ
reset = '\033[0m'  # Reset màu về mặc định

line1 = "Cho anh một chút hy vọng được không"
line1a = "              Yahh                  "
line2 = "Lý do anh vượt giông"
line2a = "          Yehh          " 
line3 = "Trái tim không còn đau"
line3a = " Vì giờ đã"
line4 = "\tGiá băng như mùa đông"
line5 = "Em mang đi hết"
line5a = "Tất cả"
line5b = " nỗi buồn đi"
line6 = "Từ cái ngày không còn bên em "
line7 = "Anh đã quen với"
line7a = "Nicotine"
line8 = "Bầu trời đang cầu vồng mây xanh"
line9 = "Bỗng chốc hóa"
line9a= "sang màu đen"
line10 = "Có phải đó là thứ mà em muốn không"
line11 = "Khi ta quay về"
line11a = "Nơi đầu tiênn..."
line11b = "🩶"

fade_in_words_non_del(line1, .001, 1)
rainbow_text(line1a, .04, 1)
fade_in_words_non_del(line2, .001, 1)
rainbow_text(line2a, .04, 1)

time.sleep(.3)
random_flicker(line3, .06, 3)
fade_in_and_move_from_right(25,line3a, 0.03, 20)      

time.sleep(.2)
fade_in_from_sides(line4, 0.07, 10)
print()

fade_in_words_non_del(line5, .001, 1)
print()
time.sleep(.2)
fade_in_text(line5a, .04)
time.sleep(.5)
show_each_letter(line5b, .05)
print()

time.sleep(.3)
bounce_text(line6, .1, 5)
print()
fade_in_words_non_del(line7, .001, 1)
show_each_letter(line7a, .05)
print()

time.sleep(.3)
bounce_text(line8, .1, 5)
print()
fade_in_words_non_del(line9, .001, 1)
time.sleep(.3)
show_each_letter(line9a, .05)
print()

time.sleep(.3)
random_flicker(line10, .1, 4)
time.sleep(.3)
fade_in_text(line11, .07)
print()
time.sleep(.3)
bounce_text(line11a, .1, 5)
show_each_letter(line11b, .05)

