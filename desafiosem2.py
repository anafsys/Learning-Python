sal_bruto = float(input("Digite salário bruto: "))
qtd_dep = float(input("Digite a quantidade de dependentes: "))

deducao_dep = qtd_dep * 189.59

if sal_bruto <= 1302:
    parc_inss = sal_bruto * 0.075
elif sal_bruto >= 1302.01 or sal_bruto <= 2571.29:
    parc_inss = sal_bruto * 0.09
elif sal_bruto >= 2571.30  or sal_bruto <= 3856.94:
    parc_inss = sal_bruto * 0.12
elif sal_bruto >= 3856.95:
    parc_inss = sal_bruto * 0.14

ir_mes = 0

if sal_bruto >= 1903.99 or sal_bruto <= 2826.65:
    ir_mes = ((sal_bruto - deducao_dep - parc_inss) * 0.075)- 142.80
    print(round(ir_mes,2)) 
elif sal_bruto >= 2826.66 or sal_bruto <= 3751.05:
    ir_mes = ((sal_bruto - deducao_dep - parc_inss) * 0.15) - 354.80
    print(ir_mes, round(2))     
elif sal_bruto >= 3751.06 or sal_bruto <= 4664.68:
    ir_mes = ((sal_bruto - deducao_dep - parc_inss) * 0.225) - 636.13
    print(ir_mes, round(2)) 
elif sal_bruto >= 4664.69:
    ir_mes = ((sal_bruto - deducao_dep - parc_inss) * 0.275) - 869.36
    print(ir_mes, round(2)) 
else:
    print("Isento")    