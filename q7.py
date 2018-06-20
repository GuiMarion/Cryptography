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

def GloutonOptimal(liste,s):
	i = len(liste)-1
	liste2 = []
	for elem in liste :
		liste2.append(0)
	while(i >= 0):
		if(liste[i]<=s):
			s = s-liste[i]
			liste2[i] = 1
		else:
			liste2[i] = 0
		i = i-1 
	return liste2


def DechiffrementMerkle(b,c,v):
	return GloutonOptimal(b,c/v)

liste = [1,2,4,8,16,32,64,128,256,512]
s = 3

#print(GloutonOptimal(liste,s))
v = 1
u = 600
for i in range(u):
	if Euclide(u,i) == 1:
		v = i
		break


a = []

for elem in liste :
	a.append(elem * v)

m = [0,1,0,1,0,1,0,1,0,1]

c = 0

for i in range(len(m)):
	c += m[i]*a[i]



print(DechiffrementMerkle(liste, c, v))				
