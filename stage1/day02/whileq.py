# #-*-coding:utf-8-*-
# result = 0 #用于保存结果
# counter = 1 #计数器,不断累加到result
#
# while counter<=100:
#     result +=counter
#     counter +=1
#  print(result)
result = 0
counter = 0

while counter < 100:
    counter += 1
    if counter % 2 == 1: #
        continue
    result +=counter
print(result)