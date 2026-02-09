
basic_pay = float(input("Enter Basic Pay: "))
da = float(input("Enter DA: "))


hra = 0.10 * basic_pay
ta = 0.02 * basic_pay
pf = 0.05 * basic_pay

grosssalary = basic_pay + hra + ta + da - pf
print("HRA:", hra)
print("TA:", ta)
print("PF:", pf)
print("Gross Salary:", grosssalary)




