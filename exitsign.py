import time
import sys
from animation import *

line1 = "🎙️ Không cần phải là người giỏi toán"
line2 = "     Đủ biết đây không phải đổi ngang"
line3 = "  Em chỉ mất đi một thằng thất bại"
line4 = "    Anh mất đi một người yêu anh 🩶  "
line5 = "♪ 8515 lần"
line6 = "\tNói anh yêu em ở trong Mess..."
line7 = "\t\tNếu mà em search"
line8 = "♪ Cũng tới lúc mình phải quên đi thôi"
line9 = "\tDù từng có với nhau"
line10 = "\t\t Là rất nhiều cam kết"
line11 = "♪ Tiếc nhất không phải chia tay"
line12 = "\tMà là không yêu em"
line13 = "\tNhiều hơn trước lúc tình yêu chết"
line14 = "♪ Có lẽ phải ghi tên em vào credit"
line15 = "Vì bài nhạc nào"
line16 = "        ♪ Anh cũng viết về em hết 🩶"

line71 = "♪ Em hiểu rằng"
line81 = "       Chúng ta"
line81a = "\t\tkhông ai là sai"
line91 = "   ♪ Chỉ là em không muốn"
line101 = "Em mãi sẽ là lựa chọn thứ hai"
line111 = "♪ Mãi sau những điều"
line121 = "   Anh cho là lý do"
line131 = "\tĐể anh tồn tại"
line141 = "   Vậy đâu còn lý do"
line151 = "\tĐể em ở lại"
line161 = "♪ Đây sẽ là lý do"
line171 = "\tEm sẽ thôi đắn đo      "
line181 = "\tCứ ôm mộng hoài"
line191 = "♪ So thanks for showing me the exit sign🩶..."


show_each_letter(line1, 0.03)
print()
time.sleep(.2)
show_each_letter(line2, 0.03)
print()
time.sleep(.2)

show_each_letter(line3, 0.04)
time.sleep(.2)
flash_line_fade_in_out_once(line4, 1)

time.sleep(.2)
fade_in_words_non_del(line5, .01, 4)
print()
fade_in_text(line6, .05)
time.sleep(.2)
print()
show_each_letter(line7, 0.04)
print()

time.sleep(.3)
fade_in_text(line8, .07)
print()
fade_in_words_non_del(line9, .01, 1)
print()
show_each_letter(line10, 0.02)
print()

time.sleep(.5)
fade_in_and_move_from_right(30, line11, .06, 10)
fade_in_words_non_del(line12, .01, 1)
print()
fade_in_text(line13, .05)
print()

time.sleep(.3)
show_each_letter(line14, 0.02)
print()
fade_in_and_move_from_right(30, line15, .08, 10)
flash_line_fade_in_out_once(line16, .5)


time.sleep(.5)
flash_line_fade_in_out_once(line71, .5)
show_each_letter(line81, 0.02)
fade_in_text(line81a, .1)
print()

time.sleep(1)
flash_line_fade_in_out_once(line91, 1)
flash_line_fade_in_out_once(line101, 2)

time.sleep(.2)
show_each_letter(line111, 0.07)
time.sleep(.4)
fade_in_and_move_from_right(30, line121, .09, 10)
time.sleep(1.5)
fade_in_text(line131, 0.08)
print()

time.sleep(.2)
fade_in_and_move_from_right(30, line141, .09, 10)
time.sleep(1.2)
fade_in_text(line151, .09)
print()

time.sleep(.2)
show_each_letter(line161, 0.09)
print()
time.sleep(.5)
fade_in_and_move_from_right(30, line171, .07, 10)
time.sleep(.2)
fade_in_text(line181, .075)
print()

time.sleep(.2)
if line191.endswith("..."):
    main_text = line191[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print() 


