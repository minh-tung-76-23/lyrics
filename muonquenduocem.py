import time
from animation import *     

line1 = "Sau tất cả lời đối đáp"
line2 = "Trao cả hai một lối thoát"
line3 = "Và giờ anh có thể nói🩶"
line3a = " Xin cảm ơn"
line4 = "Yêu nhau"
line4a = " ta tính tháng"
line4b = "\t\t\ttính năm"
line5 = "Chia tay"
line5a = "  ta tính phút"
line5b = "\t\t\ttính giây"
line6 = "Cô đơn"
line6a = " từ xuân tới đông sang"
line7 = "Quán quen"
line7a = " ta chẳng còn lui đến đây"
line8 = "Gia đình anh"
line8a = " cũng hỏi em thế nào"
line9 = "Ở đâu"
line9a = "\tvà công việc giờ ra sao"
line10 = "Đừng vì cô đơn tìm ai thay thế vào"
line11 = "Màu son từng hôn nhau 🩶"

fade_in_from_sides(line1, .06, 15)
fade_out_from_sides_left(line2, .07, 20)
fade_out_by_char(line3, .05, 20)

fade_in_words(line3a, .05, 1)

time.sleep(.2)
fade_in_words_non_del(line4, .01, 5)
time.sleep(.3)
show_each_letter(line4a, .07)
fade_in_text(line4b, .04)
print()

time.sleep(.2)
fade_in_words_non_del(line5, .01, 5)
time.sleep(.3)
show_each_letter(line5a, .07)
fade_in_text(line5b, .04)
print()

time.sleep(.3)
fade_in_text(line6, .06)
time.sleep(.2)
show_each_letter(line6a, .07)
print()

time.sleep(.3)
fade_in_text(line7, .06)
time.sleep(.2)
show_each_letter(line7a, .07)
print()

fade_in_words_non_del(line8, .01, 5)
print()
time.sleep(.3)
fade_in_and_move_from_right(40, line8a, .06, 10)
time.sleep(.3)
fade_in_words_non_del(line9, .01, 5)
time.sleep(.3)
fade_in_from_sides(line9a, .06, 15)
print()

time.sleep(.5)
show_fade_in_and_each_letter(line10, .09 )
print()
time.sleep(1)
fade_in_words_non_del(line11, .01, 4)



