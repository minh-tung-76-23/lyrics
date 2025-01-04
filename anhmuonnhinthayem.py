import time
import sys
from animation import * 

line1 = "🎙️Mưa trong anh"
line1c = "\t\t sẽ rơi"
line1a = "Và lại cuốn đi đoạn tình yêu"
line1b = "Chỉ đến thế thôi"
line2 = "Giá như cảm xúc ban đầu"
line2a = "Anh đừng               "
line2b = "\t chôn giấu"
line5 = "Thì đã chẳng quay lưng lên chuyến tàu"
line5a = "Trong vai một người xấu💔"
line7 = "Vì luôn thầm mong em yêu ấm êm"
line9 = "Và đừng như anh"
line9a = "Vỏ lon ngổn ngang"
line9b = "trên bậc thềm"
line11 = "Anh không bao giờ muốn"
line11a = "Một ngày"
line11b = " phải say goodbye"
line13 = "Chỉ là chẳng để điều ấy"
line13a = "Cứ thế diễn ra"
line13b = "Anh đã sai"
line13c = " anh phải đi🩶..."

show_each_letter(line1, .08)
time.sleep(.3)
fade_in_text(line1c, .05)
print()

time.sleep(.5)
fade_in_and_move_from_right(50, line1a, .06, 20)
time.sleep(.5)
fade_in_text(line1b, 0.08)
print()

time.sleep(1)
show_fade_in_and_each_letter(line2, .07)
print()
time.sleep(.2)
show_each_letter(line2a, .05)
time.sleep(.2)
fade_in_text(line2b, .06)
print()

time.sleep(.5)
flash_line_fade_in_out_once(line5, 1)
fade_in_words_non_del(line5a, .04, 2)
print()

time.sleep(1)
show_fade_in_and_each_letter(line7, .07)
print()

time.sleep(.7)
fade_in_and_move_from_right(40, line9, .06, 20)
time.sleep(.3)
fade_in_words_non_del(line9a, .04, 2)
show_each_letter(line9b, .07)
print()

time.sleep(1)
fade_in_words(line11, .01, 4)
time.sleep(.2)
fade_in_text(line11a, .04)
time.sleep(.5)
show_each_letter(line11b, .05)
print()

time.sleep(.7)
show_each_letter(line13, .05)
time.sleep(.3)
fade_in_and_move_from_right(40, line13a, .05, 20)

time.sleep(.3)
fade_in_text(line13b, .03)
time.sleep(.2)
if line13c.endswith("..."):
    main_text = line13c[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.7)








