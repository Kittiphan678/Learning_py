#ข้อที่ 1
score1 = int(input("กรอกคะแนนสอบ : "))
if score1 >= 50:
    print ("Pass")
else:
    print ("not pass")
#ข้อที่ 2
score2 = int(input("กรอกตัวเลขจำนวนเต็ม : "))
if score2 % 2 == 0:
    print ("even")
else:
    print ("odd")
#ข้อที่3
whigh, hight = map(float, input("กรอกน้ำหนัก (กก.) และ ส่วนสูง (ซม.) (เว้นวรรคคั่น) :").split())
BMI = whigh / ((hight/100)**2)
if BMI < 18.5:
    print ("น้ำหนักน้อย / ผอม")
elif BMI >= 18.5 and BMI <= 22.9:
    print ("สมส่วน (สุขภาพดี)")
elif BMI >= 23.0 and BMI <= 24.9:
    print ("ท้วม / เริ่มอ้วน")
else:
    print ("อ้วน")
#ข้อที่ 4
age ,hight1 = map(int,input("กรอกอายุ และ ส่วนสูง (เว้นวรรคคั่น) : ").split())
if age >= 12 and hight1 >= 140:
    print ("อนุญาตให้เล่นได้")
else:
    print ("เสียใจด้วย คุณไม่สามารถขึ้นรถไฟเหาะได้")
#ข้อที่ 5
order = float(input("กรอกยอดซื้อสินค้า : "))
shipping = 0 if order >= 1000 else 50
print(f"ค่าจัดส่งของคุณคือ: {shipping} บาท")