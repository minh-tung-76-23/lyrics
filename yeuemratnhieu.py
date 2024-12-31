import time
import sys
from animation import *

line1 = "   ♪  Những câu chuyện thật dài"
line1a = "\t\t\t\tmỗi tối"
line2 = "     Những phút giây ngập ngừng"
line2a = "\t\t\t\tbối rối"
line3 = "♪ Tiếng em cười và lời em nói"
line4 = "♭ Khiến anh giờ đang"
line4a = " như quên mất lối..."

line5 = " Những khi chạm nhìn vào"
line5a = "\t\t\t đôi mắt"
line6 = "♪ Anh chỉ muốn"
line6a = " ôm em thật chặt"
line7 = "♮ Để anh nói em nghe"
line7a = "Nói em nghe"
line7b = " lòng anh..."

line8 = "🎙️  Người ơi em có biết"
line8a = "Anh đã"
line8b = " yêu em rất nhiều❤️"
line9 = "♬ Chẳng cần những lý lẽ"
line9a = "  Để nói"
line9b = "\t nên câu tình yêu"
line10 = "♯ Làm như không quan tâm"
line10a = "Nhưng anh               "
line10b = "\th thực sự nhớ em"
line11 = "♪ Muốn được chở che cho em"
line11a = "Những đêm lạnh về"
line12 = "𝄞 Anh muốn nói "
line12a = "Yêu em rất nhiều💕..."


show_each_letter(line1, .06)
time.sleep(.2)
fade_in_text(line1a, .08)
print()
time.sleep(.5)
show_each_letter(line2, .06)
time.sleep(.2)
fade_in_text(line2a, .08)
print()
time.sleep(.5)
fade_in_and_move_from_right(35, line3, .08, 30)
time.sleep(.3)
fade_in_text(line4, .08)
time.sleep(.3)
if line4a.endswith("..."):
    main_text = line4a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.6)
print()
time.sleep(.5)
show_each_letter(line5, .07)
time.sleep(.2)
fade_in_text(line5a, .09)
print()
time.sleep(.5)
fade_in_text(line6, .09)
show_each_letter(line6a, .08)
print()

time.sleep(1)
flash_line_fade_in_out_once(line7, 1.5)
time.sleep(.3)
fade_in_text(line7a, .08)
time.sleep(.3)
if line7b.endswith("..."):
    main_text = line7b[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.7)
print()

time.sleep(.5)
flash_line_fade_in_out_once(line8, 1.5)
time.sleep(.3)
fade_in_text(line8a, .09)
show_each_letter(line8b, .1)
print()

time.sleep(1.5)
flash_line_fade_in_out_once(line9, 1.5)
time.sleep(.3)
show_each_letter(line9a, .08)
time.sleep(.5)
fade_in_text(line9b, .2)
print()

time.sleep(2)
show_fade_in_and_each_letter(line10, .045)
time.sleep(.5)
show_fade_in_and_each_letter(line10a, .045)
time.sleep(.3)
fade_in_text(line10b, .2)
print()

time.sleep(2)
fade_in_and_move_from_right(35, line11, .08, 20)
time.sleep(.5)
show_fade_in_and_each_letter(line11a, .07)
print()

time.sleep(.5)
fade_in_text(line12, .09)
print()
time.sleep(.3)
if line12a.endswith("..."):
    main_text = line12a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
print()

