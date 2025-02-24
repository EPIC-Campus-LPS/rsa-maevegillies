import random_num
import millerrabin
import extendedeuclidean
import math

#generates a random number by hashing an image taken by the laptop's camera
p = int(random_num.random_num(10, 2000000))
q = int(random_num.random_num(10, 2000000))

#checks to see if the number is prime. If it isn't, then it regenerates p and q and checks again
while millerrabin.is_prime(p) == False:
    p = random_num.random_num(10, 2000000)
while millerrabin.is_prime(q) == False:
    q = random_num.random_num(10, 2000000)
    print(q)

#compute n
n = p*q

#euler's toitent function
euler = (p-1)*(q-1)

#set e to a value, then check to see if it is coprime with euler's number
e = 65537

while True:
    a = math.gcd(e, euler)
    if  a==1:
        break
    else:
        e += 1

#take the modular inverse of euler's function
d = extendedeuclidean.mod_inverse(e, euler)
print(d)

#compute the public and private keys


print(f"p: {p}", f"q: {q}", f"e: {e}", f"n: {n}")
print(f"public: {e, n} ", f"private: {d, n}")