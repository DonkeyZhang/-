#-*-coding:utf-8-*-
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return  '<<%s>> ' % self.title

    def __call__(self):
        print('<<%s>> 是 %s 写 的' % (self.title,self.author))

if __name__ == '__main__':
    core_py =Book('Core Python', 'wesley')
    print(core_py)
    core_py()