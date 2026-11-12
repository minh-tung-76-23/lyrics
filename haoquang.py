import time
import sys
from animation import * 

line1 = "Khi anh đã có tất cả rồi"
line2 = "Lại chẳng còn em nữa"
line3 = "Khi ta đã đủ sự trưởng thành"
line4 = "      Lại chẳng dành nó"
line4a = "\t\t\tcho đối phương"
line5 = "Tình yêu này có"
line5a = "\t\tthật đáng thương..."
line6 = "Ở phía dưới"
line6a = " ngọn đèn"
line6b = "Có gã khờ đang hát"
line7 = "Cố gắng"
line7a = " mỉm cười"
line7b = "Nhưng trong lòng tan nát"
line8 = "Mất đi người rất quan trọng"
line9 = "Có lẽ vì"
line9a = " quá tham vọng🩶..."

time.sleep(.5)
fade_in_words(line1, .001, 3)
time.sleep(.3)
fade_in_text(line2, .09)
print()
time.sleep(.5)
fade_in_words(line3, .001, 3)
time.sleep(.3)
show_fade_in_and_each_letter(line4, .07)
time.sleep(.3)
fade_in_text(line4a, .09)
print()

time.sleep(.5)
show_fade_in_and_each_letter(line5, .07)
time.sleep(.3)
fade_in_text(line5a, .15)
print()

time.sleep(1)
color_splash_effect(line6, .05, 10)
time.sleep(.5)
show_each_letter(line6a, .06)
print()
time.sleep(.3)
fade_in_from_sides(line6b, 0.1, 10)
print()

time.sleep(.5)
color_splash_effect(line7, .04, 10)
time.sleep(.5)
show_each_letter(line7a, .05)
print()
time.sleep(.3)
fade_in_from_sides(line7b, 0.1, 10)
print()

time.sleep(1)
fade_in_and_move_from_right(40,line8, 0.09, 20)      

time.sleep(2)
fade_in_text(line9, .06)
time.sleep(0.3)
if line9a.endswith("..."):
    main_text = line9a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print() 



