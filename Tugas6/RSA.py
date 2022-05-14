def isPrime(num):
    for i in range(2,num):
        if (num % i) == 0:
            prime = False
        else:
            prime = True
    return prime

def find_nearest_prime(num):
    while num < 100000:
        if isPrime(num):
            return num
        else:
            num += 1
            
def get_factors(num):
    factors = []
    for i in range(2,num):
        if ((num % i) == 0):
            factors.append(i)
    return factors

def isCoprime(num1,num2):
    num1_factors = get_factors(num1)
    num2_factors = get_factors(num2)
    if set(num1_factors).isdisjoint(set(num2_factors)):
        # print('no common factors - they coprime!')
        return True
    else:
        # print('there are common factors, not coprime')
        return False

def find_e(n,phi_n):
    candidates = []
    for i in range(3,phi_n):
        if isPrime(i):
            if((isCoprime(i,n)) and (isCoprime(i,phi_n))):
                candidates.append(i)
    return candidates[len(candidates)-1]

def find_d(prime1,n, e):
    candidates = []
    for i in range(prime1,n):
        if (((i*e) % phi_n) == 1):
            print(i)
            return i

def encrypt(pt, e, n):
    hasil = []
    for i in pt:
        hasil.append((ord(i) ** e) % n)
    return hasil

def decrypt(pt, d, n):
    hasil = ""
    for i in pt:
        a = (i ** d) % n
        # print(a)
        hasil += chr(a)
    return hasil

pt = "Aku Adalah Anak Gembala Selalu Riang Serta Gembira!"

prime1 = 31
prime2 = 37
n = prime1*prime2
phi_n = ((prime1-1)*(prime2-1))
e = find_e(n, phi_n)

# print(phi_n)
# print(e)
d = find_d(prime1, n, e)
enkripsi = encrypt(pt, e, n)
print(f'hasil enkripsi: {enkripsi}')
dekripsi = decrypt(enkripsi, d, n)
print(f'hasil dekripsi: {dekripsi}')