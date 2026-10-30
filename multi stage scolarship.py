#70-->multi stage scholarship
details=[]
details.append(input("Enter your name: "))
details.append(int(input("Enter your marks percentage: ")))
details.append(int(input("Enter your attendance percentage: ")))
details.append(int(input("Enter your income: ")))
if details[1]>60 and details[2]>70:
        if details[3]>10000:
            category='Merit-cum-Means scholarship'
        else:
            category='Merit-Based scholarship'
else:
    if details[3]>10000:
        category='Need-Based scholarship'
    else:
        category='no category'
print(f'the student can apply for scholarship under {category}')