#1
secret = "X9P2A7Y4K"
print (f"{secret[1]} {secret[3]} {secret[5]} {secret[7]}")
#2
code = input("กรอกรหัสสินค้า : ")
if code[0] == "T" and code[-1] == "9":
    print ("รหัสสินค้าถูกต้อง")
else:
    print ("รหัสสินค้าผิดรูปแบบ")
#3
text = input("กรอกข้อความ : ")
count_a = 0
for count in text.lower():
    if count == "a":
        count_a += 1
print (f"พบตัวอักษร a ทั้งหมด {count_a} ตัว")