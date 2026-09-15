import fonctions as f

def carre():
	while True:
#		x = input("saisissez un nombre sur votre clavier:")
#		x = float(x)
#		result1 = x ** 2
#		print (f"le resultat est {result}")
		a = int(input("choisissez un premier argument:"))
		b = int(input("choissisez un deuxième argument:"))
		res = f.puissance(a, b)

		print (f"le résultat est {res}")

carre()
