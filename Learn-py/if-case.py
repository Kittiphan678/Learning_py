print ("1 ถอนเงิน 2 ฝากเงิน 3 ยอดเงิน")
service = int(input("กรุณาเลือกบริการ (1-3): "))
match service:
    case "1": print ("ถอนเงิน")
    case "2": print ("ฝากเงิน")
    case "3": print ("ยอดเงิน")
    case "": print ("error")