#19-->multi shopping
products=[]
total=0
budget=float(input("Enter your shopping budget: Rs."))
n=int(input("Enter number of products: "))
for i in range(n):
    name=input("Enter product name: ")
    price=float(input("Enter price: ₹"))
    quantity=int(input("Enter quantity: "))
    cost=price*quantity
    total=total+cost
    products.append([name, price, quantity, cost])
for j in products:
    print(j[0], "- Rs.", j[1], "x", j[2], "= Rs.", j[3])
print("Total bill: Rs.", total)
if total <= budget:
    print("Shopping is within your budget.")
else:
    print("Shopping exceeds your budget.")
    print("Amount exceeded: ₹", total - budget)