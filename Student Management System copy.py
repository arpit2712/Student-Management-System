


# Student Management System:

'''In this project we will make a student management system. In this system we use file handling
to create a text file and in this file we enter name of students and all the data of
students.'''



obj=open("SMS.txt","a")
obj.write("")
obj.close()

def View_Student_List():
    obj=open("SMS.txt","r")
    data=obj.read()
    print(data)
    obj.close()

def Add_Student_Data():
    
    obj=open("SMS.txt","a")
    n=input("Enter Student Name:")
    data='''
'''
    obj.write(data)
    obj.write(n)
    obj.close()

    obj=open("SMS.txt","r")
    obj.read()
    obj.close()
def removename():
    sms=open("SMS.txt","a+")
    a=input("Search Student name to remove:")
    a=a+"\n"
    sms.seek(0)
    rn=sms.readlines()
    if a in rn:
        rn.remove(a)
        print("Removed Student Name from List",a)
        s=''
        s=''.join([str(i) for i in rn])
        f1=open("SMS.txt","w")
        f1.write(s)
        f1.close()
    else:
        print("Student not found")

    sms.close()
        
def Searched_Student_List():
    obj=open("SMS.txt","r")
    data=obj.read()
    obj.close()
    n=input("Enter name of Student:")
    if(n in data):
        print("Searched data Found!!")

    else:
        print("Searched data not Found!!")


print("_"*60)
print("   *****Welcome to Student Management System *****")
print("_"*60)


print("Choose any one option:")
print("(1)TO view student List")
print("(2)TO Add student data")
print("(3)TO Remove the data")
print("(4)TO Searched data")
print("(5)Exit")



while(True):
    ch=int(input("Choose any one option:"))
    if(ch==1):
        View_Student_List()

    elif(ch==2):
        Add_Student_Data()

    elif(ch==3):
        removename()

    elif(ch==4):
        Searched_Student_List()

    elif(ch==5):
        exit()

    msg=input("Do you want to continue this loop(y/n)?:")
    
    if(msg=="y"):
        continue
    elif(msg=="n"):
        exit()
 
