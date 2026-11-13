#ข้อที่ 1
name = str(input("กรุณากรอกชื่อของคุณ : "))
Fv_food = str(input("อาหารที่คุณชอบคือ : "))
print (f"สวัสดีคุณ {name} เมนูโปรดของคุณคือ {Fv_food} น่ากินมาก!")
#ข้อที่ 2
year_BA = int(input("กรุณากรอกปีเกิด (พ.ศ.) : "))
print (f"ตอนนี้คุณอายุ : {2569 - year_BA}")
#ข้อที่ 3
PerPrice = float(input("ราคาสินค้าต่อชิ้น : "))
QTY = int(input("จำนวนที่ซื้อ : "))
total = QTY * PerPrice
print (f"ราคารวมทั้งหมด : {total:.2f} บาท")
#ข้อที่ 4
first_name, last_name = input("กรอกชื่อและนามสกุล (เว้นวรรคคั่น) : ").split()
print (f"ชื่อต้น : {first_name} นามสกุล : {last_name}")
#ข้อที่ 5
whigh, hight = map(float, input("กรอกน้ำหนัก (กก.) และ ส่วนสูง (ซม.) (เว้นวรรคคั่น) :").split())
BMI = whigh / ((hight/100)**2)
print (f"น้ำหนัก (กก.) : {whigh} ส่วนสูง (ซม.) : {hight} ค่า BMI ของคุณคือ : {BMI:.2f}")
