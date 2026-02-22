try:
    palabra = str(input("Introduce una palabra para poder comprobar si es un palíndromo: "))

    # Para evitar mayusculas y espacios de más
    palabraCorrecta = palabra.lower().replace(" ", "")

    palabraInvertida = ""

    for letra in palabraCorrecta:
        palabraInvertida = letra + palabraInvertida

    if palabraCorrecta == palabraInvertida:
        print("La palabra introducida es un palíndromo.")
    else: 
        print("La palabra introducida no es palindromo.")
except ValueError:
    print("Error: no has introducido una palabra")