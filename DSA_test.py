from DSA import keyGen, sign, verify

#!!!! Nicht korrekt implementiert!


(pk,sk,p,q,g) = keyGen(8)

m = 21
print(m)

s = sign(sk,m,p,g,p)
print(s)
print(verify(pk,m,s,p,q,g))