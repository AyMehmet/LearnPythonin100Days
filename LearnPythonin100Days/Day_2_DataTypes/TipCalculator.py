total_bill = input("enter total bill")
customer_number=input("enter customer number")
tip_percentage=input("enter tip percentege exm:10,20,15....")
result= round((int(total_bill)*(int(tip_percentage)/100)+int(total_bill))/int(customer_number))
print(result)

