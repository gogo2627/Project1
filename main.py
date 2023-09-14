def add_func(n1, n2) :
    res = n1 + n2
    return res

def sub_func(n1, n2) :
    return n1 - n2

def mul_func(n1, n2) :
    return n1 * n2

def div_func(n1, n2) :
    return n1 / n2


num1 = 100
num2 = 200

result = add_func(num1, num2)
print(num1, '+' , num2 , '=', result)

result = sub_func(num1, num2)
print(num1, '-' , num2 , '=', result)

result = mul_func(num1, num2)
print(num1, '*' , num2 , '=', result)

result = div_func(num1, num2)
print(num1, '/' , num2 , '=', result)
