import csv
import random
math_score=10
progress=[]
progress=0
def sum(x):
    print("what is the sum of ",x[0],"and",x[1],"is")
    k=1
    while(k!=0):
        s=int(input("----"))
        if(s==int(x[2])):
            print("YESS!! you are right!!")
            k=0
            global math_score
            math_score+=1
            global progress
            progress+=1
            if(k==0):
                return progress
            else:
                return 1
        elif(s==int(x[2])-1 or s==int(x[2])+1):
            print("It's not exactly crt :( you are almost close try again")
            k+=1
            progress=0
            if(k==5):
                print("wrong answer:( Try answering next one")
                break;
                
        else:
            print("It's a wrong answer:(")
            p=int(input("Do you want to try it again!?then press 1 else press zero to see the answer"))
            progress=0
            if(p==1):
                k=k+1
            else:
                k=0
            if(k==5):
                print("wrong answer:( Try answering next one")
                break;
                
            
    print(" the answer is",x[0],"+",x[1],"=",x[2]);
with open('C:\Users\user\Downloads\mathss1.csv','r')as source:
    p=csv.reader(source)
    a=[]
    for r in p:
        a.append(r);
    temp=0
    
    while(progress<4):
        temp+=1
        sum(random.choice(a[11:30]))
        print("progress : ",progress)
        if(temp==3 and progress==3):
            print("3 consequtive answers correct!!extra score")
            math_score+=1
            sum(random.choice(a[30:100]))
        elif(temp>10):
            while(progress<4):
                sum(random.choice(a[1:12]))
        
    print("your maths score: ",math_score,"!!!")
        
    