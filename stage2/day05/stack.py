#-*-coding:utf-8-*-
#列表模拟栈结构
#1.程序是交互的,思考有什么提示,用户怎么作答
#2.思考有哪些功能,将这些功定义成函数,编写程序框架
#3.在主程序调用相关函数
#4.



stack = []

def push_it():
  item =input('item to push: ').strip()
  if item:
      stack.append(item)

def pop_it():
    if stack:
        print('form stack poped %s' % stack.pop())

def view_it():
    print(stack)

def show_menu():
    cmds = { '0': push_it,'1':pop_it, '2':view_it }
    prompt='''(0)push it
(1) pop it 
(2) view it
(3) quit
please input your choice(0/1/2/3): '''

    while True:
        choice = input(prompt).strip()[0]
        if choice not in ('0123'):
            print('Invaild input. Try again.')
            continue
        if choice == '3':
            print('bye-bye')
            break
        cmds[choice]()
        if choice == '0':
            push_it()
        elif choice == '1':
            pop_it()
        else:
            view_it()

if __name__ == '__main__':
    show_menu()

