# SI = P * N * R / 100

principal = int(input("Enter the amount borrowed : "))
years = float(input("Enter the period in years : "))
rate = float(input("Enter rate of inerest : "))

interest = principal * years * rate / 100
print("Simple Interest Calc :", str(interest))