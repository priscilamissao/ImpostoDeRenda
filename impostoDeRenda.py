
porcentagem1 = 7.5/100
porcentagem2 = 15/100
porcentagem3 = 22.5/100
porcentagem4 = 27.5/100

print("MEU IMPOSTO DE RENDA")
salario = float(input("digite seu salario bruto:"))



if salario <= 1903.63:
    print("aliquota: 0%")
    print("Isento")
else: 
    if salario >= 1903.63 and salario <= 2826.98:
        print("Aliquota: 7,5%")
        print("Sárario liquido é de: ", salario - porcentagem1)
    else:
        if salario >=2826.98 and salario <= 3751.67:
            print("Aliquota: 15%")
            print("Salario liquido é de: ", salario - porcentagem2)
        else:
            if salario >=3751.67 and salario <=4664.94:
                print("Aliquota: 22,5%")
                print("Salario liquido é de: ", salario - porcentagem3)
            else:
                if salario >= 4664.94:
                    print("Aliquota: 27,5%")
                    print("Salario liquido é de:" , salario - porcentagem4)