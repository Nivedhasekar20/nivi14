phy=int(input("phy: "))
chem=int(input("chem: "))
maths=int(input("maths: "))
comp=int(input("comp: "))
bio=int(input("bio: "))
avg=(phy+chem+maths+comp+bio)/5
print(avg)
if(avg>=90):
    print("Grade: A")
elif(avg>=80):
    print("Grade: B")
elif(avg>=70):
    print("Grade: C")
elif(avg>=60):
    print("Grade: D")
else:
    print("Grade: F")
