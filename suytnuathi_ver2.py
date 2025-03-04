import time
from animation import *   

line1 = "Lời chưa nói"
line1a = "Anh thả vào trong cơn gió"
line1b = " nhắn với mây trời..."
line2 = "Tình yêu đó"
line2a = "chỉ riêng anh biết"
line2b = "Anh cũng"
line2c = " chẳng mong hơn nhiều🩶"
line3 = "Liệu rằng em còn ai đưa đón"
line3a = "     Anh ơ thờ"
line3b = "\t\tdõi"
line3c = " theo em"
line4 = "Nếu có thể trở về hôm ấy"
line4a = "Anh sẽ chẳng để"
line4b = " phí cơ hội"
line5 = "Từng vòng quay"
line5a = "Trên chiếc xe đạp"
line5b = "Anh đón"
line5c = " đưa em ngang qua"
line6 = "Thời thanh xuân"
line6a = " mà ta cùng nhau"
line6b = "Viết lên"
line6c = " những giấc mơ đẹp"
line7 = "Một buổi chiều ngập tràn mảnh vỡ"
line7a = "Rơi ra từ hạnh phúc"
line7b = " riêng anh"
line8 = "Suýt nữa thì người đã biết"
line8a = "🎙️ Yêu thương một thời"
line8b = "\t\t\tanh đã"
line8c = " tương tư..."

time.sleep(2)
fade_in_words_non_del(line1, .01, 5)
time.sleep(1)
fade_in_from_sides(line1a, .07, 25)
time.sleep(.5)
show_each_letter(line1b,.07)

print()
time.sleep(1)
fade_in_words_non_del(line2, .01, 5)
time.sleep(1)
show_each_letter(line2a,.07)
print()

time.sleep(.5)
fade_in_text(line2b, .09)
time.sleep(.5)
show_each_letter(line2c,.07)
print()
time.sleep(.5)

fade_in_and_move_from_right(40, line3, .08, 20)
time.sleep(.5)

fade_in_from_sides(line3a, .07, 15)
time.sleep(.2)
fade_in_text(line3b, .07)
time.sleep(.5)
show_each_letter(line3c,.07)

print()
time.sleep(1.3)
fade_in_and_move_from_right(40, line4, .08, 15)
time.sleep(.5)
fade_in_words_non_del(line4a, .01, 5)
time.sleep(.5)
show_each_letter(line4b,.07)

print()
time.sleep(.5)
scroll_text(line5, .05, 20)
time.sleep(.5)
fade_out_from_sides_left(line5a, .06, 20)
time.sleep(.5)
fade_in_text(line5b, .06)
time.sleep(.5)
show_each_letter(line5c,.07)

print()
time.sleep(.5)
fade_in_words_non_del(line6, .01, 5)
time.sleep(1)
show_each_letter(line6a,.07)

print()
time.sleep(.5)
fade_in_text(line6b, .09)
time.sleep(.2)
show_each_letter(line6c,.06)
time.sleep(.5)

scroll_text(line7, .05, 26)
time.sleep(.5)
fade_in_from_sides(line7a, .05, 15)
time.sleep(.5)
show_each_letter(line7b,.07)

print()
time.sleep(1)
flash_line_fade_in_out_once(line8, 2)
fade_in_words_non_del(line8a, .01, 5)
time.sleep(.5)
fade_in_text(line8b, .09)
time.sleep(.5)
if line8c.endswith("..."):
    main_text = line8c[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print()

