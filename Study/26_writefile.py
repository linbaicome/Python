# -*- coding: cp936 -*-
filename=raw_input('������Ҫ������ļ���.txt\n')
print 'DataTest�ļ��������ǣ�'
f=open('DataTest.txt')
data=f.read()
print data
f.close()
f2=open(filename,'w')
f2.write(data)
f2.close()
print '��DataTest�ļ����ݴ���Ҫ�����ļ����ļ������ǣ�\n'
f3=open(filename)
data2=f3.read()
print data2
f3.close()
