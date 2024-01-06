## Sınıflara giriş ve sınıfları tanımlamak.

#sınıf nedir, benzer özlekkileri, ortak amaçlar taşıyan , metod ve değişkenleri barındıran.

## Sınıf Özellikleri Class attributes
##
# =============================================================================
class Veribilimci():
    bolum=''
    sql='Evet'
    deneyim_yili= 0
    bildigi_diller=[]
#     
# =============================================================================
## sınıfların özelliklerine erişilebilir ve değiştirilebilir.
Veribilimci.bolum
Veribilimci.sql= 'hayir'

##sınıf örneklendirmesi (instantiation)

ali= Veribilimci()
ali.sql

ali.bildigi_diller.append('python')
ali.bildigi_diller


veli= Veribilimci()
veli.bildigi_diller

## örnek özellikleri kavramı ile gidirebiliriz bu durumu.

class Veribilimci():
    bildigi_diller= ['PYTHON','R']
    bolum=''
    sql='Evet'
    deneyim_yili= 0

    def __init__(self):
        self.bildigi_diller= []
        
ali= Veribilimci()
ali.bildigi_diller= ['python']
ali.bildigi_diller


veli= Veribilimci()
veli.bildigi_diller
Veribilimci

### Örnek Metodları.
## örneklerin üzerinde çalışan fonksiyonlar
class Veribilimci():
    calisanlar = []

    def __init__(self):
        self.bildigi_diller= []
        self.bolum=''
    
    def dil_ekle(self,yeni_dil,yeni_bolum):
        self.bildigi_diller.append(yeni_dil)
        self.bolum = yeni_bolum
        
ali= Veribilimci()
ali.bildigi_diller
ali.bolum
ali.dil_ekle('pythonl', 'yazılım müh')
ali.bildigi_diller
ali.dil_ekle('','asdasd')
ali.bolum

veli= Veribilimci()
veli.bildigi_diller
veli.bolum

dir(Veribilimci)

Veribilimci.dil_ekle

# Miras yapıları İnheritance
class Emploiees():
    
    def __init__(self):
        self.FirstName= ''
        self.LastName= ''
        self.AdressName= ''

class DataScience(Emploiees):
    def __init__(self):
        self.Progrraming= ''

veribilimci1= DataScience()
veribilimci1.Progrraming
veribilimci1
        
class Marketing(Emploiees):
    def __init__(self):
        self.StoryTelling= ''
 
### daha optimize şekilde güzel bir tanım
class Emploiees_new():
    
    def __init__(self,FirstName,LastName,Adress):
        self.FirstName= FirstName
        self.LastName= LastName
        self.Adress= Adress

ali= Emploiees_new('FirstName', 'LastName', 'Adress')
ali.FirstName
ali.LastName    

## Fonksiyonel Programlama
#fonksiyonlar dilin bastacıdır :D
# Birinci sinif nesnelerdir
# yan etkisiz fonksiyonlar (statetless, girdi-çıktı)
# Yuksek seviye fonksiyonlar
# Vektorel Operasyonlar.

## yan etkisiz fonksiyonlar (Pure Function)

A = 5

def impure_sum(b):
    return b+A

def pure_sum(a,b):
    return a+b 

impure_sum(6)
A = 9
impure_sum(6) ## dışardan etkilenebiliyor yani. sonuç 11'den 15 e çıktı.

pure_sum(3,3.4) ## bunun sonucu her zaman sabit kalacak
# dışarıdan etki yapılamayacak
# o yüzden yan etki yoktur yani pure fonksiyondur
#bağımsız yani.

### Ölümcül yan etkiler

class LineCounter:
    def __init__(self,filename):
        self.file = open(filename,'r')
        self.lines = []
        
    def read(self):
        self.lines= [line for line in self.file]

    def count(self):
        return len(self.lines)
    
    
lc= LineCounter('deneme.txt')

print(lc.lines) 
print(lc.count())

lc.read()
print(lc.lines)
print(lc.count())
# bir fonksiyonu çalıştırdktan sonra her şey değişti.


### fonkisyonel programlama ile 
def read(filename):
    with open(filename,'r') as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)

def lin(lines):
    return lines

example_lines= read('deneme.txt')
lines_count= count(example_lines)
lines_count
linese= lin(example_lines)
linese

## İsimsiz Fonksiyonlar (Anonymous functions) lambda mükkemmel bişiy.

def old_sum(a,b):
    return a+b

old_sum(3, 2)

new_sum = lambda a,b: a+b       
new_sum(4,5) 

sirasiz_liste= [('b',3), ('a',8), ('d',12),('c',1)]
sirasiz_liste

sorted(sirasiz_liste, key= lambda x: x[0]) 
# =============================================================================

### Vektorel Operasyonlar
# =============================================================================

### Object Orriented Progrraming
a= [1,2,3,4,5]
b= [2,3,4,5,6]

ab= []

for i in range(0,len(a)):
    ab.append(a[i]*b[i])

ab
# =============================================================================#
## functional Progrraming
import numpy as np


a= np.array([1,2,3,4,5])
b=np.array([2,3,4,5,6])

ab= a*b
ab

# =============================================================================
### Map Filter ve Reduce Fonksiyonları

liste= [1,2,3,4,5,6]

for i in liste:
    print(i+10)

list(map(lambda x: x+10, liste))
#map fonksiyonu verilen bir vektörün/objenin
#içerisinde bir fonksiyonu çalıştırmaya izin verir."


# filter(function, iterable)

liste= [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x : x%2 ==0, liste))
## değiştirmiyor ancak döndürüyor.

## reduce
from functools import reduce

liste= [1,2,3,4]
reduce(lambda a,b : a-b, liste)
# indirgeme işlemi yapıyor 

# =============================================================================
#Modül Oluşturmak
# =============================================================================
# =============================================================================

## Hatalar istisnalar (exceptions)
# =============================================================================
# 
# programcı hataları
# program hataları (bug)
# exceptions istisna hataları 
# =============================================================================

a=10
b=0
a/b
#ZeroDivisionError hatasi
try:
    print(a/b)
except ZeroDivisionError:
    print('paydada sıfır olmas')

#tip hatasi
a=10
b='2'

a/b

try:
    print(a/b)
except TypeError:
    print('sayılar sayılar ile çarpılır')

# =============================================================================
# ## bölüm sonu değerlendirmesi
# python giriş
# çalışma ortamı ayarladık
# temel hareketler
# veri yapıları
# Fonksiyon ve Fonksiyon okuryazarlığı
# kontrol karar yapıları
# döngüler
# Nesne yönelimli programlama temeli
# Fonksiyonel programlama
# Modüller
# hata yönetimi
# 
# 
# =============================================================================


from functools import reduce
A = ["Veri","Bilimi","Okulu"]
reduce(lambda a,b: a+b, list(map(lambda x: x[0], A)))

list(map(lambda x: x[0], A))
A
from functools import reduce
reduce(lambda a,b: a+b, ["a","4","a"])

A = [1,2,3,4,5]

if type(A) == ():
    print("islem gecersiz")
else:
    print(list(map(lambda x: x/1, A)))
    
    
list(map(lambda x: x.capitalize(), ["abc","bcd","cde"]))




A = []
for i in ["ali","veli","isik"]:
    A.append(i.replace("i","a"))
print(A)


