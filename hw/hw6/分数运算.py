def find_gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

class Rational:
    def __init__(self,numerator,denominator=1):
        gcd=find_gcd(abs(numerator),abs(denominator))
        self.numerator,self.denominator=numerator//gcd,denominator//gcd
        if self.denominator<0:
            self.denominator=-self.denominator
            self.numerator=-self.numerator

    def add(self1,self2):
        new_numerator=self1.numerator*self2.denominator+self2.numerator*self1.denominator
        new_denominator=self1.denominator*self2.denominator
        return Rational(new_numerator,new_denominator)
    
    def sub(self1,self2):
        new_numerator=self1.numerator*self2.denominator-self2.numerator*self1.denominator
        new_denominator=self1.denominator*self2.denominator
        return Rational(new_numerator,new_denominator)

    def mul(self1,self2):
        new_numerator=self1.numerator*self2.numerator
        new_denominator=self1.denominator*self2.denominator
        return Rational(new_numerator,new_denominator)
    
    def div(self1,self2):
        new_numerator=self1.numerator*self2.denominator
        new_denominator=self1.denominator*self2.numerator
        return Rational(new_numerator,new_denominator)

    def printRational(self):
        if self.denominator==1:
            print(self.numerator)
        else:
            print(f'{self.numerator}/{self.denominator}')

    def printReal(self):
        print(round(self.numerator/self.denominator,2))

op_dict1={'1':Rational.add,'2':Rational.sub,'3':Rational.mul,'4':Rational.div}
op_dict2={'1':Rational.printRational,'2':Rational.printReal}

op1=input()
num=list(map(int,input().split()))

n=Rational(num[0],num[1])
m=Rational(num[2],num[3])
res=op_dict1[op1](n,m)

op2=input()
op_dict2[op2](res)
