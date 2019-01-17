#-*-coding:utf-8-*-
#way01:调用函数
# def gen_fib():
#     fib = [0, 1]
#     for i in range(8):
#         fib.append(fib[-1] + fib[-2])
#     print(fib)
#
# gen_fib()

#way02:传参数
def gen_fib(length):
    fib = [0, 1]
    for i in range(length - 2):
        fib.append(fib[-1] + fib[-2])
    return fib

#a = gen_fib(20)
#print(a)
n =int(input('length:'))
b = gen_fib(n)
with open( '/tmp/fib.txt','w') as fobj:
    fobj.write(str(b))   # b为列表,只能输入字符str()
print(b)