square = [x**2 for x in range(200)]
print(square)
number =[2,3,4,5]
double = [x*2 for x  in number]
print(double)

numbers =[1,2,3,4,5,6,7,8,9,]
even = [x for x in numbers if x % 2 == 0]
print(even)


names =['ulrich', 'armel', 'fely','danny','amilo']
short_names = [name for name in names if len(name) < 5]
print(short_names)

numbers = [1, 2,3,4,5,6,7,8,9]

divide_by2 = [i/2 for i  in numbers if i<11]
print(divide_by2)


# labels 

labels =["Even" if x % 2 ==0  else "Odd" for x in numbers]
print(labels)