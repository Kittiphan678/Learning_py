#ข้อที่ 1
hero_name,level,atk_speed,is_alive = "Arthur",15,1.75,True
print(f"ชื่อ: {hero_name} เลเวล: {level} ความเร็วโจมตี: {atk_speed} มีชีวิตอยู่: {is_alive}")
#ข้อที่ 2
money = 500
money += 200
print(f"ยอดเงินคงเหลือ: {money}")
#ข้อที่ 3
item_price = "150"
shipping = 40
total = int(item_price) + shipping
print(f"ราคารวมค่าส่ง: {total} บาท")
#ข้อที่ 4
a = "500"
b = 500
c = 500.0
print(type(a))
print(type(b))
print(type(c))
#ข้อที่ 5
glass_a = "น้ำส้ม"
glass_b = "น้ำโค้ก"
glass_a,glass_b = glass_b,glass_a
print(f"แก้ว A คือ {glass_a} และ แก้ว B คือ {glass_b}")