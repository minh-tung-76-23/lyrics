import time
import sys
from animation import * 

line1 = "Và nếu như ta có"  
line1a = "\t\t phép màu"  
line1b = "🎙️ Thì đã không như thế"  
line1c = "\t\t\t I know"  
line2 = "But baby why you said so         "  
linea = "      ●─🩶  ─●"
line3 = "Một người lặng nhìn"  
line3a = "từng cánh hoa trong tay"  
line3b = "      Girl just keep it close     "  
line4 = "Và rồi chẳng biết"  
line4a = "em đâu hay"  
line4b = "Yêu thương kia từ đầu"  
line5 = "Cùng màn đêm đêm thâu"  
line5a = "Chẳng còn gặp được em đâu"  
line6 = "Khi trên đôi mi trong đêm"  
line6a = "Em suy tư"  
line6b = "bao u sầu"  
line7 = "Một ngày tình cờ "  
line7a = "được thấy em bên ai"  
line7b = "Yêu em như tình đầu"  
line8 = "Baby"  
line8a = "just forget me now"  
line8b = "   Forget me now🩶   "  
line9 = "Ta luôn mang theo bao nhiêu"  
line9a = " Yêu thương khi ta đậm sâu  "  
line10 = "Nhưng sao lại chẳng thể bên nhau🩶..."  

fade_in_words_non_del(line1, .01, 1)
time.sleep(.1)
fade_in_text(line1a, .04)
time.sleep(.2)

fade_in_words_non_del(line1b, .01, 1)
time.sleep(.1)
fade_in_text(line1c, .03)
time.sleep(.2)

show_fade_in_and_each_letter(line2, .03)
print()
flash_line_fade_in_out_once(linea, .3)

fade_in_words_non_del(line3, .01, 1)
time.sleep(.1)
show_each_letter(line3a, .04)
time.sleep(.5)
print()
fade_in_from_sides(line3b, .05, 15)
print()
time.sleep(.5)

fade_in_words_non_del(line4, .01, 1)
time.sleep(.1)
show_each_letter(line4a, .04)
time.sleep(.5)
print()
fade_in_and_move_from_right(30, line4b, .05, 20)
time.sleep(.2)

show_fade_in_and_each_letter(line5, .04)
time.sleep(.3)
fade_in_words_non_del(line5a, .01, 1)
print()
time.sleep(.5)

fade_out_by_char(line6, .03, 10)
time.sleep(.2)
fade_in_words_non_del(line6a, .01, 1)
time.sleep(.2)
show_each_letter(line6b, .04)
print()
time.sleep(.5)

fade_in_words_non_del(line7, .01, 1)
time.sleep(.2)
show_each_letter(line7a, .04)
print()
time.sleep(.5)
fade_out_by_char(line7b, .03, 10)
time.sleep(.3)
fade_in_words_non_del(line8, .01, 1)
time.sleep(.2)
show_each_letter(line8a, .06)
print()
time.sleep(1)
flash_line_fade_in_out_once(line8b, 2)

show_fade_in_and_each_letter(line9, .04)
fade_in_from_sides(line9a, .06, 30)
time.sleep(.5)
print()
if line10.endswith("..."):
    main_text = line10[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.7)
    print() 








