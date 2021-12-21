# RSA Alogrithm 
# Created by Mohamed Zidan
# 12/21/2021 
# Using RSA with 1024-bit primes p and q and a public exponent e = 65537  to encrypt the message m = 466921883457309

!apt install libmpc-dev
!pip install gmpy2
!pip install tinyec
from fractions import gcd
from sympy.ntheory.residue_ntheory import primitive_root
import random
import sys
import random
import timeit
import gmpy2
from tinyec import registry
import secrets
import time
import timeit
import gmpy2

# Function to Generate Prim number
def genprimeBits(k):
    x = ""
    k = int(k)
    for y in range(k):
        x = x + "1"
    y = "1"
    for z in range(k-1):
        y = y + "0"
    # print(x)
    # print(y)
    x = int(x,2)
    y = int(y,2)
    p = 0
    while True:
        p = random.randrange(y,x)
        if  Miller_rabin(p,10):
            break
    return p


# Function for Miller Test
def Miller_rabin(n, t):
  # Test if the number is even
    if n % 2 == 0:
        return False
    #Find k,q with ,k>0, q odd sif n-1=(2^k)*q
    k=0
    q=n-1
    while q % 2 == 0:
        k += 1
        q //= 2   
  # now we got values of k and q(odd number) which sitisfied n-1=(2^k)*q
    # print(f'k= {k}')
    # print(f'q= {q}')
    for _ in range(t):
        a = random.randrange(2, n - 1)
        x = pow(a,q,n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(k - 1):
            x = pow(x,2,n)
            if x == n-1:
                break 
        else:
            return False
    return True

  
  
# Function to find multiplicative inverse 
import random
import sys
sys.float_info.max
def inv(a,n):
  i=0
  n_=n
  while(i!=1):
    if(((n_+1)%a)==0):
      d=(n_+1)//a
      if((d*a)%n == 1):
        return int(d)
    else:
      n_+=n
  
  
  
message = 466921883457309
e = 65537
p=genprimeBits(1024)
print(f'p={p}')

q=genprimeBits(1024)
print(f'q={q}')

n=p*q
print(f'n={n}')

phi=(p-1)*(q-1)
print(f'φ(n)={phi}')

print(f'Message= {message}')
Cipher=(m**e)%n
print(f'Ciphertext= {Cipher}')


# Tradational decryption  and compute the comsuming time 
starttime = timeit.default_timer()
print("The start time is :",starttime)
m_=pow(Cipher,d,n)
print("Computational time without CRT :", timeit.default_timer() - starttime)
print(f'Message= {m_}')
