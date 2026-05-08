#bill = 500

#tax_rate = 2.4
 
#total_tax = (bill * tax_rate) / 100

#print ('Total tax', total_tax)

def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100, 2)

print ('Total tax', calculate_tax(175.00, 15))
print ('Total tax', calculate_tax(500.00, 10))
    