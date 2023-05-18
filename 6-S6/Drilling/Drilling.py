usuarios = {'001':'Marca','002':'Mónica','003':'Jacob'}
id_usuario = '004'
mensaje = 'La clave 004 no está en el diccionario. Añadiendo clave...' 

try:
    print(usuarios[id_usuario])
except KeyError:
    print(mensaje)
    usuarios[id_usuario]= None

print(usuarios)