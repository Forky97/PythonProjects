class Fibo:
    def __init__(self,number=None):
        self.number = number

    ########## first metod (Simple) ########

    def fibo_simple(self,num1=0,num2=1):
        for _ in range(self.number):
            num1,num2 = num2,num1+num2
        return num1

    ####### second method (Recursion)

    def fibo_recursion (self,num):
        if  num == 1:
            return 1
        elif num == 2 :
            return 1
        return self.fibo_recursion(num-1) + self.fibo_recursion(num-2)

    ###### third metod (List_index) #####
    def fibo_list(self,lst=[1,1]):
        for _ in range(self.number-2):
            lst.append(lst[-1]+lst[-2])
        return lst

operator = Fibo(int(input('Put you number : ')))


