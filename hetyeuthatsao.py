import time
from animation import *     

line1 = "Người ta nói"
line1a = " 🎙️  Yêu"
line1b = "\t  là chẳng màng"
line2 = "\t\t\tcho hết đi"
line3 = "\t là đợi chờ"
line3a = "\t\t chẳng thấy gì"
line4 = "Tình yêu vốn đến"
line4a = "    Từ nhịp đập"
line4b = "\t\thai trái tim"
line5 = "   Và anh sẽ là người   "
line6 = " Đem về lại những giấc mơ"
line7 = "  Ủa mình hết yêu nhau rồi?"
line8 = "    Hết yêu thật sao?💔"

print()
print()
time.sleep(.5)
show_fade_in_and_each_letter(line1, .06)
print()
time.sleep(.2)
fade_in_text(line1a, .06)
time.sleep(.5)
fade_in_words_non_del(line1b, .02, 5)
time.sleep(.5)
fade_in_text(line2, .15)
print()

time.sleep(.3)
fade_in_words_non_del(line1, .02, 5)
print()
time.sleep(.2)
fade_in_text(line1a, .06)
time.sleep(.5)
fade_in_words_non_del(line3, .02, 5)
print()
time.sleep(.5)
fade_in_text(line3a, .15)
print()
time.sleep(.2)

fade_in_words_non_del(line4, .02, 5)
print()
time.sleep(.5)
show_each_letter(line4a, .06)
time.sleep(.5)
fade_in_text(line4b, .15)
print()
time.sleep(.5)

fade_in_from_sides(line5, .09, 30)
print()
time.sleep(.5)
show_fade_in_and_each_letter(line6, .06)
print()
time.sleep(.5)

flash_line_fade_in_out_once(line7, 2)
time.sleep(.5)
flash_line_fade_in_out_once(line8, 3)



