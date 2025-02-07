import curses
import time
from animation import *
print("\n\n")
line1 = "Giá như anh cố yêu em"
line1a = " nhiều hơn nữa"
line2 = "Giá như anh đã không               "
line2a = "\thững hờ"
line2b = " lúc xưa"
line3 = "Chỉ vì anh quá tin là em"
line3a = "\tSẽ mãi thuộc về anh"
line4 = "Vậy mà giờ đây"
line4a = " hai đứa hai nơi"
line5 = "Hình bóng em giờ đã trôi xa"
line5a = " về nơi đâu"
line6 = "Trái tim anh vẫn mong"
line6a = "\t\t mong em sẽ quay về"
line7 = "Về đâu để thấy em người ơi"
line8 = "Giờ biết đi về đâu"
line9 = "Để một lần nữa"
line9a = "\tđược nhìn thấy nhau"
line10 = "Chỉ còn những nước mắt nhạt nhòa"
line11 = " Hòa vào cơn mơ"
line11a = "\t\tvì anh nhớ em"
line12 = "Chợt tỉnh giữa đêm"
line12a = "Thắt tim lại"
line13 = "Chợt nhận ra"
line13a = "\tem đã đi"
line13b = " thật xa🩶..."


fade_in_text(line1, .09)
time.sleep(0.3)
show_each_letter(line1a, .07)
time.sleep(1)

show_fade_in_and_each_letter(line2, .04)
print()
time.sleep(0.3)
fade_in_text(line2a, .05)
time.sleep(0.3)
show_each_letter(line2b, .07)
print()

time.sleep(1)
fade_in_from_sides(line3, .07, 20)
print()
time.sleep(0.6)
show_fade_in_and_each_letter(line3a, .06)
print()

time.sleep(.5)
fade_in_text(line4, .08)
time.sleep(0.3)
show_each_letter(line4a, .07)
print()

time.sleep(1.5)
fade_in_text(line5, .09)
time.sleep(1)
show_each_letter(line5a, .07)
print()
time.sleep(1)

show_fade_in_and_each_letter(line6, .06)
time.sleep(0.3)
fade_in_text(line6a, .09)
time.sleep(2)
print()

flash_line_fade_in_out_once(line7, 2)
flash_line_fade_in_out_once(line8, 1)
time.sleep(.3)
fade_in_from_sides(line9, .04, 20)
print()
time.sleep(0.3)
show_fade_in_and_each_letter(line9a, .06)
print()

time.sleep(.5)
flash_line_fade_in_out_once(line10, 2)
time.sleep(1)
show_fade_in_and_each_letter(line11, .06)
time.sleep(0.3)
fade_in_text(line11a, .15)
time.sleep(0.5)
print()
flash_line_fade_in_out_once(line12, 2)
time.sleep(1)
flash_line_fade_in_out_once(line12a, 1)

time.sleep(.5)
fade_in_from_sides(line13, .07, 20)
print()
time.sleep(0.5)
fade_in_text(line13a, .09)

time.sleep(0.3)
if line13b.endswith("..."):
    main_text = line13b[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print()







