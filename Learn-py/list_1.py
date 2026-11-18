#1
cart = ["หมูสไลซ์", "เบคอน", "ผักรวม"]
cart.append("เส้นอุด้ง")
print (cart)
cart.remove("ผักรวม")
print (cart)
cart[0] = "หมูสามชั้น"
print (cart)
#2
scores = [75, 88, 92, 60, 85]
print(f"จำนวนคนสอบทั้งหมด : {len(scores)}")
print(f"คะแนนรวมทั้งหมด : {sum(scores)} Average : {sum(scores) / len(scores)}")
print(f"คะแนนสูงสุด : {max(scores)} และ คะแนนต่ำสุด : {min(scores)}")
#3 
drinks = ["ชาไทย", "ชาเขียว", "โกโก้", "กาแฟเย็น"]
for index,menus in enumerate (drinks,start=1):
    print (f"เมนูที่ {index} : {menus}")
#4
oders = []
for i in range(3):
    food = input(f"สั่งอาหารรายการที่ {i+1}: ")
    oders.append(food)
print(f"สรุปรายการที่สั่งทั้งหมด: {oders}")