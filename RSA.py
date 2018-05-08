from sympy import *
from random import *
from Euclide import *
import time


class RSA:

	def __init__(self):

		self.dp = None
		self.dq = None
		self.qinv = None
		self.p = None
		self.q = None


	def KeyGen(self, lambd):
		lambd = int(lambd/2)
		rangePrime = [2**(lambd-1), 2**(lambd)-1]
		#print(rangePrime)
		p = randprime(rangePrime[0], rangePrime[1])
		q = randprime(rangePrime[0], rangePrime[1])

		while (not isprime(p)):
			p = randprime(rangePrime[0], rangePrime[1])

		while (not isprime(q)):
			q = randprime(rangePrime[0], rangePrime[1])


		Phi = (p-1)*(q-1)

		N = p*q

		e = randint(1, Phi)

		# The primality with p-1 should be unecessery but for some reasons 
		# if we don't check it the computation of the modinv of e, p-1 fails
		while (Euclide(e, Phi)[0] != 1 or Euclide(e, p-1)[0] != 1):
			e = randint(1, Phi)

		d = Euclide(e, Phi)[1]
		while d < 0:
			d += Phi

		self.dp = self.ModInv(e, p-1)
		self.dq = self.ModInv(e, q-1)
		self.qinv = self.ModInv(q, p)
		self.p = p 
		self.q = q

		PublicKey = (e, N)
		PrivateKey = (d, N)
		return (PublicKey, PrivateKey)

	def ExpBinMod(self, m,e,N):

		e = list("{0:b}".format(e))
		t = len(e)
		b = 1
		for i in range(t):
			b = (b**2) % N
			if (e[i] == '1'):
				b = (b * m) % N

		return b


	def Encrypt(self, M, PublicKey):

		(e, N) = PublicKey
		#c = Pow(M, e) % N

		return self.ExpBinMod(M, e, N)


	def Decrypt(self, C, PrivateKey):

		(d, N) = PrivateKey

		return self.ExpBinMod(C, d, N)

	def ModInv(self,a,m):

		(pgcd, u0,_) = Euclide(a,m)

		if pgcd != 1 :

			raise ValueError("Unable to compute the ModInv bacause the gcd is not 1")


		if u0 < 0 : 
			return u0 + m
		return u0



	def CRT(self,a,m):
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
			yi= self.ModInv(Mi,m[i])
			result = result + a[i]*Mi*yi % M
		return result % M

	def Decrypt_CRT(self, C):

		m1 = self.ExpBinMod(C, self.dp, self.p)
		m2 = self.ExpBinMod(C, self.dq, self.q)
		h = (self.qinv * (m1 - m2)) % self.p 
		m = m2 + h * self.q

		return m



def Test(lambd, M, string = False):

	R = RSA()
	(PublicKey, PrivateKey) = R.KeyGen(lambd)

	print("PublicKey:", PublicKey,"PrivateKey:", PrivateKey)

	Crypt = R.Encrypt(M, PublicKey)
	print("Encrypted message:", Crypt)

	start_time = time.time()
	Decrypt = R.Decrypt(Crypt, PrivateKey)
	print("Naive : --- %s seconds ---" % (time.time() - start_time))

	start_time = time.time()
	Decrypt2 = R.Decrypt_CRT(Crypt)
	print("CRT : --- %s seconds ---" % (time.time() - start_time))

	if string == False:
		print("Decrypted message:", Decrypt)
	else : 
		print("Decrypted message:", IntToString(Decrypt))

	if string == False:
		print("Decrypted message with CRT:", Decrypt2)
	else : 
		print("Decrypted message with CRT:", IntToString(Decrypt2))


	#print(R.CRT([3,4,5],[17,11,6]))

def StringToInt(M):
	S = ""
	for elem in M:
		S += str(ord(elem)-25)
	return (S)

def IntToString(M):
	M = str(M)
	chunks, chunk_size = len(M), 2
	return  "".join([ chr(int(M[i:i+chunk_size])+25) for i in range(0, chunks, chunk_size) ])

if __name__ == "__main__":

	if len(sys.argv) == 3:
		try :
			Test(int(sys.argv[1]), int(sys.argv[2]))

		except ValueError:
			Test(int(sys.argv[1]), int(StringToInt(sys.argv[2])), string = True)
	else:
		print("Usage: Python3 RSA.py <lambda> <Message to encrypt>")



