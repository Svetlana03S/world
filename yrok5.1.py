number = ["A","B","C"]
i_B = number.index("B")
print(i_B)

number.insert(i_B, "G")
print(number)

number[i_B] = "U"
print(number)

number.pop()
print(number)

number.pop(1)
print(number)

number.remove("B")
print(number)

number = list (["A","B","C","H","D","H"])
count_H = number.count("H")
print(count_H)

number.clear()
print(number)

number = list (["A","B","C","H","D","H"])
number.reverse()
print(number)

number = list (["A","B","C","H","D","H"])
number.sort()
print(number)

number = ["1","2","3","4","5","6"]
m = max(number)
print(m)

number = ["1","2","3","4","5","6"]
m = min(number)
print(m)

number = list(["1","2","3","4","5","6"])
print(number)
if "3" in number:
    number.remove("3")
print(number)

number = list(["1","3","2","3","4","5","3","6"])
print(number)
while "3" in number:
    number.remove("3")
print(number)

number = list(["1","3","2","3","4","5","3","6"])
del number[1]
print(number)

number = list(["1","3","2","3","4","5","3","6"])
del number[:3]
print(number)

number = list(["1","3","2","3","4","5","3","6"])
del number[3:]
print(number)

number = list(["1","3","2","3","4","5","3","6"])
del number[0:8:2]
print(number)

number = [10,20,30,40,50,60]
number[1:4] =[15,46]
print(number)

number = [[10,20,30,40,50,60],[10,20,30,40],[40,50,60]]
print(number[1][3])

number = [[[10,20,30,40,50,60],[10,20,30,40],[40,50,60]],[[10,20,30,40,50,60],[10,20,30,40]]]
print(number[0][1][2])



