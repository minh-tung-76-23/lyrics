import time
from animation import *   

line1 = "Suýt nữa thì"
line1a = "Anh có thể nói"
line1b = "    Muôn vàn lời muốn nói..."
line2 = "Có thể đèo em"
line2a = " qua từng hàng phố quen"
line3 = "   Dòng lưu bút năm xưa"
line3a = "\t\t\tviết vội"
line3b = "\t“Hãy còn nhớ nhau "
line3c = "đến những ngày sau”"
line4 = "      Tình yêu đầu tiên "
line4a = "\t\t\tanh giữ"
line4b = "Vẫn vẹn ngày nơi con tim này🩶"
line5 = "Anh còn nhớ"
line5a = "Mỗi lúc tan trường ngại ngùng theo em"
line6 = "Là con phố"
line6a = "Có hoa bay và anh mãi theo sau"
line7 = "Khoảng cách ấy mà sao xa quá"
line8 = "Chẳng thể nào để tới"
line8a = "\t\t\tbên em"
line9 = "Thời thanh xuân anh có"
line9a = "Là những nỗi niềm"
line9b = " nuối tiếc🩶..."

fade_in_text(line1, .09)
time.sleep(.5)
show_fade_in_and_each_letter(line1a, .08)
time.sleep(.5)
fade_in_from_sides(line1b, .09, 25)
print()

time.sleep(.5)
fade_in_text(line1, .09)
time.sleep(.5)
fade_in_from_sides(line2, .09, 30)
time.sleep(.5)
show_each_letter(line2a, .08)
print()

time.sleep(1)
show_fade_in_and_each_letter(line3, .07)
time.sleep(.5)
fade_in_text(line3a, .09)
print()

time.sleep(.5)
fade_in_words_non_del(line3b, .01, 5)
time.sleep(.5)
show_each_letter(line3c, .08)
print()

time.sleep(.5)
show_each_letter(line4, .07)
time.sleep(.5)
fade_in_text(line4a, .09)
print()
time.sleep(.5)
fade_in_and_move_from_right(40, line4b, .15, 20)

time.sleep(1)
fade_in_words_non_del(line5, .03, 10)
time.sleep(.5)
fade_in_from_sides(line5a, .1, 30)
print()

time.sleep(1)
fade_in_words_non_del(line6, .03, 10)
time.sleep(1)
fade_in_and_move_from_right(40, line6a, .15, 20)

time.sleep(1)
fade_out_from_sides_left(line7, .09, 30)
time.sleep(.5)
show_fade_in_and_each_letter(line8, .07)
time.sleep(.5)
fade_in_text(line8a, .09)
print()

time.sleep(.5)
fade_in_and_move_from_right(40, line9, .06, 20)

time.sleep(.5)
fade_in_from_sides(line9a, .06, 20)
time.sleep(.5)
if line9b.endswith("..."):
    main_text = line9b[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print()






