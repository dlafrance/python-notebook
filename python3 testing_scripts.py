mynumber=1
myfloat=3.14
mystring='Hello World!'
myboolean=True
mylist=[1,2,3,4,5]

print(mynumber)
print(myfloat)
print(mystring)
print(myboolean)
print(mylist)

print(f'{type(mynumber)}, {type(myfloat)}, {type(mystring)}, {type(myboolean)}, {type(mylist)}')

#Question 1
x = [1,2,3,4,5,6,7,8,9]
x_double= [i * 2 for i in x[3:7]]
print(x_double)

#Question 2
x_odds = x[::2]
x_even = x[1::2]
print(x_odds)
print(x_even)

#Question 3
for i in range(1, 101):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)