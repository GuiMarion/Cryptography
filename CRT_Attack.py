from Euclide import *
import gmpy
import time


def ModInv(a,m):

	(pgcd, u0,_) = Euclide(a,m)

	if pgcd != 1 :

		raise ValueError("Unable to compute the ModInv bacause the gcd is not 1")


	if u0 < 0 : 
		return u0 + m
	return u0



def CRT(a,m):
	# a and m vector of size r
	# x = ai mod mi for all i

	M = 1

	for elem in m:
		M = M*elem

	r = len(a)
	if len(a) != len(m):
		raise ValueError("Invalid input, a and m shoud have the same size.")
	result = 0
	for i in range(r):
		Mi = int(M / m[i])
		yi= ModInv(Mi,m[i])
		result = result + a[i]*Mi*yi % M
	return result % M

def sqrtn(x, n):

	m0=gmpy.mpz(x)
	return int(m0.root(n)[0])

def Attack(N, C, e):

	M = sqrtn(CRT(C, N), e)

	return M


def ExpBinMod(m, e, N):

	e = list("{0:b}".format(e))
	t = len(e)
	b = 1
	for i in range(t):
		b = (b**2) % N
		if (e[i] == '1'):
			b = (b * m) % N

	return b

# All the public keys need to don't have common factors. 
# Plus, e can't be choose by anyone because e should be prime with Phi and p-1
# In the real life e is choosen uniformly in [1, phi(N)] such that pgcd(e, phi(N)) = 1
N = [7877, 7823, 7759]
e = 3
M = 99
C = []

for elem in N: 
	C.append(ExpBinMod(M, e, elem))


print(Attack(N, C, e))




