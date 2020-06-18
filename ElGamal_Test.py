from ElGamal import keyGen, enc, dec
from helper import randEl, randQuadRes
(pk,sk,p,q,g) = keyGen(20)

print(sk,pk)
m = randQuadRes(p)
print()
print(m)
c=enc(pk,m,p,q,g)
print(c)
print(dec(sk,c, p,q,g))



