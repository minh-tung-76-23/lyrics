import time
import sys
from animation import *

line1 = "Họ đâu biết em là ai"  
line2 = "Cô ta biết em là ai"  
line3 = "Chỉ mình anh không biết em là ai cả"  
line4 = "Tối đó"  
line4a = " anh ta đã dắt cô ta"  
line5 = "Vào trong căn phòng nhỏ"  
line5a = "\t\t\tđóng kín"  
line6 = "Nghe thôi cũng biết"  
line7 = "Câu chuyện xảy ra hệt tại"  
line7a = "\t\t\ti trong phim"  
line8 = "Nô đùa trong trái tim ta"  
line9 = "Hệt tại"  
line9a = "\ttối đó"  
line10 = "Điều đáng nói hơn bây giờ"  
line11 = "Giọt nước mắt vướng trên khuôn nhạc"  
line12 = "Tưởng ngọc ngà đá quý"  
line12a = "anh yêu bạc "  
line13 = "Thấy"  
line13a = " tiếng vang oanh tạc"  
line14 = "Nàng đành lòng"  
line14a = "\tLấy bức tranh sơn vàng"  
line15 = "Vốn"  
line15a = " có một vườn hồng"  
line16 = "Chuyện tình yêu có một người trồng"  
line17 = "Người tôi yêu"  
line17a = " Xa hoa"  
line18 = "\ttrăng hoa"  
line18a = " tính đào hoa"  
line19 = "Tiếc thay bản nhạc tình"  
line20 = " anh ta có thiết tha"  
line21 = "Hương mùi hoa em để lại"  
line22 = " anh ta đâu biết"  
line23 = "Hái một nhành hoa em đặt lại "  
line24 = " trên đầu bao đám mây đen"  
line25 = " Gầm gừ"  
line25a = "\tkéo tới"  
line26 = "Điều đáng nói hơn bây giờ"  

fade_out_from_sides(line1, .05, 20)
fade_out_from_sides_left(line2, .04, 20)
fade_in_words_non_del(line3, .01, 1)
time.sleep(.5)
print()
fade_in_text(line4, .05, 5)
time.sleep(.5)
show_each_letter(line4a, .05)
print()
show_each_letter(line5, .05)
time.sleep(.3)
fade_in_text(line5a, .05, 5)
print()
time.sleep(1)
fade_in_words_non_del(line6, .01, 1)
print()
show_each_letter(line7, .05)
time.sleep(.3)
fade_in_text(line7a, .05, 10)
print()
time.sleep(.5)
fade_in_from_sides(line8, .06, 20)
print()
time.sleep(.5)
fade_in_words_non_del(line9, .01, 1)
time.sleep(.3)
fade_in_text(line9a, .05, 10)
print()
scroll_text(line10, .06, 15)
time.sleep(.5)
fade_in_words_non_del(line11, .01, 1)
print()
show_each_letter(line12, .05)
print()
bounce_text(line12a, .05, 5)
time.sleep(.5)
fade_in_text(line13, .05, 5)
time.sleep(.3)
show_each_letter(line13a, .05)
print()
time.sleep(.2)
fade_in_words_non_del(line14, .01, 1)
print()
time.sleep(.2)
fade_in_from_sides(line14a, .05, 15)
print()
time.sleep(.5)
fade_in_text(line15, .05, 5)
time.sleep(.3)
show_each_letter(line15a, .05)
print()
time.sleep(.5)
color_splash_effect(line16, .06, 20)
print()
fade_in_words_non_del(line17, .01, 1)
print()
time.sleep(.3)
fade_in_text(line17a, .03, 5)
time.sleep(.2)
fade_in_text(line18, .05, 5)
time.sleep(.5)
show_each_letter(line18a, .05)
print()
time.sleep(.5)
fade_in_words_non_del(line19, .01, 1)
print()
fade_in_text(line4, .05, 10)
time.sleep(.7)
show_each_letter(line20, .05)
print()
time.sleep(.3)
fade_in_and_move_from_right(50, line21, .05, 20)

fade_in_text(line4, .05, 10)
time.sleep(.7)
show_each_letter(line22, .05)
print()
time.sleep(.3)
# fade_in_and_move_from_right(40, line23, .03, 20)
bounce_text(line23, .07, 15)
print()

fade_in_text(line4, .05, 10)
time.sleep(.7)
show_each_letter(line24, .05)
print()
time.sleep(.3)
show_each_letter(line25, .05)
time.sleep(.5)
fade_in_text(line25a, .05, 5)
print()
time.sleep(.5)
fade_in_from_sides(line26, .08, 20)












    


