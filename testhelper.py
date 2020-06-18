import helper

for i in range(10):
    print(helper.randInt(100))
    print(helper.randInt(100))

    print(helper.randInt(10))

i=21
print("ru",i,  helper.findRU(i))

print(helper.isComposite(5,11))
print(helper.isComposite(3,11))
print(helper.isComposite(7,11))


for i in range(2,20):
    print("IsPrime:", i, helper.isPrime(i,64))

for i in range(2,100):
    result = helper.isPrime(i, 64)
    if(result):
        print(i)
print()

print("gcd(7,15)",helper.gcd(7,15))
print("gcd(9,15)",helper.gcd(9,15))
print("gcd(10,15)",helper.gcd(10,15))
print("gcd(11,15)",helper.gcd(11,15))
print()


print("multInv(7,1)",helper.multInv(7,11))
print("multInv(1,11)",helper.multInv(1,11))
print("multInv(3,11)",helper.multInv(3,11))
print("multInv(8,11)",helper.multInv(8,11))
print()

print("modexp(2,7,11)",helper.modExp(2,7,11))
print("modexp(5,17,11)",helper.modExp(5,17,11))
print("modexp(8,3,11)",helper.modExp(8,3,11))
print("modexp(4,8,11)",helper.modExp(4,8,11))



print("randprime", helper.randPrime(8))
print("randprime", helper.randPrime(40))
print("randprime", helper.randPrime(8))

print("randrelprime", helper.ranRelPrime(9))
print("randrelprime", helper.ranRelPrime(8))
print("randrelprime", helper.ranRelPrime(40))


print("modexp(4,8,11)",helper.modExp(2,3,15))
print("modexp(4,8,11)",helper.modExp(8,3,15))
