from helper import randInt, modExp, getRandSafePrime, findGenSubGroup, multInv, randRelPrime

#!!!! Nicht korrekt implementiert!

def keyGen(k):
    (p,q) = getRandSafePrime(k)
    g = findGenSubGroup(p,q)
    #sk is element of Zq
    sk = randInt(q-1)
    #pk is element of Gq
    pk = modExp(g,sk, p)
    return (pk,sk, p, q, g)

def sign(sk,m,p,g,q):
    r = randRelPrime(q)
    s1 = modExp(g,r,p) % q

    rI = multInv(r,q)
    s2 = rI*(m+sk*s1) % q
    return (s1,s2)

def verify(pk,m,s,p,q,g):
    (s1,s2) = s
    s2I = multInv(s2,q)

    pks1 = modExp(pk,s1,p)
    gm = modExp(g,m,p)

    s1N = modExp(gm*pks1,s2I,p) % q

    if(s1 == s1N):
        return 1
    else:
        return 0