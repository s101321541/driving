country = input("國籍:") 
age = input("請輸入年齡:")
age = int(age)
if country == "taiwan":
	if age >= 18:
		print("你可以開車")
	else:
		print("你不能考駕照")
elif country == "US":
	if age >=16:
		print("你可以開車")
	else:
		print("你不能考駕照")
