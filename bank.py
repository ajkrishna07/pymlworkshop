import csv

class Bank(object):
    def __init__(self,init_name, init_no, init_bal, init_pin):
        self.name = init_name
        self.no = init_no
        self.bal = int(init_bal)
        self.pin = init_pin
        with open("tran.csv","w",newline="") as myfile:
            wr=csv.writer(myfile,dialect="excel")
            wr.writerow([self.name,self.no,self.bal])
            
    def deposit(self, i):
        with open("tran.csv","a",newline="") as myfile:
            wr=csv.writer(myfile,dialect="excel")
            prev=self.bal
            self.bal += int(i)
            wr.writerow([self.name,self.no,prev,'+'+i,self.bal])
            
    def withdraw(self, i):
        i=int(i)
        prev=self.bal
        if (prev-i) >= 0:
            with open("tran.csv","a",newline="") as myfile:
                wr=csv.writer(myfile,dialect="excel")
                self.bal -= i
                wr.writerow([self.name,self.no,prev,'-'+str(i),self.bal])
        else:
            print('Insufficient balance')  
            
    def statement(self):
        with open("tran.csv") as myfile:
            reader=csv.reader(myfile)
            for row in reader:
                print(row)   
                
    @property
    def balance(self):
        return "Name: {}\nAcc no: {}\nAcc balance = Rs. {}".format(self.name,self.no,self.bal)
    
name = input('Enter name: ')
no = input('Enter account number: ')
bal = input('Enter initial balance: ')
pin = input('Enter pin: ')
obj = Bank(name,no,bal,pin)
pin=input('\nEnter pin: ')

while True:
	if pin==obj.pin:
		choice=int(input('Enter choice\n1. Deposit\n2. Withdraw\n3. View details\n4. Statement\n5. Exit\n'))
		if choice==1:
			dep=input('Enter amount to deposit: ')
			obj.deposit(dep)
		elif choice==2:
			wit=input('Enter amount to withdraw: ')
			obj.withdraw(wit)
		elif choice==3:
			print(obj.balance)
		elif choice==4:
			obj.statement()
		else:
			quit()
	else:
		print('Inavlid pin')
		pin=input('Enter pin: ')