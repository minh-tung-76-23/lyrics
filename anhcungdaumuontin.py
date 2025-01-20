import time
import sys
from animation import * 

line1 = "Giá lúc ấy ta không gặp"
line1a = "\t❤️ "
line1b = " sẽ không"
line1c = " \t\tLìa thành đôi💔         "
line2 = "🎧  Kết thúc câu chuyện thật rồi"
line3 = "Bước đi"
line3a = "\tkhông một lời"
line4 = "Nước mắt đã thôi rơi"
line4a = "Giờ thì hai đứa"
line4b = "hai nơi"
line5 = "Em sẽ viết tiếp những câu chuyện"
line6 = "Giấc mơ"
line6a = "\tchưa thành hình"
line6b = "Giấu cơn mưa lòng mình"
line7 = "Và chuyện tình cũng đã"
line7a = " nhạt phai..."

time.sleep(1)
fade_from_sides(line1, 0.06, 10)
time.sleep(.2)
fade_in_text(line1a,.05)
time.sleep(.3)
show_each_letter(line1b, .04)
print()
time.sleep(.3)
fade_in_and_move_from_right(35, line1c, 0.06, 20)   
time.sleep(.3)
flash_line_fade_in_out_once(line2, 1)
time.sleep(.3)
show_each_letter(line3, .04)
time.sleep(.3)
fade_in_text(line3a,.06)
print()
time.sleep(.3)
typewriter_effect(line4, .04)
print()
time.sleep(.3)
fade_in_words_non_del(line4a, .01, 1)
time.sleep(.3)
show_each_letter(line4b, .04)
print()
time.sleep(.5)
fade_out_from_sides(line5, .09, 20)
time.sleep(.3)
fade_in_from_sides(line6, .02, 10)
time.sleep(.3)
fade_in_text(line6a,.06)
print()
time.sleep(.3)
fade_out_from_sides_left(line6b, .06, 20)
time.sleep(.3)
fade_in_text(line7,.04)
time.sleep(.5)
if line7a.endswith("..."):
    main_text = line7a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print() 










