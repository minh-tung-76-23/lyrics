import time
import sys
from animation import *

line1 = "♪ Có lẽ là"
line1a = "vì anh🩶"
line2 = "🎙️  Có lẽ tên của anh"
line2a = "Giờ nằm trong blacklist"
line3 = "♪ Những nỗi đau này ghim vào melody"
line3a = "Thêm một track hit"
line4 = "♪ Nhưng ở phía sau anh đâu còn em"
line4a = "\tKhông còn ý nghĩa💔"
line5 = "♪ Ôm hết những hối hận trong căn phòng đen"
line6 = "♪ Nốc vài ly bia"

line7 = "♪ Tự nói sẽ mau quên"
line7a = "một bài hát vang lên"
line7b = "Bất ngờ"
line7c = " ở trong in ear"
line8 = "♪ Nó lại nhắc cho anh"
line8a = "Nó lại khiến cho     "
line8b = "Đôi mắt nhòe đi"
line8c = " trong màn đêm kia"
line9 = "♪ Những ký ức khiến anh ngã gục"
line10 = "♪ Và rồi"
line10a = "\t để lại nó ở trên giấy mực (yah)"
line11 = "♪ Chẳng nghĩ ra thêm điều gì        "
line12 = "♪ Tình này"
line12a = "\tTheo vốn dĩ đã có kết cục🩶"
line13= "          ●─ Yeah... ─●"

time.sleep(.5)
fade_in_words_non_del(line1, .04, 10)
time.sleep(.3)
show_each_letter(line1a, .08)
print()

time.sleep(.5)
show_fade_in_and_each_letter(line2, .05)
time.sleep(.2)
print()
fade_in_and_move_from_right(40, line2a, .06, 10)

time.sleep(.3)
show_fade_in_and_each_letter(line3, .04)
time.sleep(.2)
print()
fade_in_and_move_from_right(40, line3a, .06, 10)

time.sleep(.5)
show_fade_in_and_each_letter(line4, .04)
print()
time.sleep(.3)
flash_line_fade_in_out_once(line4a, .3)

time.sleep(.5)
show_fade_in_and_each_letter(line5, .03)
print()
time.sleep(.3)
flash_line_fade_in_out_once(line6, .3)

fade_in_words_non_del(line7, .001, 1)
show_each_letter(line7a, .01)
print()
fade_out_text(line7b, .04)
time.sleep(.2)
show_each_letter(line7c, .03)

time.sleep(.5)
fade_in_words_non_del(line8, .001, 1)
show_fade_in_and_each_letter(line8a, .01)
print()
fade_out_text(line8b, .03)
time.sleep(.2)
show_each_letter(line8c, .03)
print()

time.sleep(.5)
fade_out_text(line9, .05)
print()
fade_in_words_non_del(line10, .001, 2)
show_fade_in_and_each_letter(line10a, .03)
print()

time.sleep(.5)
fade_out_text(line11, .05)
print()
fade_in_words_non_del(line12, .001, 2)
print()
show_fade_in_and_each_letter(line12a, .03)
time.sleep(.3)
print()
flash_line_fade_in_out_once(line13,.5)
time.sleep(1)