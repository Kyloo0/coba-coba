x = 1
while x <= 100:
    if x == 98:
        break
    print(x)
    x += 1

var = [0 for i in range (5)]
print (var)


evenNumber = [0,1]

for j in range (0,501,2):
  evenNumber.append(j)
  
print (evenNumber)

import re
pola= '^a...s$'
string_tes= 'abyss'
hasil= re.match(pola, string_tes)
 
if hasil:
    print("Pencarian berhasil.")
else:
    print("Pencarian gagal.") 



import pandas as pd
data = {
  'Nama' :  ['John','Fitto','Alfa'],
  'Usia' : [22,21,30],
}

df = pd.DataFrame(data)

print(df)

i = 11 
if i<10:    
    print(i) 
else:    
    print("Nilai yang dimasukkan tidak boleh lebih besar dari 10") 



import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
result = matriks * 2
print(result)
print(matriks)


a =0
a+=1
matriks = [[a for j in range(5)] for i in range(5)]
print(matriks)
print(matriks[2][2])

def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info
 
print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))


def greeting(name):
    print("Halo " + name + ", Selamat Datang!")
 
greeting("Dicoding Indonesia")


import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
result = matriks * 2
print(result)
print(matriks)
