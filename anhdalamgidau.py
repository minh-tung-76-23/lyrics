import time
import sys
from animation import *

# Các dòng cần hiển thị
line3 = "Anh đã làm được gì🎧"
line4 = "♪ Đâu"
line4a = " ta đã làm được gì đâu"
line5 = "\t Ta hỏi nhau rất nhiều câu"
line6 = "   ♪   Chúng ta"
line6a = "\t\tsau này"
line7 = " Sẽ bên cạnh hay sẽ vội bước mau..."
line7a = "\t\t●─ 🩶   ─●"
line8 = "♫ Ta sẽ làm được điều đó"
line9 = "    ♫ Ta sẽ băng ngược chiều gió"
line9a = "\t\t\t\t giông kia"
line10 = " Ta vẫn không ngại ngần"
line11 = "♩ Cười lên anh"
line11a = "Đời sẽ chẳng mấy vui"
line12 = "\t Nếu không ồ ạt"
line13 = "\t  ♪ Vỗ về từng con sóng lớn"
line14 = "\t  ♪ Khiến ta càng phải khôn hơn"
line15 = "\t  ♪ Và mạnh mẽ hơn..."
line16 = "♭ Mọi muộn phiền sẽ qua"
line17a = "♪ Chúng ta".ljust(3)
line17 = "\tNắm tay đi hết chặng đường"
line18 = "♭ Miễn đôi mình vui là được"
line18a = " nhé anh..."

#Thực thi
# time.sleep(.5)
fade_in_words(line3, 0.001, 5)
time.sleep(.5)
fade_in_text(line4, .05)
show_each_letter(line4a, .07)
print()

time.sleep(.8)
show_each_letter(line5, .07)
print()

time.sleep(.7)
fade_in_text(line6, .05)
fade_in_text(line6a, .05)
print()

time.sleep(.8)
show_fade_in_and_each_letter(line7, delay=0.09)  
print()
fade_in_text(line7a, .1)
print()

time.sleep(.4)
flash_line_fade_in_out_once(line8, 2)
time.sleep(.4)
fade_in_text(line9, .3)
time.sleep(.4)
fade_in_text(line9a, .09)
print()
fade_in_text(line10, .09)
time.sleep(1.5)
print()

fade_in_words_non_del(line11, .001, 5)
print()
time.sleep(1.5)
show_fade_in_and_each_letter(line11a, 0.07)
print()
time.sleep(.2)
fade_in_text(line12, .09)
print()
time.sleep(1)
flash_line_fade_in_out_once(line13, 2)
time.sleep(.2)
fade_in_text(line14, .3)
print()
fade_in_text(line15, .13)
print()

time.sleep(.5)
show_each_letter(line16, .09)
print()
time.sleep(.5)
fade_in_words_non_del(line17a, .01, 10)
time.sleep(.2)
print()
fade_in_text(line17, .2)
print()
time.sleep(1)
fade_in_text(line18, .15)
time.sleep(.9)
if line18a.endswith("..."):
    main_text = line18a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print() 








