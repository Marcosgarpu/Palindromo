def is_palindrome(palabra):
    try:
        # Para evitar mayusculas y espacios de más
        palabraCorrecta = palabra.lower().replace(" ", "")

        palabraInvertida = ""

        for letra in palabraCorrecta:
            palabraInvertida = letra + palabraInvertida

        if palabraCorrecta == palabraInvertida:
            return True
        else:
            return False
    except ValueError:
        print("Error: no has introducido una palabra")

palabra = input("Introduce la palabra para comprobar si es un palindromo.")
if print(is_palindrome(palabra)) == True:
    print("La palabra elegida es palindromo")
else:
    print("La palabra elegida no es palindromo")