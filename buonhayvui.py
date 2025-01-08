import time
import sys
from animation import *

red = "\033[91m"  # Mã đỏ
reset = "\033[0m"  # Reset màu về mặc định

line1 = f"{red} Hurt, hurt,{reset}"
line1a = "baby "
line1b = f"Rất,{red} rất đau💔 {reset}"
line2b = f"    {red}Rất {reset}               "
line2c = "\trất đau💔"

line3 = "🎙️  Baby, 2 A.M in the morning "
line4 = "Tự hỏi dòng suy nghĩ của em ra sao"
line4a = "\tYou got me fallin'"
line5 = "Girl, ain't no trap, just good vibe "
line5a = "\tWhen you callin"
line6 = "Chỉ cần dòng tin nhắn đến đón em"
line6a = "        I'ma ballin             "
line7 = "Đừng để trái tim ta phai tàn"
line7a = "Để nụ hồng lại héo đi"
line8 = "Nước mắt rơi trong đêm lạnh"
line8a= "Nụ cười nàng lại méo đi"
line9 = "Cứ trao nhau môi ngọt"
line9a = "Bảo chuyện buồn nó xéo đi"
line10 = "Hãy cứ khóc đi"
line10a = "\t\tAnh đây rồi"
line10b = "Tay người đâu anh kéo đi..."

fade_in_words_non_del(line1, .001, 10)
show_each_letter(line1a, .04)
print()
time.sleep(.3)
fade_in_words_non_del(line1b, .001, 10)
print()

fade_in_words_non_del(line1, .001, 10)
show_each_letter(line1a, .04)
time.sleep(.3)
fade_in_text(line2b, .02)
time.sleep(.2)
fade_in_text(line2c, .03)
time.sleep(.3)
show_fade_in_and_each_letter(line3, .06)
print()

time.sleep(.5)
show_each_letter(line4, .04)
print()
time.sleep(.2)
fade_in_text(line4a, .05)
print()

time.sleep(.5)
show_each_letter(line5, .04)
print()
time.sleep(.2)
fade_in_text(line5a, .05)
print()

time.sleep(.5)
show_fade_in_and_each_letter(line6, .04)
time.sleep(.2)
flash_line_fade_in_out_once(line6a, .5)

show_each_letter(line7, .04)
print()
time.sleep(.3)
fade_in_and_move_from_right(40, line7a, .06, 10)
time.sleep(.5)

show_each_letter(line8, .04)
print()
time.sleep(.3)
fade_in_and_move_from_right(40, line8a, .06, 10)
time.sleep(.5)

show_each_letter(line9, .04)
print()
time.sleep(.3)
fade_in_and_move_from_right(40, line9a, .06, 10)
time.sleep(.5)

fade_in_words_non_del(line10, .001, 1)
fade_in_text(line10a, .04)
print()
time.sleep(.3)
show_fade_in_and_each_letter(line10b, .04)


