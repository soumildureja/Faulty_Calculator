# This Is The Calculator Which Gives Incorrect Answer For Only Three Questions
a="Answer"
print("THIS THE MOST TRUSTED CALCULATOR")
print("(+)For Addition\n" "(-)For Subtraction\n" "(*)For Multiplication\n" "(/)For Division")
n1=(input())
print("ENTER YOUR FIRST NUMBER")
n2=int(input())
print("ENTER YOUR SECOND NUMBER")
n3=int(input())
if n2 ==67 and n3==89 and n1=="+":
    print(a+"180")
elif n2==58 and n3==12 and n1=="-":
        print(a+":19")
elif n2==78 and n3==90 and n1=="/":
    print(a+":3")
elif n2==45 and n3==78 and n1=="*":
    print(a+":890")
else:
    if n1=="+":
        print("Answer:",int(n2)+int(n3))
    elif n1=="-":
        print("Answer:",int(n2)-int(n3))
    elif n1=="/":
        print("Answer:",int(n2)/int(n3))
    elif n1=="*":
        print("Answer:",int(n2)*int(n3))
