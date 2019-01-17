#-*-coding:utf-8-*-
# way01:
# number = int(input('number:'))
#
# if 60 <= number < 70:
#     print('及格')
# elif 70 <=  number < 80:
#     print('良好')
# elif 80 <= number < 90:
#     print('好')
# elif 90 <= number <= 100:
#     print('优秀')
# elif number > 100 or number < 0:
#     print('你瞎输什么!我的刀呢!')
# else:
#     print('你要继续努力了!')

#way02:
number = int(input('number:'))
if number >100 or number < 0:
    print('wrong number!')
elif number >= 90:
    print('A')
elif number >= 80:
    print('B')
elif number >= 70:
    print('C')
elif number >= 60:
    print('D')
elif 0<= number < 60:
    print('E')
# else:
#     print('please input a number!')
