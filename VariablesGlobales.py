vg='Global'
def funcion_v1():
    print(vg)
funcion_v1()
print(vg)
def funcion_v2():
    vg='Local'
    print(vg)
funcion_v3()
def funcion_v4():
    global vg
    print(vg)
    vg='Local'
    print(vg)
funcion_v4()
print(vg)
