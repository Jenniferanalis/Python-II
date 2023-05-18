# Error aritmetico

try:
    suma = 3000
    contador = 0
    resultado = suma / contador
    print(resultado)
        
except ZeroDivisionError as e:
    print(f'{e} no permitido') #Error: division by zero no permitido
except Exception as error:
    print(f'Error: {error}')

