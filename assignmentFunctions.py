class SubfieldsInAI():
    def subfields():
        fields = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for field in fields:
            print(field)
            
class OddEven():
    def oddOrEven():
        num=int(input("Enter a Number"))
        if(num %2 == 1):
            print(f"{num} is Odd Number")
        else:
            print(f"{num} is Even Number")
        
class ElegiblityForMarriage():
    def elegible(gender, age):
        print("Your Gender: ", gender)
        print("Your Age: ", age)
        if(gender == "Male"):
            if(age >=21):
                print("Eligible for marriage")
            else:
                print("Not Eligible for marriage")
        else:
            if(age >=18):
                print("Eligible for marriage")
            else:
                print("Not Eligible for marriage")
                
class FindPercent():
    def percentage(marks):
        print("FindPercent.percentage()")
        total = sum(marks)

        for i in range(len(marks)):
            m = marks[i]
            print(f"Subject{i+1}= {m}")

        print("Total  :", total)
        percentage = total / len(marks)
        print("Percentage :", percentage)

class Triangle():
    def areaOfTriangle(height, breadth):
        print("Height:", height)
        print("Breadth:", breadth)
        print("Area formula: (Height*Breadth)/2")
        area = (height * breadth) / 2
        print("Area of Triangle:", area)

    def perimeterOfTriangle(h1, h2, breadth):
        print("Height1:", h1)
        print("Height2:", h2)
        print("Breadth:", breadth)
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter = h1 + h2 + breadth
        print("Perimeter of Triangle:", perimeter)