def imprime_nombre(nombre):
    print('hola' +nombre)
imprime_nombre("JJ")
def cuadrado(x):
    return x**2
x=5
print('el cuadrado de {} es {}'.format(x, cuadrado(x)))
def varios(x):
    return x**2, x**3,x**4
vall, vall2, vall3=varios(2)
print('{} {} {}'.format(vall, vall2, vall3))
def cuadrado_default(x=3):
    return x**2
cuadrado_default()
val4, _, val5=varios(2)
print('{} {}'.format(val4, val5))
