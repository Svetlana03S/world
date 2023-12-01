number = [1,2,3,4,5]
print(number)

number = list([1,2,3,4,5])
print(number)

name = "Alex"
print(name)

name1 = list(name)
print(name1)

number = [1,2,3,4,5]*2
print(number)

image = [0]*256
print(image)

image = [0,256]*8
print(image)

image = ["  0","255"]*32
print(image)

number = ["A","B","C"]
print(number)

print(number[0])

number = [1,2,3,4,5]
print(number)
for elem in number:
    print(elem)
    elem +=1
    print(elem)
    print("--------")
    
number = [1,2,3,4,5]  
i = 0
while i < len(number):
    print([i])
    i += 1
    
number1 = [1,2,3,4,5]
print(number1)

number2 = list([1,2,3,4,5])
print(number2)  

if number1==number2:
    print("Yes")
else:
    print("No")
    
number1 = [1,2,3,4,5]
print(number1)

number2 = list([1,2,3,4,5,6])
print(number2)  

if number1==number2:
    print("Yes")
else:
    print("No")    

number1 = [1,2,3,4,5,6,7,8,9]
print(number1)  
new_number = number1[:1]
print(new_number)

number1 = [1,2,3,4,5,6,7,8,9]
print(number1)  
new_number = number1[4:]
print(new_number)

number1 = [1,2,3,4,5,6,7,8,9]
print(number1)  
new_number = number1[2:7]
print(new_number)

number1 = [1,2,3,4,5,6,7,8,9]
print(number1)  
new_number = number1[2:7:2]
print(new_number)

number1 = [1,2,3,4,5,6,7,8,9]
print(number1)  
new_number = number1[-2:-7]
print(new_number)

number1 = [1,2,3,4,5,6,7,8,9]
print(number1)  
new_number = number1[-2:-7:2]
print(new_number)

number = ["A","B","C"]
number.append("D")
number.append("I")
number.extend(["F","G","H"])
print(number)
