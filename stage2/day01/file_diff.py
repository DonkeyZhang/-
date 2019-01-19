#-*-coding:utf-8-*-

with open('/etc/passwd') as fobj:
    aset = set(fobj)

with open('/tmp/mima') as fobj:
    bset =  set(fobj)

with open('/tmp/myfile','w') as fobj:
    fobj.writelines(bset -aset)