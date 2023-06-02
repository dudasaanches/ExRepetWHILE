soma = 0
qnt = 0
while True:
    ini = float(input("Digite número: "))
    qnt += 1
    soma += ini
    if ini < 0:
     print("Número negativo")
     media = soma / qnt
     print(f"A média é de {media}")
     break
    f = str(input("Desejar continuar?[S/N]: "))
    if f == "N":
     media = soma / qnt
     print(f"A média é de {media}")
     break