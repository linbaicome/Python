# -*- coding: cp936 -*-
try:
    f=open('non-exist.txt')
    print 'file open'
    f.close
except:
    print 'File not exists'
print 'Done'

#���try�ڳ����쳣��ִ��except�ڵĴ���
#���try��û�г����쳣��ִ��try�ڵĴ���
#���򲻻ᱻ�жϣ����� ��Done' �ᱻ���
