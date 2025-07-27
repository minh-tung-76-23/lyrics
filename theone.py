import time
import sys
from animation import * 

line_space = "                                "
line1 = "Come on lemme see you"  
line1a = "\t\t\tpop off"  
line2 = "Baby"  
line2a = "show out"  
line3 = "If you got that"  
line4 = "go down"  
line5 = "On the low now"  
line6 = "Make it go loud"  
line7 = "No control now"  
linea = "      Oh🩶     "  
line8 = "Và anh xin lỗi nếu như em cảm thấy phiền"  
line8a = "Khi thấy được dòng tin nhắn này"  
line9 = "Anh chỉ muốn nói vài lời cuối"  
line9a = "   Sau đó thì anh sẽ phắn ngay"  
line10 = "Anh biết em thắc mắc"  
line10a = "Sao thời gian qua anh đã đi vắng vậy"  
line11 = "Well"  
line11a = "anh đã gặp một người con gái"  
line11b = "Và ❤️  anh đã có ngày"  
line11c = "Nó được lấp đầy "  
line12 = "And yeah I know you got some love"  
line12a = " for the boy"  
line13 = "Broke your heart twice"  
line14 = "Sending love"  
line14a = "to Hanoi"  
line15 = "Pretty young thing"  
line15a = "Đem lòng mến"  
line15b = "Một thằng tồi"  
line16 = "Khi anh hẹn gặp"  
line16a = "Em nói không đến"  
line16b = "là được rồi😎"  

show_fade_in_and_each_letter(line1, .04)
time.sleep(.2)
fade_in_text(line1a, .05)
time.sleep(.2)
fade_in_words_non_del(line2, .01, 1)
time.sleep(.2)
show_each_letter(line2a, .04)
time.sleep(.5)
fade_in_text(line_space, .001)
fade_in_words_non_del(line3, .01, 1)
time.sleep(.4)
fade_in_text(line_space, .001)
fade_in_words_non_del(line2, .01, 1)
time.sleep(.2)
show_each_letter(line4, .04)
time.sleep(.4)
fade_in_text(line_space, .001)
fade_in_words_non_del(line5, .01, 1)
time.sleep(.4)
fade_in_text(line_space, .001)
fade_in_words_non_del(line6, .01, 1)
time.sleep(.4)
fade_in_text(line_space, .001)
fade_in_words_non_del(line7, .01, 1)
time.sleep(.1)
flash_line_fade_in_out_once(linea, .2)

show_fade_in_and_each_letter(line8, .02)
print()
fade_in_words_non_del(line8a, .01, 1)
print()
time.sleep(.3)
fade_in_words_non_del(line9, .01, 1)
print()
time.sleep(.1)
random_flicker(line9a, .06, 10)
print()
time.sleep(.5)
fade_out_with_color(line10, .04, 10)
time.sleep(.1)
fade_in_words_non_del(line10a, .01, 1)
print()
time.sleep(.1)
fade_in_words_non_del(line11, .01, 1)
time.sleep(.1)
show_each_letter(line11a, .02)
print()
time.sleep(.1)
show_fade_in_and_each_letter(line11b, .02)
print()
time.sleep(.1)
bounce_text(line11c, .04, 10)
print()
time.sleep(.3)

fade_in_from_sides(line12, .05, 10)
time.sleep(.1)
show_each_letter(line12a, .03)
print()
time.sleep(.5)
scroll_text(line13, .02, 15)
time.sleep(.1)
fade_in_words_non_del(line14, .01, 1)
time.sleep(.1)
show_each_letter(line14a, .03)
print()
time.sleep(.3)

fade_in_from_sides(line15, .05, 20)
print()
time.sleep(.1)
fade_in_words_non_del(line15a, .01, 1)
print()
time.sleep(.2)
fade_in_words_non_del(line15b, .01, 1)
print()
time.sleep(.4)

show_each_letter(line16, .03)
print()
time.sleep(.2)
fade_in_words_non_del(line16a, .01, 1)
time.sleep(.2)
show_each_letter(line16b, .03)

