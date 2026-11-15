#ข้อที่ 1
for count in range (1,6):
    print (f"รอบที่ : {count}")
#ข้อที่ 2
num1 = int(input("ต้องการดูสูตรคูณแม่ไหน : "))
for MP_table in range (1,13):
    print (f"{num1} x {MP_table} = {num1*MP_table}")
#ข้อที่ 3
AP = int(input("กรอกตัวเลข N : "))
total = 0 
for i in range (1,AP+1):
    total += i
print (f"ผลรวมตั้งแต่ 1 ถึง {AP} คือ : {total}")
#ข้อที่ 4
count1 = 5
while count1 > 0 :
    print (count1)
    count1 -= 1
print ("ปล่อยจรวด")
#5
while True:
    pwd = input("กรุณากรอกรหัสผ่าน: ")
    if pwd == "1234":
        print("เข้าสู่ระบบสำเร็จ!")
        break
    else:
        print("รหัสผ่านผิด ลองใหม่อีกครั้ง")