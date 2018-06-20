import sys
from sympy import *


# Recursive Euclide, but not efficient with large numbers
# def Euclide(a,b):

# 	return Euclide1(a, 1, 0, b, 0, 1)

# def Euclide1(a, u0, v0, b, u1, v1):
# 	# return (x1, x2, x3)
# 	# With a PGCD(a,b)
# 	# x2 first bezout coef
# 	# x3 second bezout coef
# 	if b == 0:
# 		return (a, u0, v0)
# 	else:
# 		q = int(a/b)
# 		return (Euclide1(b, u1, v1, a -q*b, u0 - q*u1, v0 - q*v1)) 


def Euclide(a, b):
	# return (x1, x2, x3)
	# With x1 PGCD(a,b)
	# x2 first bezout coef
	# x3 second bezout coef

	(a, u0, v0, b, u1, v1) = (a, 1, 0, b, 0, 1)

	while b != 0:
		(a_pred, u0_pred, v0_pred, b_pred, u1_pred, v1_pred) = (a, u0, v0, b, u1, v1)
		q = int(a // b)
		a = b_pred
		u0 = u1_pred
		v0 = v1_pred
		b = a_pred - q*b_pred
		u1 = u0_pred - q*u1_pred
		v1 = v0_pred - q*v1_pred

	return (a, u0, v0)




if __name__ == "__main__":

    if len(sys.argv) == 3:
        print(Euclide(int(sys.argv[1]), int(sys.argv[2])))
    else:
        print("Usage: Python3 Euclide.py a b")
