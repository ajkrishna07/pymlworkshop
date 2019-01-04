import csvdemo

done=0
while done==0:
    print('Enter choice:\n1. View participants\n2. Add participants\n3. Exit')
    choice=int(input())
    if choice==1:
        csvdemo.viewp()
    elif choice==2:
        name=input('Enter name: ')
        gender=input('Enter gender: ')
        email=input('Enter email: ')
        event=input('Enter event: ')
        csvdemo.addp(name,gender,email,event)
    else:
        done=1    