import time
import sys
from animation import * 

red = "\033[91m"  # Mã đỏ
reset = "\033[0m"

line1 = "♫  Tại sao lại nói yêu anh"  
line2 = "Mà lại để mi anh             "  
line2a = "\t\t ướt nhèm 💔"  
line3 = " 🎙️  Thật ra anh biết từ đầu rồi"  
line3a = f"{red}\t\t\t\t Bae{reset}"  
line4 = "Rằng lời yêu đó"  
line4a = " chỉ ra gió bay"  
line5 = "Giờ tim vỡ nát như này"  
line6 = "Do anh cố chấp"  
line6a = "nên vậy..."  
line7 = "Mong em hạnh phúc đi bên người ta"  
line8 = "Phần anh sẽ cố gắng để vượt qua"  
line9 = "Đến đây thôi em à"  
line10 = "Đến lúc ta phải"  
line10a = " chia xa🩶 ..."  
print('\n\n')
show_fade_in_and_each_letter(line1, .07)
time.sleep(.3)
show_fade_in_and_each_letter(line2, .05)
time.sleep(.5)
fade_in_text(line2a, .2)
print()
time.sleep(.3)

show_fade_in_and_each_letter(line3, .06)
time.sleep(.5)
fade_in_text(line3a, .09)
print()
time.sleep(.5)
fade_in_words_non_del(line4, .02, 3)
time.sleep(.3)
show_each_letter(line4a, .07)
print()
time.sleep(.5)

show_fade_in_and_each_letter(line5, .07)
print()
time.sleep(.5)
fade_in_words_non_del(line6, .02, 3)
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
        time.sleep(.5)
print()
time.sleep(.5)

flash_line_fade_in_out_once(line7, 2)
time.sleep(.5)
flash_line_fade_in_out_once(line8, 2.5)
time.sleep(.5)
fade_in_words_non_del(line9, .02, 3)
print()
time.sleep(.5)
fade_in_from_sides(line10, .05, 20)
time.sleep(.5)
if line10a.endswith("..."):
    main_text = line10a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.09) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.7)






