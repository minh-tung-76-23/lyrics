import time
import sys
from animation import *

line1 = "Liệu người ấy có yêu em "
line1a = "\t\t\t  chân"
line1b = "\t\t\t\tthành"
line2 = "    Nếu khóc cứ"
line2a = "\t\t chạy"
line2b = "\t\t chạy lại"
line2c = "\t\t chạy lại với anh"
line3 = "♬ Gom hết"
line3a = "\t\tnỗi đau này lên bờ vai"
line3c = "\t\t\t\tđể chữa lành"
line4 = "\tChân thành đổi lại gì đâu,"
line4a = "♬ Chỉ toàn phải chứng kiến thấy"
line5 = "\t▶ Em đau"
line5a = "\t▶ Anh đau"
line5b = "\t▶ Ta đau"
line5c = "  Sao cứ phải"
line5d = "\t\t\t xa nhau"
line6 = "♪ Anh cứ hy vọng"
line6a = " Rồi ôm về mình mớ"
line6b = "\t\tmớ thất vọng"
line7 = "♬ Những gì đã từng hứa"
line7a = "\t Giờ đây cũng chỉ là"
line8 = "\t\t🩶 Lời bông đùa..."

print()
time.sleep(.5)
show_fade_in_and_each_letter(line1, .06)
time.sleep(.5)
fade_in_text(line1a, 0.09)
fade_in_text(line1b, 0.09)
print()

time.sleep(.5)
show_fade_in_and_each_letter(line2, .06)
fade_in_text(line2a, 0.09)
fade_in_text(line2b, 0.09)
fade_in_text(line2c, 0.09)
print()

fade_in_and_move_from_right(40, line3, .02, 20)
fade_in_text(line3a, .09)
print()
time.sleep(.1)
show_fade_in_and_each_letter(line3c, .08)
print()

time.sleep(.8)
show_fade_in_and_each_letter(line4, .05)
print()
time.sleep(.8)
show_each_letter(line4a, .07)
print()
flash_line_fade_in_out_once(line5, .5)
flash_line_fade_in_out_once(line5a, .5)
flash_line_fade_in_out_once(line5b, .5)
show_each_letter(line5c, .01)
flash_line_fade_in_out_once(line5d, 1)
fade_in_text(line5d, .09)
print()

time.sleep(.9)
fade_in_words_non_del(line6, .01, 10)
print()
show_each_letter(line6a, .07)
fade_in_text(line6b, .09)
print()

time.sleep(.9)

fade_in_and_move_from_right(30, line7, .05, 20)
fade_in_text(line7a, .09)
print()

time.sleep(.2)
if line8.endswith("..."):
    main_text = line8[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print()


