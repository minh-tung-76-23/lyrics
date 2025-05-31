import time
import sys
from animation import *

line1 = "Đừng yêu"  
line1a = "\t anh"  
line1b = "\t\tnữa"  
line2 = "Cũng đừng"  
line2a = "\tg khóc"  
line2b = "\t\t nữa"  
line3 = "Hai chúng ta từ nay"  
line4 = "Không cùng lối"  
line4a = "cũng chẳng chung đường"  
line5 = "Cớ sao lại"  
line5a = " yêu anh đến thế"  
line6 = "Bởi anh đâu"  
line6a = " cho em nụ cười"  
line7 = "Thế giới có bao người"  
line8 = "     Tốt hơn người giống như anh"  
line8a = "\t\t\t\t em hỡi"  
line9 = "Cuộc đời anh như"  
line9a = " sóng vỗ"  
line9b = "\t\t\t lênh đênh"  
line10 = "Làm thuyền em không"  
line10a = " bến đỗ"  
line10b = "\t\t\tđỗ chênh vênh"  
line11 = "Một người như anh"  
line12 = "Chỉ làm em thêm"  
line12a = "\t\tđớn"  
line12b = " đau🩶..."  

fade_in_words_non_del(line1, .05, 5)
time.sleep(.5)
fade_in_text(line1a, .05, 10)
time.sleep(.2)
fade_in_text(line1b, .05, 20)
print()
time.sleep(.3)

fade_in_words_non_del(line2, .05, 5)
time.sleep(.5)
fade_in_text(line2a, .05, 10)
time.sleep(.2)
fade_in_text(line2b, .05, 25)
print()
time.sleep(.4)

fade_in_from_sides(line3, .05, 25)
time.sleep(.2)
fade_in_words_non_del(line4, .03, 5)
time.sleep(.2)
show_each_letter(line4a, .08)
print()
time.sleep(1)

fade_in_from_sides(line5, .05, 20)
time.sleep(.3)
show_each_letter(line5a, .06)
print()
time.sleep(.5)

fade_in_from_sides(line6, .05, 20)
time.sleep(.3)
show_each_letter(line6a, .15)
print()
time.sleep(.7)

fade_in_words_non_del(line7, .03, 5)
print()
time.sleep(.3)
show_fade_in_and_each_letter(line8, .06)
time.sleep(.5)
fade_in_text(line8a, .05, 15)
print()
time.sleep(.8)

show_each_letter(line9, .06)
time.sleep(.3)
show_each_letter(line9a, .06)
time.sleep(.3)
fade_in_text(line9b, .05, 20)
print()
time.sleep(.5)

show_each_letter(line10, .06)
time.sleep(.3)
show_each_letter(line10a, .06)
time.sleep(.3)
fade_in_text(line10b, .05, 20)
print()
time.sleep(.5)

fade_in_from_sides(line11, .05, 10)
print()
time.sleep(.5)
show_each_letter(line12, .05)
time.sleep(.3)
fade_in_text(line12a, .04, 10)
time.sleep(.3)
if line12b.endswith("..."):
    main_text = line12b[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)