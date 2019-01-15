#-*-coding:utf-8-*-
# import sys
# import password
# import subprocess
#
# def adduser(username,password,userfile):
#     user_info = '''username: %s
# password: %s
# ''' % (username,password)
#
#     subprocess.call('useradd %s' % username,shell=True)
#     subprocess.call(
#         'echo %s|passwd --stdin %s' % (password,username),
#         shell=True
#     )
#
#     with open(userfile, 'a') as fobj:
#         fobj.writelines(user_info)
#
# if __name__ == '__main__':
#     password= password.gen_pass()
#     adduser(sys.argv[1],password,'/mnt/user.info')






