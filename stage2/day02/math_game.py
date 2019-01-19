#-*-coding:utf-8-*-
#函数

import random
#
# def add(x,y):
#     return x+y
#
# def sub(x,y):
#     return x-y


def exam():
    #cmds={'+':add,'-':sub}
    cmds = {'+': lambda x,y:x+y, '-': lambda x,y:x-
                                                 y}
    nums= [random.randint(1,100) for i in  range(2)]
    nums.sort(reverse=True)

    #nums.sort()       #默认升序
    #nums.reverse()

    op=random.choice('+-')

    result=cmds[op](*nums)

    # if op =='+':
    #     result = nums[0] +nums[1]
    # else:
    #     result =nums[0] - nums[1]

    prompt ='%s %s %s = ' %(nums[0], op ,nums[-1])

    #answer =int(input(prompt))
    counter =0
    while counter <3:
        try:
            answer = int(input(prompt))
        except:
            print()
            continue
        if answer == result:
            print('Very Good!')
            break
        else:
            print('Wrong number!')
            counter +=1
    else:
        print('%s%s' % (prompt,result))


def main():
    while True:
        exam()
        try:
            yn = input('Continue(y/n)?').strip()
        except IndentationError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if  yn in 'nN':
            print('Bye-bye')
            break


if __name__ == '__main__':
    main()