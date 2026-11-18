#1คัดกรองตัวเลขด้วย
numbers ,big_numbers = [12, 5, 28, 9, 40, 3, 17],[]
for round in numbers:
    if round > 15:
        big_numbers.append(round)
print (f"เลขที่มากกว่า 15 ได้แก่ : {big_numbers}")
#2เช็กข้อมูลซ้ำก่อนเพิ่มลง
stock = ["หมู", "ไก่", "กุ้ง"]
new_item = input("กรอกชื่อสินค้าที่จะเพิ่ม: ").strip()
if new_item in stock:
    print ("มีสินค้านี้อยู่ในระบบแล้ว ไม่สามารถเพิ่มซ้ำได้")
else :
    stock.append(new_item)
    print (f"เพิ่มสินค้าเรียบร้อย : {stock}")
#3โปรแกรมตะกร้าสินค้า
cart = []
while True :
    item = input("หยิบใส่ตะกร้า (พิมพ์ 0 เพื่อจบ): ").strip()
    if item == "0":
        break
    else :
        cart.append(item)
print (f"จำนวนสินค้าทั้งหมดในตะกร้า : {len(cart)}")
for index,products in enumerate(cart,start=1):
    print (f"สินค้าตัวที่ {index} รายชื่อสินค้า {products}")


