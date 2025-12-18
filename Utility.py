class multipleFuncs():
    def oddOrEven():
        num=int(input("Enter the Number"))
        if(num %2 == 1):
            message = "Odd Number"
        else:
            message = "Even Number"
        return message; 
    
    def BMI():
        index=int(input("Enter the BMI Index:"))
        if(index<19):
            print("Under Weight")
            bodyState="Under Weight"
        elif(index<25):
            print("Normal Weight")
            bodyState="Normal Weight"
        elif(index<30):
            print("Over Weight")
            bodyState="Over Weight"
        elif(index<35):
            print("Obisity Class 1")
            bodyState="Obisity Class 1"
        elif(index<40):
            print("Obisity Class 2") 
            bodyState="Obisity Class 2"
        else:
            print("Obisity Class 3")
            bodyState="Obisity Class 3"
        return bodyState    