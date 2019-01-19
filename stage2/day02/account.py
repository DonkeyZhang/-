#-*-coding:utf-8-*-
#fname='account.data'  #不建议用耦合度高,直接传参
#shift+F6 -->所有相同变量都会补

import os
import pickle
import time

def save(fname):
    amount = int(input('amount:'))
    comment = input('comment:')
    date= time.strftime('%Y-%m-%d')

    with open(fname,'rb') as fobj:
        all_records = pickle.load(fobj)

    balance =all_records[-1][-2] + amount
    record= (date,0,amount,balance,comment)
    all_records.append(record)

    with open(fname,'wb') as fobj:
        pickle.dump(all_records,fobj)

def cost(fname):
    amount =int(input('cmount:'))
    comment=input('comment:')
    date =time.strftime('%Y-%m-%d')

    with open(fname,'rb') as fobj:
         allrecords=pickle.load(fobj)

    balance =allrecords[-1][-2] - amount
    record=(date,amount,0,balance,comment)
    allrecords.append(record)

    with open(fname,'wb') as fobj:
        pickle.dump(allrecords,fobj)


def query(fname):
    with open(fname,'rb') as fobj:
        all_records = pickle.load(fobj)
        print('%-12s %-8s%-10s%-10s%-20s' % ('date','cost','save','balance','comment'))
        for record in all_records:
            print('%-12s %-8s%-10s%-10s%-20s' % record)

def show_menu():
    cmds={'0':save,'1':cost,'2':query}

    fname='account.data'

    if not os.path.exists(fname):
        init_data =[(time.strftime('%Y-%m-%d'), 0, 0, 1000, 'init')]
        with open(fname,'wb') as fobj:
            pickle.dump(init_data,fobj)

    prompt = '''(0) save
    (1) cost
    (2) query
    (3) quit
    Please input your choice 0/1/2/3: '''

    while True:

        choice =input(prompt).strip()[0]

        if choice not in ('0123'):
            print('Invaild input.')
            continue

        if choice == '3':
            break

        cmds[choice](fname)

if __name__ == '__main__' :
    show_menu()
