# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 08:35:42 2023

@author: poorn
"""

age=6#fetch from database

argumnet=0

def start(age,marks_list): 
    score_list=list(marks_list)
    #print(score_list)
    k=1
        
    for k in range (10):
        print('''Subjects are:
              1.Addition 
              2.Subsrtaction
              3.Multiplication
              4.Division
              5.english
              0.Exit''')
        argument=int(input("Enter your choice:"))
        
        if(argument==0 ) :
            return score_list
            
        elif(argument== 1) :
           previous_marks=score_list[0] 
           print("your previous addition score",previous_marks)#fetch from database
           from funadsum import main
           add_marks=str(main(previous_marks,age))
           score_list[0]=add_marks
           
           #return score_list
           
           #update in the database
        elif(argument==2 ) :
            previous_marks=score_list[1] 
            #fetch from database
            from sub import main 
            score_list[1]=str(main(previous_marks,age))
            
        elif(argument==3 ) :
            previous_marks=score_list[2] #fetch from database
            from mult import main
            score_list[2]=main(previous_marks,age)
        elif(argument==4 ) :
            previous_marks=score_list[3] #fetch from database
            from div import main
            score_list[3]=main(previous_marks,age)
        elif(argument== 5) :
            previous_marks=int(score_list[4])
            from english import main
            score_list[4]=main(previous_marks,age)
        else:
            print("Enter valid choice")

        #score_list=choose_ur_subject(argument,score_list)
        #print(score_list)
        #return score_list
        
start(age, ('34', '18', '12', '2', '2', 0))    