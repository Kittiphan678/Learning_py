#1
menu = {
    "ข้าวมันไก่" : 50,
    "ข้าวหมูแดง": 55,
    "ก๋วยเตี๋ยว": 45
}
print(f"ข้าวหมูแดง : {menu.get("ข้าวหมูแดง")}")
#2 ใช้ตัวแปร menu จากข้อที่ 1 ต่อได้เลย
menu["ข้าวขาหมู"] = 60
menu["ก๋วยเตี๋ยว"] = 50
print (f"{menu['ข้าวขาหมู']} : {menu['ก๋วยเตี๋ยว']}")
#3
del menu["ข้าวมันไก่"]
print (f"จำนวนเมน : {len(menu)}")
#4
item = input("ค้นหาราคาเมนู : ").strip()
result = menu.get(item,"ไม่มีเมนูนี้ในร้าน")
print (f"เมนที่ค้นหา {item} : {result}")
#5
food = input("ค้นหาราคาเมนู : ").strip()
if food in menu:
    qty = int(input("รับกี่จาน : "))
    total = menu[food] * qty
    print (f"เมนู : {food} จำนวน : {qty} จาน แจ้งยอดเงิน : {total} บาท")
else :
    print (f"ขออภัย เมนูหมดหรือไม่มีในร้าน")