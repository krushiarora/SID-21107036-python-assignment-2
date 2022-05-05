a= float(input("Enter the no. here",))
b= float(input("Enter the no. here",))
c= float(input("Enter the no. here",))

d= a+b>c
print(d,)
e= b+c>a
print(e,)
f= c+a>b
print(f)

answer= str(d & e& f)
answer= answer.replace("True","Yes")
answer= answer.replace("False","No")
print(answer)
