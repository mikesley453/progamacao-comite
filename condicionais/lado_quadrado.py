lado_1 = int(input(" informe um numero para primeiro lado -> "))
lado_2 = int(input(" informe o segundo numero -> "))
lado_3 = int(input(" informe o terceiro numero -> "))

if lado_1 + lado_2 > lado_3 or \
    lado_2 + lado_3 >lado_1 or \
    lado_1 + lado_3 > lado_2: 
    print(" triângulo valido! ")

if lado_1 == lado_2 == lado_3:
    print(" triangulo equilatero")
elif lado_1 == lado_2 or \
    lado_2 == lado_3 or \
    lado_1 == lado_3:
    print(" tiangulo isoceles")
elif lado_1 != lado_2 != lado_3:
    print (" triangulo escaleno")
else:
    print(" triângulo invalido! ")

