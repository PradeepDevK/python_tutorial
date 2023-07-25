# SI = P * N * R / 100

principal = int(input("Enter the amount borrowed : "))
years = float(input("Enter the period in years : "))
rate = float(input("Enter rate of inerest : "))

interest = principal * years * rate / 100
#print("Simple Interest Calc :", str(interest))

#print("Simple Interest on the principal amount", principal, "For a actual period of", years, "years at the rate of", str(rate) + "% is $", interest)

print(f"Simple Interest on the principal amount {principal}, For a actual period of {years} years at the rate of {rate}% is ${interest}")
