def puissance(a, b):
#	a = input ("choisissez un premier argument:")
#	a = float (a)

#	b = input ("choissisez un deuxième argument:")
#	b = float(b)
	if not type(a) is int:
		raise TypeError("Only integers are allowed")
	if not type(b) is int:
		raise TypeError("Only integers are allowed")
	result = a**b
	return result	
#	print(f"le resultat est {result}")

#puissance(a, b)
