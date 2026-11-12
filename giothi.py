import time
import sys
from animation import *

line1 = "♪ Cho anh quay lại khoảnh khắc ấy"
line1a = "     Để anh cố níu tay em lại"
line1b = "          ●─🩶  ─●"
line2 = "♬ Giờ thì mình đã..."
line2a = "\tKhông còn thương"
line3 = "\tKhông còn đau"
line4 = "\tKhông còn vì nhau nữa"
line5 = "♪ Cũng đã từng mang nhiều điều mong ước"
line5a = "nhưng đành xa xôi"
line6 = "♪ Bỏ quên những dấu yêu bao ngày"
line6a = "ở lại đằng sau"
line7 = "♭ Ta bước tiếp trên"
line7a = "\tĐoạn đường"
line7b = " chẳng có nhau"
line8 = "♩ Nỗi đau ấy"
line8a = "\t\trồi sẽ thay bằng"
line8b = "♮ Niềm hạnh phúc của riêng mỗi người..."

line9 = "♪ Rồi mình sẽ trưởng thành hơn kiên cường hơn không còn như lúc trước"
line10 = "♪ Em sẽ dần quên từng đêm khóc nấc trên đôi vai này"
line11 = "♪ Ngày em có đến bên ai trong đời"
line12 = "♪ Thật tâm vẫn chúc em luôn vui cười"
line13 = "♪ Vì anh yêu em rất nhiều, chỉ là chúng ta chọn rời xa"

time.sleep(1)
show_each_letter(line1, .06)
time.sleep(.5)
print()
fade_in_text(line1a, .2)
print()

time.sleep(.5)
flash_line_fade_in_out_once(line1b, 3)

time.sleep(.3)
fade_in_words_non_del(line2, .03, 5)
print()

time.sleep(.1)
fade_in_text(line2a, .08)
print()
time.sleep(.6)
fade_in_text(line3, .08)
print()
time.sleep(.6)
fade_in_text(line4, .15)
print()

time.sleep(.8)
show_each_letter(line5, .05)
print()

time.sleep(.5)
fade_in_and_move_from_right(40, line5a, .09, 10)

time.sleep(2.5)
show_each_letter(line6, .08)
print()
time.sleep(.7)
fade_in_and_move_from_right(40, line6a, .08, 10)

time.sleep(.4)
fade_in_and_move_from_right(30, line7, .05, 10)
time.sleep(.2)
fade_in_text(line7a, .03)
time.sleep(.5)
show_each_letter(line7b, .05)

print()
time.sleep(.3)
show_fade_in_and_each_letter(line8, delay=0.08)
time.sleep(.3)
print()
fade_in_text(line8a, delay=0.05)
print()

time.sleep(.5)
if line8b.endswith("..."):
    main_text = line8b[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print() 












