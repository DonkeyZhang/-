#-*-coding:utf-8-*-
#way01:
# f1=open('/bin/ls','rb')
# f2=open('/tmp/list','wb')
# while True:
#     data=f1.read(4096)
#     f2.write(data)
# f1.close()
# f2.close()

#way02:
# src_fname='/bin/ls'
# dst_fname='/tmp/list'
#
# with open(src_fname,'rb') as src_fobj:
#     with open(dst_fname,'wb') as dst_fobj:
#         while True:
#             data = src_fobj.read(4096)
#             #if len(data) == 0:
#             #if data == b'':
#             if not data:
#                 break
#             dst_fobj.write(data)

#way03:
import  sys
def copy(src_name, dst_fname):
    with open(src_name, 'rb') as src_fobj:
        with open(dst_fname,'wb') as dst_fobj:
            while True:
                data = src_fobj.read(4096)
                #if len(data) == 0:
                #if data == b'':
                if not data:
                    break
                dst_fobj.write(data)
copy(sys.argv[1],sys.argv[2])