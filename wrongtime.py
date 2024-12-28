import time
import sys
from animation import *

# Các dòng cần hiển thị
line1 = "♪ Giấu nước mắt vào trong"
line1a = "  Coi như chuyện đã xong "
line2 = "  ♪ Còn điều gì để nói nữa"
line2a = "Khi thực tâm em chẳng còn mong"
line2b= "\tYeah 🩶"
line3 = "🎧 Em quay đi ta mất nhau"
line4 = "Yêu thương kia đành cất sâu"
line5 = "Con tim anh đã rất đau"
line5a = "𝄫 Đi nơi đâu"
line5b = "\tđể có phép nhiệm màu"
line6 = "   ♪ Anh không muốn phải níu đâu"
line6a = "   ♪ Hai ta chưa từng hiểu nhau"
line7 = "♪ Cứ chạy đi"
line7a = "\tTìm nơi"
line7b = " mà em thấy em thuộc về"
line8 = "♪ Mặc kệ những tiếc nuối"
line8a = "\tTìm tới"
line8b = "\t\tKhi mưa còn rơi"
line9 = "♪ Cơn đau kia anh nhận lấy"
line9a = "\tRiêng anh mà thôi"
line9b = "\t\t Em đâu cần"
line9c = " quay đầu lại"
line10 = "♪ Và chỉ cần một lần cuối"
line10a = "Gỡ những nút thắt"
line10b = "\tQuên đi mắt môi"
line11 = "\t\t♪ 350 xé đôi"
line11a = "\tCơn đau kia sẽ nguôi🩶"

# time.sleep(.5)
show_each_letter(line1, .045)
time.sleep(.2)
show_fade_in_and_each_letter(line1a, .045)
time.sleep(.5)
show_fade_in_and_each_letter(line2, .04)
print()
time.sleep(.2)
fade_in_and_move_from_right(30, line2a, .08, 10)

time.sleep(.2)
flash_line_fade_in_out_once(line2b, 1.5)
print()
show_each_letter(line3, .05)
print()
time.sleep(.2)
fade_in_and_move_from_right(40, line4, .08, 10)

time.sleep(.2)
fade_in_words(line2b, .01, 3)
show_each_letter(line5, .04)
print()
fade_in_words_non_del(line5a, .01, 3)
print()
fade_in_text(line5b, .03)
print()

time.sleep(.5)
flash_line_fade_in_out_once(line6, 1.)
flash_line_fade_in_out_once(line6a, 1.)

fade_in_words_non_del(line7, .01, 2)
print()
fade_in_text(line7a, .01)
time.sleep(.2)
show_each_letter(line7b, .03)
print()

time.sleep(.5)
show_each_letter(line8, .03)
print()
fade_in_text(line8a, .01)
time.sleep(.2)
print()
show_fade_in_and_each_letter(line8b, .045)
print()

time.sleep(.5)
show_fade_in_and_each_letter(line9, .04)
print()
time.sleep(.2)
fade_in_text(line9a, .04)
print()
fade_in_text(line9b, .03)
time.sleep(.2)
# fade_in_words_non_del(line9c, .01, 2)
show_each_letter(line9c, .04)
print()

time.sleep(.5)
show_each_letter(line10, .03)
print()
fade_in_and_move_from_right(35, line10a, .08, 10)
fade_in_text(line10b, .05)
print()

time.sleep(.5)
flash_line_fade_in_out_once(line11, 1.)
flash_line_fade_in_out_once(line11a, 1.)











