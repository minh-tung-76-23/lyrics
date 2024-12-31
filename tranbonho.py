import time
import sys
from animation import *

line1 = "𝄞 Bộ nhớ ấy"
line1a = "\t bao nhiêu điều thật quý"
line2 = "♬ Chỉ muốn giữ trong lòng"
line2a = "\t\t\t chớ bay đi"
line3 = "♭ Cạnh bên nhau"
line3a = "\t\t xua đi nhiều cơn đau"
line4 = "♪ Thành tâm với"
line4a = "\tnốt nhạc cứu thân này..."

time.sleep(.5)
fade_in_words_non_del(line1, .01, 10)
print()
time.sleep(.2)
fade_in_text(line1a,0.05)
print()

time.sleep(.8)
show_each_letter(line2, .09)
print()
fade_in_text(line2a, .1)
print()

time.sleep(.2)
fade_in_words_non_del(line3, .01, 10)
print()
fade_in_text(line3a,0.1)
print()

time.sleep(.7)
fade_in_words_non_del(line4, .01, 10)
time.sleep(.6)
print()
if line4a.endswith("..."):
    main_text = line4a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print() 



