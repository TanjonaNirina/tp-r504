def puissance(a, b):
    if not type(a) is int:
        raise TypeError("Only integers are allowed")
    if not type(b) is int:
        raise TypeError("Only integers are allowed")
    if a == 0 and b <= 0:
        raise ValueError("l'exposant doit être strictement positif")

    result = 1
    # iteration de la valeur absolue de l'exposant
    nb_iterations = -b if b < 0 else b

    for _ in range(nb_iterations):
        result *= a

    # si exposant négatif, on prend l'inverse
    if b < 0:
        result = 1 / result

    return result
