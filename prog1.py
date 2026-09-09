import fonctions as f

def carre():
	while True:
#		x = input("saisissez un nombre sur votre clavier:")
#		x = float(x)
#		result1 = x ** 2
#		print (f"le resultat est {result}")
		a = input ("choisissez un premier argument:")
		a = int (a)

		b = input ("choissisez un deuxième argument:")
		b = int (b)

		res = f.puissance(a, b)

		print (f"le résultat est {res}")

carre()	
	
