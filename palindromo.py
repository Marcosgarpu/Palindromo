def is_palindrome(ana):
    try:
        # Para evitar mayusculas y espacios de más
        palabraCorrecta = palabra.lower().replace(" ", "")

        palabraInvertida = ""

        for letra in palabraCorrecta:
            palabraInvertida = letra + palabraInvertida

        if palabraCorrecta == palabraInvertida:
            print("La palabra introducida es un palíndromo.")
            return True
        else: 
            print("La palabra introducida no es palindromo.")
            return False
    except ValueError:
        print("Error: no has introducido una palabra")