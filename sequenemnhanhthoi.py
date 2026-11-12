import time
import sys
from animation import *

line1 = "Như cái cách"  
line1a = "Em lảng tránh"  
line1b = "Mọi cuộc tranh luận"  
line1c = "Và cứ ngồi trầm ngâm "  
line2 = "Cách"  
line2a = " mà em khiến"  
line2b = "Mọi người điên đầu"  
line2c = "Dù em chẳng bận tâm"  
line3 = "Cách"  
line3a = "Em mang đến"  
line3b = "Cơn say nắng nhẹ "  
line3c = "Mà tới giờ còn ngấm"  
line4 = "Cách em làm anh"  
line4a = "\tMuốn quên đi bản thân"   
line5 = "Toàn bộ những thứ em để lại"  
line6 = "Nặng hơn điếu thuốc mà anh chẳng thể cai"  
line7 = "Khiến anh thao thức"  
line7a = "    Suốt những đêm dài"  
line8 = "Dai dẳng như"  
line8a = "món nợ đòi nặng lãi"  
line9 = "Nếu như mỗi kí ức"  
line9a = "Là một niềm đau"  
line10 = "Thì giờ đây"  
line10a = "Anh đang tiên lượng xấu"  
line11 = "Em như morphin được tiêm vào máu"  
line12 = "Khiến anh liên"  
line12a = " tiếp chìm thật sâu"  
line13 = "Cuốn lấy anh vào"  
line13a = "       Chẳng lối thoát ra"  
line14 = "Vẫn cứ dối lòng "  
line14a = "Với những thiết tha"  
line15 = "Để "  
line15a = "tự nhủ"  
line15b = "Rằng  "  
line15c = "\tTa"  
line15e = " đã hết xót xa🩶 ..."  
line16 = "Sẽ chẳng buồn lâu"  
line16a = "Vết thương sẽ ngừng"  
line16b = " nhói"  
line16c = "Sẽ không còn đâu"  
line16d = "Dấu yêu ta từng"  
line16e = "nói"  
line16f = "Và sẽ quên"  
line16g = "\tEm"  
line16i = "\t\tnhanh thôi🩶"  

fade_in_words_non_del(line1, .01, 1)
print()    
time.sleep(.2)
fade_in_words(line1a, .01,1)
fade_in_words_non_del(line1b, .01, 1)
print()   
bounce_text(line1c, .03, 10)
print()
time.sleep(.5)

random_flicker(line2, .04, 5)
time.sleep(.2)
show_each_letter(line2a, .03)
print()
time.sleep(.2)
fade_in_words_non_del(line2b, .01, 1)
print()
time.sleep(.2)
bounce_text(line2c, .03, 10)
print()
time.sleep(.5)

fade_in_text(line3, .05, 5)
time.sleep(.2)
fade_in_words_non_del(line3a, .01, 1)
print()
time.sleep(.2)
bounce_text(line3b, .03, 10)
print()
time.sleep(.5)
random_flicker(line3c, .04, 5)
print()
time.sleep(1)

fade_in_words_non_del(line4, .01, 1)
print()
time.sleep(.5)
fade_in_from_sides(line4a, .04, 20)
print()
time.sleep(.5)

fade_from_sides(line5, 0.04, 10)
time.sleep(.2)
show_fade_in_and_each_letter(line6, delay=0.03)  
print()
time.sleep(.5)

fade_in_words_non_del(line7, .01, 1)
print()
time.sleep(.2)
random_flicker(line7a, .04, 5)
print()
time.sleep(.2)
fade_in_words_non_del(line8, .01, 1)
time.sleep(.2)
show_each_letter(line8a, .03)
print()
time.sleep(.5)

fade_in_words(line9, 0.001, 5)
time.sleep(.2)
show_fade_in_and_each_letter(line9a, delay=0.05)  

print()
time.sleep(.2)
fade_out_from_sides_left(line10, .03, 10)
time.sleep(.2)
show_each_letter(line10a, .05)

print()
time.sleep(.2)
random_flicker(line11, .1, 10)
print()
time.sleep(.2)
fade_in_text(line12, .05)
time.sleep(.2)
show_each_letter(line12a, .05)
print()
time.sleep(.2)


fade_in_words_non_del(line13, .01, 1)
print()
time.sleep(.2)
color_splash_effect(line13a, .07, 15)
print()
time.sleep(1)
bounce_text(line14, .06, 10)
print()
time.sleep(.2)
show_fade_in_and_each_letter(line14a, 0.07)  
print()
time.sleep(1)

fade_in_text(line15, .05)
time.sleep(.2)
fade_in_words_non_del(line15a, .01, 1)
time.sleep(.2)
fade_in_text(line15b, .03)
time.sleep(.2)
fade_in_text(line15c, .05)
time.sleep(.2)
if line15e.endswith("..."):
    main_text = line15e[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.8)
    print()

fade_in_words_non_del(line16, .01, 1)
print()
time.sleep(.2)
random_flicker(line16a, .1, 15)
time.sleep(.5)
show_each_letter(line16b, .05)

print()
time.sleep(.5)
color_splash_effect(line16c, .07, 10)

print()
time.sleep(.2)
fade_in_words_non_del(line16d, .01, 1)
time.sleep(.5)
show_each_letter(line16e, .05)

print()
time.sleep(.5)
fade_in_words_non_del(line16f, .01, 1)
print()
time.sleep(.5)
random_flicker(line16g, .1, 10)
time.sleep(.5)
flash_line_fade_in_out_once(line16i, 4)






















