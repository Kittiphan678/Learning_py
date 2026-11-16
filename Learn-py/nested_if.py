PV_username,PV_password = "min0006x","1234"
print ("===== ระบบสมัครสมาชิก =====")
while True:
    username = input("กรุณากรอก username : ")
    if username == PV_username :
        print ("มี username ")
        password = input("กรุณากรอก password : ")
        if password == PV_password :
            print ("login success")
            break
        else:
            print ("login fail (กรุณาลองใหม่)")
    else:
        print ("ไม่มี username (กรุณาลองใหม่)")
