#-*-coding:utf-8-*-

try:
    num = int(input('number: '))
    result = 100 /num

except (ValueError,ZeroDivisionError):
    print('Invalid input.')
except (KeyboardInterrupt, EOFError):
    print('end')
else:
    print(result)
finally:
    print('Done')


