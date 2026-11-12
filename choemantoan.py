import time
import sys
from animation import * 

line1 = "Họ thường nói"  
line2 = "Ai khi xem tình yêu quý hơn vàng"  
line3 = "Đem cho ta những cảm giác an toàn"  
line4 = "Không cần lo xa"  
line5 = "Vì"  
line5a = "không ai đổi thay"  
line6 = "Chỉ cần nhớ"  
line7 = "Ai luôn ngay phía sau"  
line8 = "Ai cho em vòng tay êm ái"  
linea = "      ●─🩶  ─●"
line9 = "Không cho ai"  
line9a = "làm em phải đau"  
line10 = "Cho"  
line10a = " Cho em an toàn"  
line12 = "Từ trong 🩶 "  
line12a = "này đây..."  

fade_in_words_non_del(line1, .001, 1)
print()
time.sleep(1)
flash_line_fade_in_out_once(line2, 2)
time.sleep(.3)
flash_line_fade_in_out_once(line3, 1)
time.sleep(1)
fade_in_words_non_del(line4, .001, 1)
time.sleep(.6)
fade_in_words_non_del(line5, .001, 1)
time.sleep(.2)
show_each_letter(line5a, .06)
print()

time.sleep(1.5)
fade_in_words_non_del(line6, .001, 1)
print()
time.sleep(.6)
flash_line_fade_in_out_once(line7, 2)
time.sleep(.5)
fade_in_from_sides(line8, .06, 20)
print()
time.sleep(1)
flash_line_fade_in_out_once(linea, 2)

time.sleep(.5)
fade_in_words_non_del(line9, .001, 1)
time.sleep(.2)
show_each_letter(line9a, .06)
print()
time.sleep(1)

fade_in_text(line10, .06)
time.sleep(.5)
fade_in_words_non_del(line10a, .001, 1)
time.sleep(.5)

fade_in_text(line10, .06)
time.sleep(.5)
show_each_letter(line10a, .09)
print()
time.sleep(2.5)

fade_in_words_non_del(line12, .05, 5)
time.sleep(.2)
if line12a.endswith("..."):
    main_text = line12a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.15) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.6)
    print()














