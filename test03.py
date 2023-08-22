emp_name = input("ป้อนชื่อพนักงาน : ")
sale_price = input("ป้อนยอดขาย : ")
print("------------------------------------")
comis = float(sale_price) * 10/100

print(f"คุณ {emp_name} ยอดขาย {float(sale_price):.2f} บาท ได้ค่าคอม {comis:.2f} บาท")

print("คุณ",emp_name,"ยอดขาย",float(sale_price),"บาท ได้ค่าคอม",comis,"บาท")

print("คุณ " +str(emp_name) +"ยอดขาย" +str(sale_price)+ "บาท ได้รับค่าคอม"+str(comis)+ "บาท")

print("คุณ {} ยอดขาย {} บาท ได้ค่าคอม {} บาท " .format(emp_name,sale_price,comis) )
