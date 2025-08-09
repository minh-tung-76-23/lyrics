import time
import sys
from animation import * 

linea = "    🎙️  Anh"
lineaa = "     Chưa   "
lineaaa = "Bao giờ ngừng một ngày nhớ về em"
line1 = "Khi nào ngừng một giờ nghĩ về em"  
line2 = "Phút nào ngừng thuộc về em"  
line3 = "Chưa từng một giây nào"  
line3a = "\t\t\t ngừng yêu em."  
line4a = "    Mang   "  
line4b = "Kỷ niệm chìm vào hồi ức thật lâu"  
line5 = "♪ Ghi"  
line5a = " tên một ❤️  từng rất đậm sâu"  
line6 = "♬ Cám"  
line6a = " ơn vì đã gặp được nhau"  
line7 = "Kiếp này xem như"  
line7a = "Đã nhặt được 🏴‍☠️ 💰"  
line8 = "🎙️  You're the only one I love 💕 "  
line9 = "Kiếp này xem như"  
line9a = "đã nhặt được kho báu..."  


time.sleep(3)
fade_in_text(linea, .05)
time.sleep(.2)
fade_in_text(lineaa, .05)
time.sleep(.2)
show_fade_in_and_each_letter(lineaaa, .03)
print()
time.sleep(.3)

fade_in_text(lineaa, .05)
time.sleep(.2)
show_fade_in_and_each_letter(line1, .03)
print()
time.sleep(.5)

fade_in_text(lineaa, .06)
time.sleep(.5)
show_fade_in_and_each_letter(line2, .03)
print()
time.sleep(.5)

fade_in_words_non_del(line3, .02, 5)
time.sleep(.3)
fade_in_text(line3a, .06)
print()
time.sleep(.3)

fade_in_text(linea, .05)
time.sleep(.2)
fade_in_text(line4a, .05)
time.sleep(.3)
show_fade_in_and_each_letter(line4b, .03)
print()
time.sleep(.3)

fade_in_text(line5, .05)
time.sleep(.2)
show_each_letter(line5a, 0.04)
print()
time.sleep(.3)
fade_in_text(line6, .05)
time.sleep(.3)
show_each_letter(line6a, 0.04)

print()
time.sleep(.3)
fade_in_from_sides(line7, .04, 15)
time.sleep(.2)
fade_in_words_non_del(line7a, .01, 1)
print()
time.sleep(.2)
fade_out_by_char(line8, .05, 10)
time.sleep(.5)
fade_out_from_sides(line8, .07, 30)
time.sleep(.5)
show_fade_in_and_each_letter(line8, .06)
print()
time.sleep(.5)
fade_in_words_non_del(line9, .01, 1)
time.sleep(.3)
if line9a.endswith("..."):
    main_text = line9a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.7)
    print() 



