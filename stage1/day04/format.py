#-*-coding:utf-8-*-]
import  mktxtfile

content = mktxtfile.get_content()

print('+%s+' % ('*' * 48))

for line in content:
    print('+{:^48}+'.format(line))

print('+%s+' % ('*' * 48))