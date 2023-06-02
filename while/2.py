pares = 0
while True:
    ini = int(input("Digite número[digite 0 para parar]:  "))
    if ini % 2 == 0:
     pares += ini
    if ini == 0:
     print(f"Soma dos números pares: {pares}")
     break