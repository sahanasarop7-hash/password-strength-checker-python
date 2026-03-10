#Password Strength Checker

password=input("Enter the password:")
strength=0
if len(password)>=8:
             strength+=1
for i in password:
    if i.isupper()==True:
        strength+=1
    elif i.islower()==True:
        strength+=1
    elif i.isdigit()==True:
        strength+=1
    else:#special character or punctuation
        strength+=1

if strength <=2:
    print("Weak Password")
elif strength ==3 or strength ==4:
    print("Moderate Password")
else:
    print("Strong Password")
