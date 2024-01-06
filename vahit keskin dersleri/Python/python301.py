# =============================================================================
# ## Fonksiyonlara giriş ve Fonksiyon Okur Yazarlığı
# ## ctrl+I kullanmak lazım
# ## fonksiyon belirli amaçları yerine getiren işleçler.
# ?print
# ## Argüman fonksiyonların genel amaçlarını özelleştirmeye, o genel amaçları farklı şekillerde biçimendirmeye yarayan görevciler
# print('asda','asdasd', sep='+') #mesela 'sep' argümanı
# print() 
# len()
# 
# =============================================================================

##♦ Fonskiyon Yazmak, nasıl yazılır?
# =============================================================================
# 
# #Matematiksel işlemler, Operatörler
# 4*4
# 4-4
# 4+4
# 4/4
# ##power alma
# 3**2
# 3**3
# ### Fonksiyon tanımlama
# def kare_al(x):
#     x= x**2
#     print(x) 
# 
# 
# def vaht(x):
#     print("girilen sayının karesi: " + str(x**2))
#     
# vaht(16)
# 
# =============================================================================
# =============================================================================
# 
# ##iki argümanlı fonksiyon  tanımlamak
# 
# def tamkare_al(x,y):
#     temp= x**2+2*x*y+y**2    
#     print('girilen ifadelerin toplamnının tam karesi: '+ str(temp))
#     
# tamkare_al(12, 2)
# 
# ## Ön tanımlı argümanlar ile fonksiyon tanımlamak
# 
# def tamkare_al(x,y):
#     temp= x**2+2*x*y+y**2    
#     print('girilen ifadelerin  toplamının tam karesi: '+ str(temp))
# 
# tamkare_al(3) ## missing argument hatası veriyor, defaultu olan argümanlar iyi olabliyor.
#  
# def tamkare_al(x,y=1):
#     temp= x**2+2*x*y+y**2    
#     print('girilen ifadelerin toplamının tam karesi: '+ str(temp))
#     
# 
# tamkare_al(3) ## şimdi hata vermiyecek. çünkü y nin default değeri 1 dir.
# 
# tamkare_al(3,2)    
#     
# tamkare_al(y=13,x=16)
# 
# ### ne zaman fonskiyon yazılır, yazmalıyız.
# ## tekrar eden görevleri yerine getirmek ve varolan işleri daha programatik bir biçimde gerçekleştirmek için kullanılır.
# 40,25,90
# def direk_hesap(nem,isi,şarj):
#     print((isi+nem)/şarj)
# 
# direk_hesap(20, 40, 82)        
# ### fonksiyonların çıktılarını girdi olarak kullanmak.
# 
# def direk_hesap(nem,isi,şarj):
#     temp=(isi+nem)/şarj
#     return temp
# 
# cıktı= direk_hesap(20, 40, 82) 
# cıktı
# #### Local ve Global değişkenler 
# #bunlar global
# x=10
# y=15
# 
# ##fonksiyonların içindekiler local değişkenlerdir
# 
# def ustel_al(x,y):
#     return x**y
# ustel_al(10, 3)
# 
# ## local etki alanından global etki alanını değiştirmek
# x= []
# 
# def eleman_ekle(y):
#     x.append(y)
#     print(str(y)+ " ifadesi eklendi")
# 
# eleman_ekle(120)
# x
# 
# =============================================================================

#Karar kontrol yapıları

## True False - mantıksal sorgulamalar
sinir=5000

sinir==4000

sinir==5000

## if koşul yapısı
sinir=5000

if(sinir==5000):
    sinir= sinir+1
    print(sinir)
## if statetment true dönerse execute olur
else:
    sinir=sinir-1
    print (sinir)
## elif yapısı birden fazla koşul kullanmak için kullanılır.

sinir=500
gelir=400

if sinir>gelir:
    print('tebrikler')
elif sinir<gelir:
    print('Daha çok çalışmalısın')
else:
    print('tam sinirdasınız')
## mini uygulama
sinir= 50000
magza_adi=input('magza adını giriniz: ')
gelir= int(input('gelirinizi giriniz: '))

if gelir>sinir:
    print('tebrikler')
elif gelir<sinir:
    print('maalesef')
else:
    print('normal')

### Döngüler
#iteratif işlemleri uygulamaları rahatça ve sistematik şekilde uygulamaya yarar
#For

ogrenci = ['ali','veli','ahmet','yusuf','cem']


for x in ogrenci:
    print(x)
########### yüzde 20 zam
maaslar = [1000,2000,3000,1400]

def yeni_maas(x):
    print(x*0.20+x)

for i in maaslar:
    yeni_maas(i)

#############3 üst sınırlı alt sınırlı

maaslar = [1000,2000,3000,4000,5000,6000]

def maas_ust(x):
    print(x*10/100+x)


def maas_alt(x):
    print(x*20/100+x)


for i in maaslar:
    
    if i <3000:
        maas_alt(i)
    else:
        maas_ust(i)

####### break ve continue çık(break) ve bunu atla çalışmaya devam et (contnuie)

## while// olduğu sürece
sayi=1
while sayi<10:
    sayi +=1
    print (sayi)

def islem(x,y):
    print(x-y)

islem(3)

def harf_say(x):
    return len(x)
 
a= 'Merhaba'
harf_say("Merhaba!")
type(a)
harf_say(a)
def islem(x,y):
    A = [x,y]
    return A[0] + A[1]

islem(1,3) 

def islem(x):
    if (x>10):
        return "YES"
    else:
        return x*5
 
islem(4)

if [1,2,3,4][1] == 2:
    print("YES".lower())
else:
    print("NO") 
    
def islem(x, y):
    print(x + y)
 
islem(1,9)

A = []

for i in [1,2,3,4]:
    A.append(i)

A[0]



