import time
import sys
from animation import *

line1 = "Liệu người có còn"  
line1a = "Ở đây với tôi thật lâu"  
line2 = "Ngày rộng tháng dài"  
line2a = "Sợ mai không còn thấy nhau"  
line3 = "Ngày em đến"  
line3a = "\tÁng mây xanh thêm"  
line4 = "Ngày em đi"  
line4a = "\tNắng vương cuối thềm"  
line5 = "Thiếu em tôi sợ bơ vơ"  
line5a = "Vắng em như tàn cơn mơ 💔"  
line6 = "Chẳng phải phép màu"  
line6a = "\tVậy sao chúng ta gặp nhau?"  
line7 = "Một người khẽ cười"  
line7a = "\tNgười kia cũng dịu nỗi đau"  
line8 = "Gọi tôi thức giấc cơn ngủ mê"  
line9 = "Dìu tôi đi"  
line9a = "lúc quên lối về"  
line10 = "Quãng đời mai sau"  
line10a = "luôn cạnh nhau..."  

time.sleep(1.55)
fade_in_words_non_del(line1, .03, 3)
time.sleep(.5)
flash_line_fade_in_out_once(line1a, 3)
time.sleep(1)

fade_in_words_non_del(line2, .05, 3)
time.sleep(.5)
fade_in_from_sides(line2a, .08, 25)
print()
time.sleep(1.5)

fade_in_words_non_del(line3, .05, 5)
print()
time.sleep(.3)
show_each_letter(line3a, .05)
print()
time.sleep(.8)

fade_in_words_non_del(line4, .03, 3)
print()
time.sleep(.3)
show_each_letter(line4a, .06)
print()
time.sleep(.6)

flash_line_fade_in_out_once(line5, 3)
flash_line_fade_in_out_once(line5a, 3)

show_fade_in_and_each_letter(line6, .06)
print()
time.sleep(.5)
fade_in_from_sides(line6a, .08, 25)
print()
time.sleep(2.5)

show_fade_in_and_each_letter(line7, .06)
print()
time.sleep(.5)
fade_in_from_sides(line7a, .08, 25)
print()
time.sleep(2.5)

scroll_text(line8, .06, 25)

fade_in_words_non_del(line9, .03, 3)
time.sleep(.5)
show_each_letter(line9a, .05)
print()
time.sleep(.5)

fade_in_words_non_del(line10, .05, 5)
time.sleep(1)
if line10a.endswith("..."):
    main_text = line10a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.5)
    print('\n\n')
