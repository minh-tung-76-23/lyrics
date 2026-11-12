import time
import sys
from animation import *

# Các dòng cần hiển thị
line6 = "▶ Anh đã mất quá nhiều thời gian"
line6a = "\t\t\t\t để chờ"
line7 = " ♪ Chờ một người"
line7a = "\t\t không ở đó"
line8 = "♪ Và khi màn đêm bao vây"
line8a = "♪ Không còn ai nơi đây    "
line9 = "  ♪ Phải trở về"
line9a = "\t\tđâu"
line9b = "\t\tđâu bây"
line9c = "\t\tđâu bây giờ ?"
line12 = "♪ Và giờ"
line12a = "\t những"
line12a1 = "      thước phim"
line12b = "\t\t anh vẫn"
line12c = "\t\t\t giữ nguyên"
line13 = "♪ Tự dặn lòng mình"
line13a = "\t Sẽ không"
line13b = "\t\t   phai"
line13c = "\t\t\tmờ🩶"

#Thực thi
# time.sleep(.5)
fade_in_words_non_del(line6, .01, 2)
fade_in_text(line6a, .05)
print()
time.sleep(.5)
show_each_letter(line7, .06)
time.sleep(.5)
fade_in_text(line7a, .08)
print()

time.sleep(.5)
flash_line_fade_in_out_once(line8, .8)
flash_line_fade_in_out_once(line8a, .5)

time.sleep(.2)
show_each_letter(line9, .05)
fade_in_text(line9a, .05)
fade_in_text(line9b, .05)
fade_in_text(line9c, .05)
print()

fade_in_words_non_del(line6, .01, 2)
fade_in_text(line6a, .05)
print()
time.sleep(.5)
show_each_letter(line7, .06)
time.sleep(.5)
fade_in_text(line7a, .08)
print()

show_each_letter(line12, .05)

fade_in_text(line12a, .04)
print()
fade_in_text(line12a1, .04)
fade_in_text(line12b, .04)
fade_in_text(line12c, .04)

print()
show_each_letter(line13, .06)
print()
fade_in_text(line13a, .04)
fade_in_text(line13b, .04)
fade_in_text(line13c, .04)
