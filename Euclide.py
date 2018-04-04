import sys


def Euclide1(a, u0, v0, b, u1, v1):
	# return (x1, x2, x3)
	# With a PGCD(a,b)
	# x2 first bezout coef
	# x3 second bezout coef
	if b == 0:
		return (a, u0, v0)
	else:
		q = int(a/b)
		return (Euclide1(b, u1, v1, a -q*b, u0 - q*u1, v0 - q*v1)) 


def Euclide(a,b):
	return Euclide1(a, 1, 0, b, 0, 1)




if __name__ == "__main__":

    if len(sys.argv) == 3:
        print(Euclide(int(sys.argv[1]), int(sys.argv[2])))
    else:
        print("Usage: Python3 Euclide.py a b")
