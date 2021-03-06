from helper import randInt, modExp, getRandSafePrime, findGenSubGroup, multInv

def keyGen(k):
    (p,q) = getRandSafePrime(k)
    g = findGenSubGroup(p,q)
    #sk is element of Zq
    sk = randInt(q-1)
    #pk is element of Gq
    pk = modExp(g,sk, p)
    return (pk,sk, p, q, g)

def enc(pk, m, p, q, g):
    r = randInt(q-1)
    print("R",r)
    c = (modExp(g,r,p), m*modExp(pk,r,p) %p)
    return c

def dec(sk, c, p, q, g):
    (a,b) = c
    s = modExp(a,sk,p)
    m = (b*multInv(s,p)) % p
    #m = b*(modExp(a,multInv(sk,p),p)) % p
    return m