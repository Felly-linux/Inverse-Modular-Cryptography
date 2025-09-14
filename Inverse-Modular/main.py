"""
Decodificador de retos con inverso modular (ej. CTF tipo picoCTF)

 _________________________________________
/ Este codigo anteriormente lo sabia Dios \
| y nosotros dos.  Ahora solo lo sabe     |
\ Dios...                                /
 ----------------------------------------
         \   ^__^ 
          \  (oo)\_______
             (__)\       )\/\\
                 ||----w |
                 ||     ||
                 
Mejorado con manejo de errores, funciones y mensajes de depuración.
"""

def obtener_residuos(lista, mod):
    return [x % mod for x in lista]

def mapear(numero, alfabeto):
    return alfabeto[numero - 1] if 1 <= numero <= len(alfabeto) else '?'

def decodificar(residuos, mod, alfabeto):
    flag = ""
    detalles = []
    for i, r in enumerate(residuos):
        try:
            inv = pow(r, -1, mod)
            ch = mapear(inv, alfabeto)
            detalles.append((i, r, inv, ch))
            flag += ch
        except ValueError:
            detalles.append((i, r, None, '?'))
            flag += '?'
    return flag, detalles

if __name__ == "__main__":
    entrada_lista = input("Ingrese la lista de números separados por comas: ")
    lista_a = [int(x.strip()) for x in entrada_lista.split(",")]
    modulo = int(input("Ingrese el módulo: "))

    #==========================|
    #  TABLA DE CARACTERES     |
    #==========================|

    default_alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    alfabeto = input(
        f"Alfabeto (ENTER para usar el estándar picoCTF): "
    ).strip() or default_alfabeto

    residuos = obtener_residuos(lista_a, modulo)
    flag, detalles = decodificar(residuos, modulo, alfabeto)

    print("\n--- Residuos calculados ---")
    print(residuos)

    print("\n--- Decodificación paso a paso ---")
    for i, r, inv, ch in detalles:
        print(f"[{i:02}] residuo={r:2}  inverso={inv}  caracter='{ch}'")

    #imprimimos la flag final
    print("\n--- FLAG RESULTANTE ---")
    print("picoCTF{"+ flag +"}")

#==================================|
#  Codigo By Dvvsalom3 y Fellcrack |
#==================================|
#           14/09/2025             |
#==================================|

#DISFRUTENLO :D
#HACK THE PLANET!
#Happy hacking :D
#Si te gusta el codigo damos credito porfavor :D
#Estaremos desarrollando un tookit de herramientas para CTFs