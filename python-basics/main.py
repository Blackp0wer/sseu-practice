print("Hello, Wolrd!")


my_list = [1,2,3,4,5,6,7,8,9,10]
sum = 0

for i in my_list:
    sum+=i

print(sum)

def factorial(num):
    temp = 1
    for i in range(num):
        temp*=i+1
    return temp

print(factorial(5))