#-*-coding:utf-8-*-
# import sys
#import keyword
# import string
#
# first_chs=string.ascii_letters+'_'
# all_chs=string.ascii_letters+'_'+string.digits
#
# def check_id(idt):
#
#     if  keyword.iskeyword(idt):
#         return  '%s是关键字' % idt
#
#     if idt[0]  not in  first_chs:
#                 print('不合法的字符')
#
#     for ind, ch  in enumerate(idt[1:]):
#         if ch not in all_chs:
#             return  '第%s个字符不合法' % (ind + 2)
#
#     return  '%s是合法字符' % idt
#
# if __name__ == '__main__':
#     result=check_id(sys.argv[1])
#     print(result)