#12-->student attendance recovery
attended=int(input("enter classes attended: "))
conducted=int(input("enter classes conducted: "))
print("required 75% attendance")
print(f'your attendance is {100*attended/conducted:.2f} ')
to_attend=0
present=100*attended//conducted
if present<75:
    while present<75:
        to_attend=to_attend+1
        present=((to_attend+attended)/(conducted+to_attend))*100
    print(f"you need to attend {to_attend} upcoming classes to aquire required attendance")
else:
    print(f'you have required attendance')