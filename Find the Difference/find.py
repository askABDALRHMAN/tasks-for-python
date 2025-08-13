s = "abcd"
t = "abcde"

for char in t:
    if t.count(char) != s.count(char): #علشان نقارن عدد مرات ظهور الحرف هنا وهنا ولو مش شبه بعضه نطبعه وده هيكوون الحرف المختلف
        print(char)
        break