#1 tuple
shop_location = (19.1662, 99.9019)
categories = ("อาหารสด", "เครื่องดื่ม", "ของทานเล่น")
print(shop_location[0])
#categories[2] = "ของหวาน" error เพราะtuple แก้ไขไม่ได้
#2 tuple
employee = ("EMP01", "กิตติพันธ์", "แคชเชียร์")
emp_id,emp_name,role = employee[0],employee[1],employee[2]
print (f"รหัส: {emp_id} | ชื่อ: {emp_name} | ตำแหน่ง: {role}")
#3 set
orders = ["หมูสไลซ์", "เบคอน", "หมูสไลซ์", "กุ้งสด", "เบคอน", "หมูสไลซ์"]
unique_menus = set(orders)
unique_menus.add("เส้นอุด้ง")
print (f"รายชื่อเมนูที่ไม่ซ้ำกันทั้งหมด :{unique_menus} จำนวนชนิดของเมนูที่สั่งทั้งหมด {len(unique_menus)}")
#4 set 
table_1 = {"หมูสไลซ์", "เบคอน", "น้ำจิ้มสุกี้", "โค้ก"}
table_2 = {"เบคอน", "กุ้งสด", "น้ำจิ้มสุกี้", "น้ำเปล่า"}
both = table_1 & table_2
only_t1 = table_1 - table_2
print (f"ทั้ง 2 โต๊ะสั่งเหมือนกัน : {both}")
print (f"โต๊ะ 1 สั่ง แต่โต๊ะ 2 ไม่ได้สั่ง : {only_t1}")