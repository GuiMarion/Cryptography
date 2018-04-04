from sympy import *
from random import *
from Euclide import *

class RSA:
	def KeyGen(self, lambd):
		lambd = int(lambd/2)
		rangePrime = [2**(lambd-1), 2**(lambd)-1]
		#print(rangePrime)
		p = randprime(rangePrime[0], rangePrime[1])
		q = randprime(rangePrime[0], rangePrime[1])

		N = p*q

		while (not isprime(p)):
			p = randprime(rangePrime[0], rangePrime[1])

		while (not isprime(q)):
			q = randprime(rangePrime[0], rangePrime[1])

		Phi = (p-1)*(q-1)

		e = randint(1, Phi)

		while (Euclide(e, Phi)[0] != 1):
			e = randint(1, Phi)

		d = Euclide(e, Phi)[1]
		while d < 0:
			d += Phi

		PublicKey = (e, N)
		PrivateKey = (d, N)
		return (PublicKey, PrivateKey)


	def Encrypt(self, M, PublicKey):

		(e, N) = PublicKey
		c = Pow(M, e) % N

		return c


	def Decrypt(self, C, PrivateKey):

		(d, N) = PrivateKey

		return Pow(C, d) % N


def Test(lambd, M, string = False):

	R = RSA()
	(PublicKey, PrivateKey) = R.KeyGen(lambd)

	print("PublicKey:", PublicKey,"PrivateKey:", PrivateKey)

	Crypt = R.Encrypt(M, PublicKey)
	print("Encrypted message:", Crypt)

	Decrypt = R.Decrypt(Crypt, PrivateKey)
	if string == False:
		print("Decrypted message:", Decrypt)
	else : 
		print("Decrypted message:", IntToString(Decrypt))

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



