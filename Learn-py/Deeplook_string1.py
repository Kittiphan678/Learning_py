text = "PythonProgramming"
#1
print (f"ตัวอักษรแรก : {text[0]} ตัวอักษรสุดท้าย : {text[-1]}")
#2
print (text[0:6])
print (text[6:])
#3
word = input("กรอกคำที่ต้องการ : ")
print (word[::-1])
#4
name = input("กรอกชื่อของคุณ : ")
for i in range (len(name)):
    print(name[i])