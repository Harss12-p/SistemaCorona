print("Corona circular")
radio_ma = float(input("ingrese radio mayor: "))
radio_me = float(input("ingrese radio menor: "))
area = 3.14*(radio_ma**2 - radio_me**2)
perimetro = 2*3.14*radio_ma + 2*3.14*radio_me
print("resultado")
print("Area:", area.__around__(2))
print("Perimetro:", perimetro.__around__(2))
