# =============================================================================
# 
# Veri yapıları
# Data types
# 
# #Listeler
# *değiştirilebilir
# *sıralıdır
# *kapsayıcıdır(farklı tiplerde veri tutabilir.)
# 
# ## iki yol var liste oluşturmak için [] ve list() 
# 
# list bir üst tiptir, içinde her türden veri tipi tutabilir.
# =============================================================================

# notlar = [90,80,70,50]
# type(notlar)


# liste= ['a',19,12.3]
# type(liste)
# =============================================================================
# liste içi type sorgulama

# listeleri birleştirmek için : 
# =============================================================================

# type(liste[0])
# type(liste[3])
# type(liste[2])
# type(liste[1])

# =============================================================================
# genisListe = [notlar,liste]
# genisListe
# 
# #del genisListe
# =============================================================================

#Liste eleman işlemleri
# =============================================================================
# 
# liste= [10,20,30,40,50,60]
# 
# liste[5]
# 
# liste[0:3]
# 
# liste[1:3]
# 
# liste[2:3]
# 
# liste[:5] #5 e 'kadar' yani 5. index dahil değil
# 
# liste[:6] #6 ya kadar
# 
# liste[:8] ## hata vermiyor sonuna kadar yazdırıp bırakıyor.
# 
# liste[2:] ## 2 'den' sona 'kadar' yazdır 2. index dahil. ! 
# =============================================================================

yeni_liste = ['a', 10, [12,14,11.6,13]]

# yeni_liste[2]
# yeni_liste[1]
# yeni_liste[0:2]


# yeni_liste[2][2] ## alt kümeye böyle ulaşılıyor.
yeni_liste = ['a', 10, [12,14,11.6,13],8,9,'C']
yeni_liste[2][2:]
# yeni_liste[2][:2]

## Listelere eleman ekleme çıkarma
# =============================================================================
# liste= ['ali','veli', 'berkcan','ayse']
# 
# liste[1]
# 
# # liste[1]='velinin babası'
# 
# liste[1]
# 
# liste[0:3]='alinin_babası','velinin_babasi','berkcannın_babası'
# liste
# 
# #del liste[2]
# liste
# =============================================================================


# =============================================================================
# #append ve remove ile Listelere eleman ekleme ve çıkarma
# 
# liste = ['ali','veli','ayse']
# 
# dir(liste)
# 
# liste.append('berkcan')
# liste
# 
# liste.remove('berkcan')
# liste
# 
# =============================================================================
# =============================================================================
# 
# ## insert, indekse göre eleman ekleme
# liste= ['ali','veli','isik']
# liste.insert(0, 'ayşe')
# liste
# liste.insert(2, 'mahmut')
# liste
# 
# len(liste)
# 
# liste.insert(len(liste), 'onder')
# 
# =============================================================================
## count

# =============================================================================
# liste=['ali','veli','isik','ali','veli']
# 
# liste.count('ali')
# liste.count('isik')
# 
# #copy
# liste_yedek= liste.copy()
# liste_yedek
# 
# #extend
# liste.extend(['a','b',10])
# liste
# 
# #index()
# liste.index(10)
# 
# #reverse()
# liste.reverse()
# liste
# 
# # sort()
# liste.remove(10)
# liste.sort()
# liste
# #clear()
# liste.clear()
# liste
# =============================================================================

#Tuple oluşturma  
# =============================================================================
# tuple : kapsayıcıdır, sıralıdır,!! değiştirilemez!!!
#
# =============================================================================

# =============================================================================
# t= ('ali','veli',1,2,3, 45.4, [1,45,65,78])
# t
# dir(t)
# 
# tup= 'ali','veli',1,2,3, 45.4, [1,45,65,78]
# ## paranteze gerek yok yani tupleda
# type(tup)
# type(t)
# 
# tup
# t
# ## tuple()
# t= ('eleman',)
# type(t) ## tek elemanlı tuple oluştururken değişkenin sonuna virgül atman lazım
# 
# =============================================================================
# =============================================================================
# 
# # Tuple eleman işlemleri
# 
# t= ('ali','veli',1,2,3, [2,5,8,6.4])
# t
# 
# t[1]
# t[0:3]
# ## t[2]=99 ## tuple değiştirilemez!!
# 
# =============================================================================

# =============================================================================
## Sözlükler dict
# kapsayıcı
# sırasız
# değiştirilebilir
# 
# =============================================================================
# =============================================================================
#   creating dict
# sozluk={'REG':'Regresyon Modeli',
#         'LOJ' : 'Lojistik Regresyon',
#         'CART': 'Classification and Reg'}
# 
# sozluk
# len(sozluk)
# 
# sozluk['REG'] + sozluk['LOJ']
# 
# sozluk={'REG':['Regresyon Modeli',12],
#         'LOJ' : ['Lojistik Regresyon',15],
#         'CART': [15,'Classification and Reg']}
# 
# sozluk
# len(sozluk)
# 
# =============================================================================
## Sözlük Eleman seçme işlemleri
# =============================================================================
# sozluk={'REG':'Regresyon Modeli',
#         'LOJ' : 'Lojistik Regresyon',
#         'CART': 'Classification and Reg'}
# 
# sozluk[0] ## key error verecek
# sozluk['REG']
# 
# sozluk={'REG': {'Regresyon Modeli':12,
#                 'MSE': 20,
#                 'yuca': 11}, 
#          'LOJ' : ['Lojistik Regresyon',15],
#          'CART': [15,'Classification and Reg']}
# 
# sozluk['REG']
# 
# sozluk
# 
# =============================================================================
## Dict eleman ekleme degistirme

# sozluk={'REG': {'Regresyon Modeli':12,
#                  'MSE': 20,
#                  'yuca': 11}, 
#           'LOJ' : ['Lojistik Regresyon',15],
#           'CART': [15,'Classification and Reg']}

# dir(sozluk)

# sozluk['GBM']= 'Gradient Boosting Mac'
# sozluk
# sozluk[1]='Yapay Sinir Ağları' # 1 Key değer oldu
# sozluk

# l= [2]
# sozluk[l] = 'something new' # sozluklerde ki keyler sabit veri yapıları ile yapılabilir. Yani string ve int sabit yapılardır.
# #keyler list olamaz, keyler hashable tiplerle yapılabilir.

# t =('tuple',)
# sozluk[t]='try this'
# sozluk

# =============================================================================
# ## Veri Yapısı-Set Kümeler
# Sırasızdır
# Değerler eşsizdir
# Değiştirilebilirdir.
# =============================================================================

# =============================================================================
# #Set oluşturma
# 
# liste=[1,2,4,'ali','ahmet','can',123,1.5,'ali']
# s=set(liste)
# s
# 
# t=('a','ali','a')
# s=set(t)
# s
# 
# ali='ali ata bakma uzaya git'
# s=set(ali)
# s
# 
# len(s)
# #setler hızlı ve performanslıdır.
# 
# ## setler index işlemini desteklemez çünkü SIRASIZDIR
# 
# =============================================================================

# =============================================================================
# #Setlerde eleman ekleme çıkarma
 l= ['Gelecegi','yazanlar']
# 
 s=set(l)
# dir(s)
# 
# s.add('ile')
# s
# s.add('gelecege git')
# s
# 
  s.pop()
  s
# s
# s.remove('ile')
# s
# s.add('yeni bir eleman')
# s.discard('yeni bir elema') ## bulamazsa hata üretmez.
# s
# 
# =============================================================================

# =============================================================================
# difference() her iki kumenin farkını ya da '-' ifadesi ile
# intersection() iki küme kesişimi ya da & ifadesi 
# union() iki kumenin birleşimi
# symmetric_difference() ikisinde de olmayanlar
# =============================================================================

#difference
set1= set([1,3,5])
set2= set([1,2,6])

set1.difference(set2)

set1.symmetric_difference(set2)
set1-set2
set2-set1
#intersection ve union
set1= set([1,3,5])
set2= set([1,2,6])
set1.intersection(set2)
set2.intersection(set1)

set1 & set2

set1.union(set2)
set2.union(set1)

#intersection_update kesişimi işlem yapılan sete update eder.
set1.intersection_update(set2)
set1

# Setlerde Sorgu işlemi
set1 = set([7,8,9])
set2=  set([5,6,7,8,9,10])

## iki kümenin kesişimi boş mu değil mi

set1.isdisjoint(set2)

## alt kümesi mi değil mi
set1.issubset(set2)

#kapsıyor mu kapsamıyor mu
set2.issubset(set1)
l = ['a','b',12]
l.append('D')
l
t= ('a','b',10)
t[0] = 1
t[1]
