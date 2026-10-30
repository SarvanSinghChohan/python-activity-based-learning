#58-->
valid_books=["book1","book2","book3","book4","book5"]
books=['book1'*3,'book2'*3,'book3'*3,'book4'*3,'book5'*3]
print("available actions: take , return")
request=input("what is your request: ")
if request=="take":
    name=input("what book do you want: ")
    if name in books:
        books.remove(name)
        print("return within 5 days!")
    else:
        print("this is not available")
elif request=="return":
    name=input("what book are you returning: ")
    if name in valid_books:
        books.append(name)
    time=int(input("for how many days did you take this book?: "))
    if time>5:
        fine=50
        for i in range(5,time):
            fine=fine+50
    else:
        fine=0
    print(f"you need to pay {fine}")