#ain't get doxxed by the NSA, do NOT trust the DOT companies :D
#FREEDOM IS FOR ALL OF US!
#Decoder for Inverse Modular Challenges - picoCTF
#By Dvvsalom3 and Fellcrack
#Feel free to use and modify it as you wish :D
#If you do some interesting modification, please share it with us or do a github pull request :D
#If u find any bug, please report it to us :D
#We're open to suggestions :D
#  __________________________________________
# / This code was previously known and       \
# | understood by God and the two of us. Now |
# \ only God knows and understands it.       /
#  ------------------------------------------
    #     \   ^__^ 
   #       \  (oo)\_______
  #           (__)\       )\/\\
 #                ||----w |
#                 ||     ||
#|=====================================================================|                 
#|  Enhanced with error handling, debugging functions, and messages.   |
#|=====================================================================|
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
    entrada_lista = input("Put the list of numbers to decode (Separated by commas): ")
    lista_a = [int(x.strip()) for x in entrada_lista.split(",")]
    modulo = int(input("Put the module: "))

    #|==========================|
    #|     CHARACTERS TABLE     |
    #|==========================|

    default_alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    alfabeto = input(
        f"alfabet (ENTER to use the standart by picoCTF): "
    ).strip() or default_alfabeto

    residuos = obtener_residuos(lista_a, modulo)
    flag, detalles = decodificar(residuos, modulo, alfabeto)

    print("\n--- calculated waste ---")
    print(residuos)

    print("\n--- step-by-step decoding ---")
    for i, r, inv, ch in detalles:
        print(f"[{i:02}] residuo={r:2}  inverso={inv}  caracter='{ch}'")

    #imprimimos la flag final
    print("\n--- SOLVED FLAG ---")
    print("picoCTF{"+ flag +"}")

#Huh? Some of reverse engineering? :D
#Well, this is a simple script for decoding Inverse Modular Challenges from picoCTF
#and, to your knowledge, this ain't a challenge, btw, go to do something more productive :D
#This script was made in python3, so, please, run it with python3

#|==================================|
#| Script By Dvvsalom3 y Fellcrack  |
#|==================================|
#|          14/09/2025              |
#|==================================|

#Enjoy it so much :D
#HACK THE PLANET!
#Happy hacking :D
#If you liked the code, please give us some of credits :D
#We're gonna to make a toolkit for ctf :D (More like for cryptography)
