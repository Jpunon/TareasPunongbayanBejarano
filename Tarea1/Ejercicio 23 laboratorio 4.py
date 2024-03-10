#Ejercicio 23 laboratorio 4
#Hecho por Joel Punongbayan Bejarano
#carné 2024145400


n = int(input("Digite el numero que se desea:"))
#funcion
def Primo(n):
    for h in range(2, int(n/2)):
        if n % h == 0:
            return False
    return True

#programa
if Primo(n):
    print("El numero", n,"es primo")
else:
    print("El numero", n, "no es primo")
