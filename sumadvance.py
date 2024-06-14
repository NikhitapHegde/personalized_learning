import csv
import random
def sum(x):
    print("what is the sum of ",x[0],"and",x[1],"is")
    k=1
    while(k!=0 and k!=5):
        s=int(input("----"))
        if(s==int(x[2])):
            print("YESS!! you are right!!")
            k=0
        elif(s==int(x[2])-1 or s==int(x[2])+1):
            print("It's not exactly crt :( you are almost close try again")
            k+=1
        else:
            print("It's a wrong answer:(")
            p=int(input("Do you want to try it again!?then press 1 else press zero to see the answer"))
            if(p==1):
                k=k+1
            else:
                k=0
    print(x[0],"+",x[1],"=",x[2]);
with open('C:\Users\user\Downloads\mathss1.csv','r')as source:
    p=csv.reader(source)
    a=[]
    for r in p:
        a.append(r);
    random_question=random.choice(a[10:40])
    sum(random_question)
        