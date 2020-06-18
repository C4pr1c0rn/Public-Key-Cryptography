from RSA import keyGen, enc, dec

#(pk,sk) = keyGen(13)

#print("public key",pk)
#print("private key",sk)

#For KeyLength bigger than 55 not possible --> bigInt
(pk,sk) = keyGen(40)

print("public key",pk)
print("private key",sk)



m = 14
c = enc(m, pk)
result = dec(c,sk)

print("Encrypt message ", m)
print("Ciphertext ", c)
print("result ", result)