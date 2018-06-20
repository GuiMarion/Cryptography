from sympy import *
from random import *
from Euclide import *
import time


class RSA:

	def KeyGen(self):

		p = randprime(2**(500-1), 2**(500)-1)
		q = randprime(2**(4500-1), 2**(4500)-1)

		while (not isprime(p)):
			p = randprime(2**(500-1), 2**(500)-1)

		while (not isprime(q)):
			q = randprime(2**(4500-1), 2**(4500)-1)


		Phi = (p-1)*(q-1)

		N = p*q

		e = randint(20, 100)

		# The primality with p-1 should be unecessery but for some reasons 
		# if we don't check it the computation of the modinv of e, p-1 fails
		while (Euclide(e, Phi)[0] != 1 or Euclide(e, p-1)[0] != 1):
			e = randint(20, 100)

		d = Euclide(e, Phi)[1]
		while d < 0:
			d += Phi

		dp = Euclide(d, p-1)[1]
		while d < 0:
			dp += p-1

		PublicKey = (e, N)
		PrivateKey = (d, N, dp, p)
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

		if M > (2**300)-1:
			raise ValueError("Message too big to be coded with this algorithm.")

		return self.ExpBinMod(M, e, N)


	def Decrypt(self, C, PrivateKey):

		(d, N, dp, p) = PrivateKey

		M = self.ExpBinMod(C, dp, p)

		return M

	def ModInv(self,a,m):

		(pgcd, u0,_) = Euclide(a,m)

		if pgcd != 1 :

			raise ValueError("Unable to compute the ModInv bacause the gcd is not 1")


		if u0 < 0 : 
			return u0 + m
		return u0



def Test(M, string = False):

	R = RSA()
	(PublicKey, PrivateKey) = R.KeyGen()

	print("PublicKey:", PublicKey,"PrivateKey:", PrivateKey)

	Crypt = R.Encrypt(M, PublicKey)
	print("Encrypted message:", Crypt)

	start_time = time.time()
	Decrypt = R.Decrypt(Crypt, PrivateKey)
	print("Naive : --- %s seconds ---" % (time.time() - start_time))

	if string == False:
		print("Decrypted message:", Decrypt)
	else : 
		print("Decrypted message:", IntToString(Decrypt))

	return Decrypt


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

def LookingForBugs(epochs):
	bugs = 0
	for i in range(epochs):
		try :
			M = randint(1, 2**256-1)
			D = Test(2048, M)

		except ValueError:
			bugs += 1

		if M != D :
			bugs += 1
	print("Il y a eu", bugs, "bugs dans l'execution.")



if __name__ == "__main__":

	#LookingForBugs(1000)

	if len(sys.argv) == 2:
		try :
			Test(int(sys.argv[1]))

		except ValueError:
			Test(int(sys.argv[1]), string = True)
	else:
		print("Usage: Python3 RSA2.py <Message to encrypt>")



