import functools
s=input("szam: ")
alap=int(input("szamrendszerbol: "))
cel=int(input("szamrendszerbe: "))
szamjegyek="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#ez lehetne egy sima szam=int(s,alap)
szam=functools.reduce(
  lambda osszeg,szamjegy: osszeg*alap+szamjegyek.find(szamjegy.upper()),
  s,0)
print("Tizes szamrendszerben: "+str(szam))
if szam==0:
    print(szam)
else:
  l=[]
  while szam>0:
   szam,maradek=divmod(szam,cel)
   l.append(szamjegyek[maradek])
  print("".join(l[::-1]))

