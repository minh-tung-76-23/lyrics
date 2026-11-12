import time
import sys
from animation import * 

line1 = "Vì chắc có lẽ do đôi mình sai"
line2 = "Ngay khi bắt đầu             "
line3 = "Chuyện tình mình đã"
line3a = "cuốn theo làn mây"
line4 = "Trôi đi mất rồi"
line5 = "Dặn lòng này "
line5a = "chẳng thể quên được em"
line6 = "Sao đây hỡi người"
line7 = "Vì lòng này"
line7a = "..."
line8 = "\tĐã trót yêu một ai"
line9 = "Yêu đến suốt đời"
line10 = "Tình mình giờ chắc"
line10a = " chỉ đến vậy thôi"
line11 = "Không nên cất lời"
line12 = "Và lòng chỉ muốn"
line12a = " có em ở bên"
line13 = "Nhưng sao chẳng còn"
line14 = "Chẳng còn gì thương đau"
line15 = "Và anh ước"
line15a = "Ta không"
line15b = " xa nhau🩶..."

# time.sleep(.5)
fade_in_words_non_del(line1, .01, 1)
time.sleep(.3)
show_fade_in_and_each_letter(line2, .05)
print()

fade_in_words_non_del(line3, .01, 1)
time.sleep(.2)
show_each_letter(line3a, .04)
print()
time.sleep(.5)
fade_in_and_move_from_right(30,line4, 0.04, 20)   

time.sleep(.3)
fade_in_from_sides(line5, .02, 10)
show_each_letter(line5a, .05)
time.sleep(.5)
fade_in_and_move_from_right(36,line6, 0.05, 20)   

time.sleep(1)
fade_in_from_sides(line7, .05, 10)
if line7a.endswith("..."):
    main_text = line7a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.75)
    print() 

time.sleep(.3)
fade_in_words_non_del(line7, .01, 1)
print()
fade_in_text(line8, .09)
print()

time.sleep(.5)
fade_in_and_move_from_right(30,line9, 0.05, 20)   
time.sleep(.5)
color_splash_effect(line10, .04, 10)
time.sleep(.2)
show_each_letter(line10a, .05)
print()
time.sleep(.5)
fade_in_and_move_from_right(30,line11, 0.05, 20)   

time.sleep(.2)
color_splash_effect(line12, .04, 10)
time.sleep(.2)
show_each_letter(line12a, .05)
print()
time.sleep(.8)
fade_in_and_move_from_right(30,line13, 0.05, 20)   

time.sleep(.5)
random_flicker(line14, .09, 10)
print()
time.sleep(1)
fade_in_from_sides(line15, .02, 10)
print()
time.sleep(.5)
fade_in_text(line15a, .02, 10)
time.sleep(1)
if line15b.endswith("..."):
    main_text = line15b[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print() 




