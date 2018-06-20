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

liste = [1,2,4,8,16,32,64,128,256,512]
s = 3

print(GloutonOptimal(liste,s))
				
