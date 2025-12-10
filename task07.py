text = input("Text: ")
check = input("Tekshiriladigan so'zni kiriting: ")

if text.endswith(check):
    print("To'g'ri")
else:
    print("Noto'g'ri, matn ushbu so'z bilan tugamaydi.")