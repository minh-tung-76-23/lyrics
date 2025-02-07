import curses
import time
from animation import *

line1 = "Tình yêu"
line1a = " vốn đâu có luật lệ"
line2 = "Nhưng nếu tôi có"
line2a = "\tliệu anh có "
line2b = "mặc kệ bỏ qua?"
line3 = "Không muốn nghe những hứa hẹn lời thề"
line4 = "Không muốn chỉ là một người thay thế"
line5 = "Tôi vốn"
line5a = " cũng đâu có luật lệ"
line6 = "Tình yêu khó đoán"
line6a = "nên tôi cần phải tự vệ"
line7 = "Dành cho nhau sự chấp nhận và yêu thương  "
line8 = "Mặc dù"
line8b = "nhiều khi"
line8a = "Chúng là thứ khiến ta mất phương hướng    "
line9 = "🎧 Nên là tình yêu tôi nói không"
line10 = "Không thích cảm giác phải ngóng trông"
line11 = "Không muốn phải thấy một ai"
line11a = "Đi mất để tôi lại khổ"
line12 = "     Càng không"
line12b = "\t\tmuốn thấy"
line12a = "Ai vì tôi mà cũng phải khổ"
line13 = "Nên là"
line13a = " nếu có tìm đến tôi"
line14 = "Nếu có thực sự cần đến tôi"
line14b = "          ●─ 💔  ─●"
line15 = "Xin hãy dạy tôi biết thế nào là yêu"
line16 = "Đừng lại rời xa"
line16a = "\tĐể tôi mới biết"
line16b = " mình đang yêu💔?"
line17 = "Somebody tell me how to love?"

fade_in_text(line1, .04)
time.sleep(0.3)
show_each_letter(line1a, .07)
print()
time.sleep(1)

show_fade_in_and_each_letter(line2, .06)
print()
time.sleep(0.2)
fade_in_text(line2a, .06)
time.sleep(0.2)
show_each_letter(line2b, .06)
print()
time.sleep(0.5)

flash_line_fade_in_out_once(line3, 2)
time.sleep(1)
flash_line_fade_in_out_once(line4, 2)
time.sleep(1)

time.sleep(0.5)
fade_in_text(line5, .06)
time.sleep(0.2)
show_each_letter(line5a, .06)
print()
time.sleep(0.5)

fade_in_words_non_del(line6, .001, 1)
show_each_letter(line6a, .09)
time.sleep(1)
show_fade_in_and_each_letter(line7, .06)
print()
time.sleep(0.5)
fade_in_words_non_del(line8, .001, 1)
show_each_letter(line8b, .04)
print()
time.sleep(.3)
show_fade_in_and_each_letter(line8a, .06)
print()

time.sleep(0.2)
fade_in_from_sides(line9, .07, 20)
time.sleep(1)
fade_out_from_sides_left(line10, .15, 20)

show_fade_in_and_each_letter(line11, .07)
print()
time.sleep(0.5)
fade_in_and_move_from_right(40, line11a, .08, 10)

time.sleep(0.5)
fade_in_words_non_del(line12, .001, 1)
time.sleep(0.5)
fade_in_text(line12b, .06)
print()
time.sleep(0.5)
fade_in_and_move_from_right(40, line12a, .08, 10)

time.sleep(0.3)
fade_in_text(line13, .06)
time.sleep(0.2)
show_each_letter(line13a, .06)
print()
time.sleep(1)
fade_in_from_sides(line14, .07, 20)
print()

time.sleep(1)
fade_in_from_sides(line14b, .09, 20)
time.sleep(1)

show_fade_in_and_each_letter(line15, .05)
print()
time.sleep(.3)
fade_in_from_sides(line16, .04, 20)
print()

time.sleep(0.3)
fade_in_text(line16a , .04)
time.sleep(0.3)
show_each_letter(line16b, .08)
print()

time.sleep(1)
flash_line_fade_in_out_once(line17, 2)





