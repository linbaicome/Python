# -*- coding: cp936 -*-
dic={'ը����':'��ʦ','����':'��ʦ','�°���':'ADC','äɮ':'��Ұ'}
print '����ֵ����ݣ�'
for hero in dic:
    print hero+': '+dic[hero]
print r'����ֵ��Ա�����ӣ���Ұ'
dic['����']="��Ұ"
print '����ֵ����ݣ�'
for hero in dic:
    print hero+': '+dic[hero]   
print r'ɾ���ֵ��Ա��äɮ����Ұ'
del dic['äɮ']
print '����ֵ����ݣ�'
for hero in dic:
    print hero+': '+dic[hero]
