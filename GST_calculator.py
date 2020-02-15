# A program which calculates and  displays total amount after including CGST AND SGST on a product
cp = int(input("Enter cost of production "))
cgst = 9
sgst = 9
amt_cgst = (cgst/100)*cp
amt_sgst = (sgst/100)*cp
total = cp+amt_cgst+amt_sgst
print("cost price", cp)
print("Amount after CGST ", amt_cgst)
print("Amount after SGST ", amt_sgst)
print("Total amount inc. CGST and SGST ", total)

