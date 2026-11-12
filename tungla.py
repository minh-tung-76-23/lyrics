import time
import sys
from animation import * 

line1 = "Oh"  
line2 = "Anh nghĩ em không tiếc à ?"  
line3 = "Từng chặng đường ấy"  
line3a = "\t\t đã thiết tha"  
line3b = "đã thiết tha"  
line4 = "Em cũng đau cũng tiếc mà"  
line5 = "Chỉ vì những lúc"  
line5a = "\t\t chẳng nói ra"  
line6 = " Điều sâu trong thâm tâm này  "  
line7 = "♪ Cứ giấu đi và"  
line7a = "\t\tcứ thế xa 💔"    
line51 = "          ●─ 🩶  ─●"
line11 = "🎙️ Vì cứ nghĩ"  
line11a = "\t\t hạnh phúc"  
line11b = " là nhún nhường"  
line12 = "Để rồi sau cùng thì"  
line12a = "\tWe used to be lover🩶 ..."  


fade_in_words_non_del(line1, .02, 2)
time.sleep(.1)
fade_in_words_non_del(line2, .01, 1)
time.sleep(.5)
show_fade_in_and_each_letter(line3, .04)
time.sleep(.2)
fade_in_text(line3a, .04)
time.sleep(.3)
fade_in_words_non_del(line1, .02, 2)
time.sleep(.1)
fade_in_words_non_del(line4, .01, 1)
time.sleep(.4)
show_fade_in_and_each_letter(line5, .04)
time.sleep(.2)
fade_in_text(line5a, .04)
time.sleep(.5)

fade_in_from_sides(line6, .09, 20)
time.sleep(.2)
fade_in_words_non_del(line7, .02, 2)
time.sleep(.2)
fade_in_text(line7a, .07)
print()
time.sleep(.3)
flash_line_fade_in_out_once(line51, 2)
time.sleep(.3)

fade_in_words_non_del(line1, .02, 2)
time.sleep(.1)
show_fade_in_and_each_letter(line2, .04)
print()
time.sleep(.3)
fade_in_words_non_del(line3, .01, 1)
print()
time.sleep(.1)
fade_in_and_move_from_right(30, line3b, .05, 20)
time.sleep(.3)

show_each_letter(line1, .02)
time.sleep(.1)
show_fade_in_and_each_letter(line4, .04)
print()
time.sleep(.5)
fade_in_words_non_del(line5, .02, 2)
time.sleep(.2)
fade_in_text(line5a, .04)
print()
time.sleep(.5)

fade_in_words_non_del(line11, .02, 2)
time.sleep(.2)
fade_in_text(line11a, .05)
time.sleep(.2)
show_each_letter(line11b, .05)
print()
time.sleep(.1)
fade_in_from_sides(line12, .05, 15)
print()
time.sleep(.2)
if line12a.endswith("..."):
    main_text = line12a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.6)
    print()
