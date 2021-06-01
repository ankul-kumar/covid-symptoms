

def logo():
    print("####################################################################################")
    print("#                   check weather you have corona virus                            #")
    print("####################################################################################")
    
def question():
    name=input("Enter your name:")
    age=input("Enter your age:")
    gender=input("Enter your gender:")
    print("Are you experiencing of the following symptoms:")
    print("1 -Cough")
    print("2 -Fever")
    print("3 -Difficulty in breathing")
    print("4 -None of these")    
    symp=int(input("enter your option:"))
    print("have you ever had any of the following")
    print("1-Diabetes")
    print("2-HyperTension")
    print("3-Lungs Diseases")
    print("4-Heart Diseases")
    print("5-None of these")
    
    dis=int(input("Enter your option"))
    print("Have you Travel internationally within 15 days(yes/no)")
    print("1-yes")
    print("2-no")
    Enter1 = input("Enter your option:")
    print("have you recently interacted with corona positive person")
    print("1-yes")
    print("2-no")
    Enter = input("Enter your option:")
    if symp==1 or dis ==1 or symp==2 or dis==2 or symp==3 or dis==3 or dis==4:
      print("YOU ARE COVID POSITIVE")
    else :
         print("YOU ARE COVID NEGETIVE")
        
    	  
y=logo()
x=question()    
    
    
