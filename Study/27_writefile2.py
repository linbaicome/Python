# -*- coding: cp936 -*-
filename=raw_input('������Ҫ������ļ���.txt\n')
data=raw_input('������Ҫ��������ݣ�\n')
f=open(filename,'w')
f.write(data)
f.close()
f2=open(filename)
data2=f2.read()
print '����������ǣ�\n'
print data2
f2.close()
