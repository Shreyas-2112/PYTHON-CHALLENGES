print("Enter a number which you feel is lucky for you (numerator):")
numb = int(input())
print("Enter a number which you feel is unlucky for you (denominator): ")
numd = int(input())

if numb%numd==0:
    print("\n" +str(numb)+ " is divisible by " +str(numd))
else:
    print("\n" +str(numb)+ " is not divisible by " +str(numd)) 
