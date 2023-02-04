########## first metod (Simple) ########

num1,num2 = 0,1
for _ in range(int(input())):
    num1,num2 = num2,num1+num2
    print(num1,end=' ')


####### second method (Recursion)

def fibo (num):
    if num == 1:
        return 1
    elif num == 2 :
        return 1
    return fibo(num-1) + fibo(num-2)
print(fibo(int(input())))

###### third metod (List_index) #####
def fibo_list(num,lst=[1,1]):
    for _ in range(num-2):
        lst.append(lst[-1]*lst[-2])
    return lst

print(fibo(int(input())))
