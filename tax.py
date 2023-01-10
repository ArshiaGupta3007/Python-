gross_income = int(input("ENTER GROSS INCOME : "))
dependent=int(input("ENTER NUMBER OF DEPENDENTS : "))
tax_in=gross_income - 10000 - (3000*dependent)
tax_rate=0.20
tax = tax_in * tax_rate
print("INCOME TAX = ",tax)