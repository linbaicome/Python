# -*- coding: cp936 -*-
import random

print 'random.uniform(10,20)'           #�����Χ�ڵ����С��
print random.uniform(10,20)      #17.749276658
print 'random.uniform(20,10)'  
print random.uniform(20,10)      #11.9747960764


print 'random.random()'              #���0-1֮������С��
print random.random()             #0.849376425391

print 'random.range(0,10,2)'                      #���ָ�������ķ�Χ��(����������)���������
print random.randrange(0,10,2)    #(0,2,4,6,8) 6

print 'random.randint(0,5)'                  #�����Χ�ڵ�����������������
print random.randint(0,5)            #3

#����������ӣ�ͬһ����������µõ������ֵ��ͬ��ͨ���ڵ����������ǰ�����������
random.seed(10)
print 'Random number with seed 10:',random.random()

random.seed(10)
print 'Random number with seed 10:',random.random()

random.seed(10)
print 'Random number with seed 10:',random.random()
result=random.randint(0,100)
print 'Guess What I Think?'
answer=input()
while(answer!=result):
    if(answer>result):
        print '%d is too big,try a small one:' % answer
        answer=input()
    if(answer<result):
        print '%d is too small,try a big one:' % answer
        answer=input()
print 'you got it,result is  %d' % result


