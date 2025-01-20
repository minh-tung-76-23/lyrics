import time
import sys
from animation import *

line1 = "Từng bước chân đi vào phòng"
line2 = "Anh giấu cơn đau vào lòng"
line3 = "Vì vết thương"
line3a = " chỉ là bên ngoài"
line4 = "Nỗi đau"
line4a = "\tmới thêm dài"
line5 = "Quá khứ"
line5a = "kia em đã"
line5b = "\t\ttừng chôn vùi"
line5c = " bên ai"
line6 = "Và tình yêu kia vụt tắt"
line6a = "\tLike a city in the night"
line7 = "Anh cầm đôi tay để níu"
line7a = " giữ"
line7b = "\tNhưng không thấy em ở lại"
line8 = "Anh biết là"
line8a = "sẽ đau"
line8b = "\tKhi thấy em"
line8c = " buồn sầu"
line9 = "Đợi chờ là"
line9a = "\tlà sẽ lâu"
line9b = "\tTa chẳng thể"
line9c = " giống như ngày đầu..."

fade_out_from_sides_left(line1, .07, 20)
time.sleep(.3)
fade_out_from_sides(line2, .07, 20)
time.sleep(.3)
fade_in_text(line3, .07)
time.sleep(.3)
show_each_letter(line3a, .05)
print()
time.sleep(.3)
show_fade_in_and_each_letter(line4, .05)
time.sleep(.3)
fade_in_text(line4a, .07)
print()

time.sleep(.5)
fade_in_words_non_del(line5, .01, 1)
time.sleep(.3)
show_each_letter(line5a, .06)
print()
time.sleep(.3)
fade_in_text(line5b, .06)
time.sleep(.3)
show_each_letter(line5c, .2)
print()

time.sleep(.3)
fade_in_from_sides(line6, .07, 20)
print()
time.sleep(.2)
show_fade_in_and_each_letter(line6a, .05)
print()

time.sleep(.5)
fade_in_from_sides(line7, .07, 20)
time.sleep(.2)
show_each_letter(line7a, .1)
print()
time.sleep(.1)
show_fade_in_and_each_letter(line7b, .05)
print()

time.sleep(.5)
fade_in_words_non_del(line8, .01, 1)
time.sleep(.2)
show_each_letter(line8a, .07)
print()
time.sleep(.2)
fade_in_from_sides(line8b, .04, 20)
time.sleep(.1)
show_each_letter(line8c, .08)
print()

time.sleep(.3)
show_fade_in_and_each_letter(line9, .05)
time.sleep(.2)
fade_in_text(line9a, .04)
print()

time.sleep(.3)
fade_in_from_sides(line9b, .03, 10)
time.sleep(.1)
if line9c.endswith("..."):
    main_text = line9c[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.5)
    print()







