import time
import sys
from animation import *

line6 = "       Vì ❤️  này"  
line6a = "Chẳng thể yêu thêm một ai..."  
linea = "      ●─🩶  ─●"
line1 = "Chỉ là một phút"  
line1a = "anh nhớ đến em"  
line2 = "Chỉ là mùa thu"  
line2a = " mà ta đã quên"  
line3 = "Chỉ là nỗi nhớ"  
line3a = " khi thu về"  
line3b = "Lại ở bên anh"  
line3c = " Mỗi khi"  
line3d = "nhớ đến"  
line4 = "Mai này liệu ta"  
line4a = "Sẽ mãi mất nhau"  
line5 = "Sau này sẽ chẳng có em"  
line5a = "Cùng anh phía sau"  

flash_line_fade_in_out_once(line6, 1)
time.sleep(.3)
fade_in_from_sides(line6a, .06, 20)
print()
time.sleep(.2)
flash_line_fade_in_out_once(linea, 1)
time.sleep(.5)
fade_in_words_non_del(line1, .03, 5)
time.sleep(.3)
show_each_letter(line1a, .07)
print()
time.sleep(.5)
fade_in_words_non_del(line2, .03, 5)
time.sleep(.3)
show_each_letter(line2a, .07)
print()
time.sleep(.5)
fade_in_words_non_del(line3, .02, 3)
print()
time.sleep(.3)
fade_in_and_move_from_right(30, line3a, .05, 20)
time.sleep(.5)
show_fade_in_and_each_letter(line3b, .06)
print()
time.sleep(.5)
fade_in_words_non_del(line3c, .05, 5)
time.sleep(.8)
show_each_letter(line3d, .07)
print()
time.sleep(.5)
fade_in_words_non_del(line4, .02, 3)
time.sleep(.5)
flash_line_fade_in_out_once(line4a, 2)
time.sleep(.5)
flash_line_fade_in_out_once(line5, 1)
time.sleep(.2)
fade_in_words_non_del(line5a, .02, 3)
print()
time.sleep(.5)
fade_in_from_sides(line6, .06, 20)
print()
time.sleep(.5)
if line6a.endswith("..."):
    main_text = line6a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)

