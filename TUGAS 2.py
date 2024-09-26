# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:52:50 2024

@author: Muysaa'z'
"""

#NESTED FOR LOOP

x = [1,2,3]
y = [4,5,6]
    
for a in x:
    for b in y:
        print(a,b)



#SORTED KECIL KE BESAR

x = [20, 7, 11, 3, 1, 17, 8]
x.sort()
print(x)
x.sort(reverse=True)
print(x)



# MENEMUKAN UKURAN ANGKA 11 DENGAN COMMAND INDEX

x = [20, 7, 11, 3, 1, 17, 8]
result = x.index(11)
print(result)


#GABUNGAN 2 List Menjadi 1 Directory

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))
print(result)


#GABUNGAN 2 DIRECTORY MENJADI 1 DIRECTORY

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

result = {**dict1,**dict2}
print(result)



#MENGEKTRAKSI KATA KUNCI

sample_dict = { "name": "Kelly",
                "age": 25,
                "salary": 8000,
                "city": "New york"}


keys = ["name", "salary"]

result = {k: sample_dict[k] for k in keys}
print(result)


#CALCULATE PANJANG X LEBAR


def calculate_area(panjang, lebar):
    luas = panjang * lebar
    return luas

print(calculate_area(5,10))






























