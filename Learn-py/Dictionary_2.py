#1
menu = {
    "ข้าวมันไก่" : 50,
    "ข้าวหมูแดง": 55,
    "ก๋วยเตี๋ยว": 45
}
for name, price in menu.items():
    print (f"เมนู : {name} ราคา : {price}")
#2
bill = {"น้ำเปล่า": 10, "โค้ก": 20, "น้ำแข็ง": 5}
total_bill = bill.values()
print (sum(total_bill))
#3 
orders = ["ชานม", "กาแฟ", "ชานม", "โกโก้", "ชานม", "กาแฟ"]
count = {}
for items in orders:
    if items in count:
        count[items] += 1
    else:
        count[items] = 1
print (f"{count}")
#4
main_dish = {"ผัดกะเพรา": 50, "ข้าวผัด": 50}
dessert = {"ไอศกรีม": 30, "บัวลอย": 25}
main_dish.update(dessert)
print (main_dish)
#10
stock_db = {
    "ปากกา": {"price": 15, "stock": 10},
    "สมุด": {"price": 25, "stock": 2}
}
ST_search = input("หาสินค้า : ").strip()
if ST_search in stock_db :
    qty = int(input("มิสินค้า รับกี่จำนวน : ").strip())
    if qty < stock_db[ST_search]["stock"]:
        print (f"ซื้อสินค้าสำเร็จ จำนวน : {qty}ชิ้น ราคารวม : {stock_db[ST_search]["price"]*qty}")
        stock_db[ST_search]["stock"] -= qty
    else :
        print ("สินค้าคงเหลือไม่เพียงพอ")
print (f"สินค้าคงเหลือ : {stock_db}")
