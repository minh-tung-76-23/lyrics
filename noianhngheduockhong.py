import time
import sys
from animation import *

line1 = "Em có biết được không"
line2 = "Điều gì làm con tim đau nhất?"
line3 = "Chẳng phải là khi"
line4 = "Ta nói dối thay cho sự thật"
line5 = "Anh biết là rất khó"
line6 = "Anh biết ngày nào đó"
line7 = "Nếu nhìn lại"
line7a = "    Đã hối tiếc"
line8 = "\t\tvì để đánh mất"
line9 = "Quá khứ là thế"
line10 = "Theo đuôi anh"
line10a = "mỗi khi đêm tới..."
line11 = "Tương lai chẳng đến"
line12 = "Khi anh chẳng thấy"
line12a = "điều gì mới..."
line13 = "Anh chỉ muốn"
line13a = " được thứ tha"
line14 = "Để mọi thứ"
line14a = " qua nhanh và"
line15 = "Chẳng phải chúng ta"
line15a = "đã từng nói"
line16 = "   Sẽ chẳng thể"
line16a = "\t\tcách xa"
line16b = " nhau🩶..."

show_fade_in_and_each_letter(line1, .03)
print()
time.sleep(.3)
fade_in_from_sides(line2, .07, 20)
print()
time.sleep(.5)
show_fade_in_and_each_letter(line3, .03)
print()
time.sleep(.3)
fade_in_from_sides(line4, .07, 20)
print()
time.sleep(.5)

scroll_text(line5, .04, 20)
fade_in_and_move_from_right(40, line6, .06, 20)
show_fade_in_and_each_letter(line7, .03)
print()
time.sleep(.5)
show_each_letter(line7a, .06)
fade_in_text(line8, .06)
print()
time.sleep(1)

fade_in_from_sides(line9, .05, 20)
print()
time.sleep(.2)
fade_in_words_non_del(line10, .01, 1)
if line10a.endswith("..."):
    main_text = line10a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.1)
    print() 

fade_in_from_sides(line11, .04, 20)
print()
time.sleep(.1)
fade_in_words_non_del(line12, .01, 1)
if line12a.endswith("..."):
    main_text = line12a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.1)
    print() 

time.sleep(.3)
fade_in_text(line13, .05)
time.sleep(.1)
show_each_letter(line13a, .04)
print()

time.sleep(.3)
fade_in_text(line14, .05)
time.sleep(.1)
show_each_letter(line14a, .04)
print()

time.sleep(.1)
fade_in_words_non_del(line15, .01, 1)
show_each_letter(line15a, .04)
print()

time.sleep(.2)
fade_in_from_sides(line16, .03, 20)
time.sleep(.2)
fade_in_text(line16a, .04)
time.sleep(.3)
if line16b.endswith("..."):
    main_text = line16b[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print()


# fade_out_from_sides_left(line5, .05, 10)
