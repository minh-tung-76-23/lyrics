import time
import sys
from animation import *

line1 = "🎙️ Tình yêu cứ "  
line1a = "\t\tgiống hệt"  
line1b = " một câu đố"  
line2 = "🎧 Ta mất bao"  
line2a = "\t\ttháng năm để trả lời"  
line3 = "Dại khờ lúc ấy"  
line4 = "Anh cũng"  
line4a = "như người mà thôi"  
line5 = "Rất đỗi chơi vơi"  
line6 = "Vì khi thấy"  
line6a = "cách mình đặt niềm tin"  
line7 = "Vào đôi mắt"  
line7a = "ngẩn ngơ đắm chìm"  
line8 = "Anh đâu"  
line8a = "trách than gì người"  
line9 = "Chuyện hợp tan"  
line9a = "vẫn diễn ra thôi"  
line10 = "Đừng vội đi mau"  
line11 = "Cho anh nói hết"  
line12 = "Giấc mơ không thành"  
line13 = "Đã hóa nên nhành nên hoa"  
line14 = "Ôm vết thương anh"  
line15 = "Chuyện buồn không tên mình từng viết nên"  
line16 = "Dẫu không còn đoạn kết mới"  
line17 = "Thì cũng đã qua rồi người ơi"  
line18 = "Bình an đi thôi"  

fade_in_from_sides(line1, .04, 20)
time.sleep(.5)
fade_in_text(line1a, .09)
time.sleep(.2)
show_each_letter(line1b, .06)
time.sleep(.5)
print()
show_each_letter(line2, .06)
time.sleep(1)
fade_in_text(line2a, .09)
time.sleep(.5)
print()

show_fade_in_and_each_letter(line3, .04 )
print()
time.sleep(.2)
fade_in_words_non_del(line4, .03, 2)
time.sleep(.5)
show_each_letter(line4a, .06)
time.sleep(.5)
print()

fade_in_from_sides(line5, .06, 20)
time.sleep(.5)
print()

fade_in_words_non_del(line6, .03, 2)
time.sleep(.5)
show_each_letter(line6a, .06)
time.sleep(.5)
print()
show_fade_in_and_each_letter(line7, .04 )
time.sleep(.5)
fade_in_text(line7a, .09)
time.sleep(.5)
print()

fade_in_text(line8, .09)
time.sleep(.5)
print()
show_each_letter(line8a, .06)
time.sleep(.5)
print()

fade_in_words_non_del(line9, .03, 2)
time.sleep(.5)
if line9a.endswith("..."):
    main_text = line9a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print()












