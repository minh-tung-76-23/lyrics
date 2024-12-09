import time

text = """
Em muốn quên đi chuyện lúc xưa
Anh cũng không quan tâm em hơn nữa
Trong chúng ta đâu ai có quyền níu kéo được nhau
Em muốn quên đi bao tháng ngày
Anh cũng mong hai ta cùng giữ lấy
Những giấc mơ khi xưa khép lại theo gió nhẹ trôi
Thôi cũng đành thôi…
"""

char_delay = 0.07   
line_delay = 0.8   

time.sleep(1.0)

for i, char in enumerate(text):
    if text[i:i+1] == "…":
        for dot in range(3):
            print(".", end='', flush=True)
            time.sleep(1.0) 
        continue  

    print(char, end='', flush=True)

    time.sleep(char_delay)

    if text[i-5:i] == "quyền" and char == ' ':
        time.sleep(0.8)

    if text[i-4:i] == "nhau":
        time.sleep(1.2)  
    if text[i-6:i] == "hai ta" and char == ' ':
        time.sleep(0.8)
    if text[i-3:i] == "lại" and char == ' ':
        time.sleep(0.8)
    if text[i-3:i] == "gió" and char == ' ':
        time.sleep(0.8)
    if text[i-4:i] == "đành" and char == ' ':
        time.sleep(1.0)

    if char == '\n':
        time.sleep(line_delay)
