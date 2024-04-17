marks1 = int(input("Enter marks1 : "))
marks2 = int(input("Enter marks2 : "))
marks3 = int(input("Enter marks3 : "))

avg = (marks1 + marks2 + marks3)//3

def marks(marks1, marks2, marks3):

    if(avg >= 90) and (avg <= 100):
            print('A')
    elif(avg >= 80) and (avg <= 89):
            print('B')
    elif(avg >= 70) and (avg <= 79):
            print('C')
    elif(avg >= 60) and (avg <= 69):
            print('D')
    else:
            print('F')        
 
marks(marks1,marks2,marks3)