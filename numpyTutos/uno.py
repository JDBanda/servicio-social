import numpy as np
#Creación de un arreglo
a = np.array([1,2,3])
b = np.array([[9.0,5.2,0.3],[6.0,2.5,3.0]])
print('Arreglo a:',a)
print('Arreglo b:',b)
#Obtener la dimensión de un arreglo
print('Dimensión de a:',a.ndim)
print('Dimensión de b:',b.ndim)
'''
Algunos atributos de un arreglo numpy son:
shape = devuelve los datos de cada dimension
dtype = el valor del arreglo (puede se cambiado cuando se delcara uno nuevo
        a = np.array([1,2,3], dtype='int8/16/24/32'))
itemsize = cuantos octetos de bits conforman el arreglo
size = total de datos
nbytes = numero de bits en total que tiene el arreglo
'''
c = np.array([[1,2,4,5,6,7,8],[3,45,5,4,7,71,83]])
#Recuperando un valor [fila, columna]
print(c[1,2]) 

#Obteniendo una fila específica
print(c[0,:])
#Obteniendo una coumna
print(c[:,3])
#Acceso mas especifico, indicas la columna, donde empieza: donde termina : saltos
print(c[0,0:6:2])

#Reemplazar un elemento
c[1,5] = 0
print('Nuevo C:',c)

#Ejemplo con 3 dimensiones
d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print('indice 1 de cada y',d[:,1,:])

#Inicialización de arreglos
#Todoso con 0
e = np.zeros((2,4))
print('Ceros:',e)
#Todoso con 1
f = np.ones((5,3))
print('Unos',f)
#Inicializar con cualquier otro número, full_like sirve para crear un arreglo a partir de otro (copias el tamaño)
g = np.full((3,3),7)
print('7s:',g)

#Generar un arreglo random decimal
h = np.random.rand(4,2)
print('Arreglo random',h)

#Arreglo random enteros
i = np.random.randint(7,size=(3,3))
print('Enteros',i)

#Obtener matriz identidad
j = np.identity(7)
print('\n wey no:\n',j)

#Repetir un arreglo, la neta no le entendi
arr = np.array([[1,2,3]])
r1 = np.repeat(arr, 3, axis=0)
print('Se repite o algo así:',r1)

#Crear una matriz 5x5 con unos, ceros internos y 9 en medio
output = np.ones((5,5))
z = np.zeros((3,3))
z[1,1] = 9
output[1:-1, 1:-1] = z
print('TARAAAAAAN:\n',output)

#Si se desea copiar un elemento es necesario usar el metodo copy() de la variable que guarda el arreglo
ex = a.copy()
#Las operaciones matematicas hacen su funcion en cada elemento...
ex2 = a + 1
print('antes :',a)
print('despues :',ex2)
