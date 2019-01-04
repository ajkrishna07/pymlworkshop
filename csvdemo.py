import csv

def addp(name,gender,email,event):
    with open("data.csv","a",newline="") as myfile:
        wr=csv.writer(myfile,dialect="excel")
        if(checkp(name) and checkemail(email)):
            wr.writerow([name,gender,email,event])

def viewp():
    with open("data.csv") as myfile:
        reader=csv.reader(myfile)
        for row in reader:
            print(row)
        
def checkp(name):
    l=[]
    with open("data.csv") as myfile:
        reader=csv.reader(myfile)
        for row in reader:
            l.append(row[0])
        if name not in l:
            return True
        else:
            print('Participant already exists')
            return False
            
def checkemail(email):
    email=list(email)
    if '@' not in email:
        print('Invalid email')
        return False
    if '.'not in email:
        print('Invalid email')
        return False
    return True