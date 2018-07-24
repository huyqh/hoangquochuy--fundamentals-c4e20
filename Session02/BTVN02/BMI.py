h = int(input("Nhap vao chieu cao cua ban (cm):"))
w = int(input("Nhap vao can nang cua ban (kg):"))
BMI = w/(h*h*0.0001)
print(BMI)
if BMI < 16:
    print("Ban gay qua")
elif BMI < 18.5:
    print("Ban dang thieu can")
elif BMI < 25:
    print("Co the binh thuong")
elif BMI < 30:
    print("Ban dang thua can")
else:
    print("Beo phi")
    
