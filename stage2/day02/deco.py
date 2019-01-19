#-*-coding:utf-8-*-
def deco(func):
    def color():
        return '\033[31;1m%s\033[0m' %func()
    return  color

def hello():
    return  'hello world!'

@deco
def weclome():
    return 'hello China!'


if __name__ == '__main__':
    a=deco(hello)
    print(a())

    hello=deco(hello)
    print(hello())

    print(weclome())
