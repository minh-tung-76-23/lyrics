import time
import sys
from animation import *

line1 = "Em đã có cho mình"
line1a = "  Một bận tâm mới💔"
line2 = "Anh cũng đã cho mình"
line2a = "   Một câu trả lời  "
line3 = "Có nuối tiếc cũng vậy thôi"
line4 = "Trả nhau"
line4a = "\t tự do"
line4b = "Tình yêu"
line4c = " như gió cuối trời"
line5 = "Dù rằng còn yêu em đến thế"
line5a = "  ♬ Nhưng không"
line5b = "\t\tthành lời"
line6 = "Buồn nào rồi chẳng nguôi"
line6a = "    ♬ Tội người"
line6b = "\t\tsắp tới"
line7 = "Nỗi đau vốn đã thế rồi"
line7a = "Nhân duyên vốn ở thiên thời"
line9 = "Nhưng sao đơn phương lại cứ mãi chờ đợi🩶..."

time.sleep(5)
fade_in_words_non_del(line1, .01, 3)
time.sleep(.2)
fade_in_from_sides(line1a, .05, 25)
print()
time.sleep(.5)


fade_in_words_non_del(line2, .01, 3)
time.sleep(.2)
fade_in_from_sides(line2a, .05, 25)
print()
time.sleep(.5)

show_fade_in_and_each_letter(line3, .06)
print()
time.sleep(.3)
fade_in_text(line4, .06)
time.sleep(.5)
fade_in_text(line4a, .06)
print()
time.sleep(.5)
fade_in_text(line4b, .06)
time.sleep(.2)
show_each_letter(line4c, .07)
print()
time.sleep(.5)
fade_out_by_char(line5, .06, 10)
time.sleep(.2)
fade_in_text(line5a, .06)
time.sleep(.5)
fade_in_text(line5b, .06)

print()
time.sleep(.5)
show_fade_in_and_each_letter(line6, .06)
print()
time.sleep(.2)
fade_in_text(line6a, .06)
time.sleep(.5)
fade_in_text(line6b, .06)
print()
time.sleep(.3)

flash_line_fade_in_out_once(line7, 3)
time.sleep(.2)
fade_in_from_sides(line7a, .06, 30)
print()
time.sleep(.5)
if line9.endswith("..."):
    main_text = line9[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.7)
    print() 