# -*- coding: cp936 -*-
sentence=raw_input('����һ�λ���')
print 'ʹ��Split()���зָ�'
liststr=sentence.split()
for s in liststr:
    print s
print 'ʹ��join���ӣ������ַ�Ϊ��-��'
s='-'
print s.join(liststr)
