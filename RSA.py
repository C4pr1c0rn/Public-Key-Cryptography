from helper import randPrime, ranRelPrime, multInv, modExp

def keyGen(k):
    p=0
    q=0
    while(p == q):
        p = randPrime(int(k/2))
        q = randPrime(int(k/2))
    print("Found Prime p ",p)
    print("Found Prime q ",q)
    
    n = p*q
    print("Calculate n ", n)

    order = (p-1) * (q-1)
    print("Calculate order ", order)

    e = ranRelPrime(order)
    print("Calculate public key value e ", e)

    d = multInv(e, order)
    print("Calculate private key value d ", d)

    pk = (n,e)
    sk = (n,d)
    return (pk,sk)

def enc(m, pk):
    (n,e) = pk
    return modExp(m,e,n)

def dec(c, sk):
    (n,d) = sk
    return modExp(c,d,n)
    
def sign(sk,m):
    (n,d) = sk
    s = modExp(m,d,n)
    return s

def verify(pk,m,s):
    (n,e) = pk
    ms = modExp(s,e,n)
    if(ms==m):
        return 1
    else:
        return 0