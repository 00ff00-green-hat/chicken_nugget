# 9 – Considere que você deseja fazer uma reserva mensal, em dinheiro, para a compra de
# um determinado presente para você mesmo(a). Considere que todo mês você depositará,
# em uma poupança no banco, um mesmo valor em reais. Faça um programa que leia o
# valor que será depositado mensalmente e exiba na tela o valor acumulado mês a mês
# durante 24 meses. Considere que a taxa de juros de uma poupança é 0,5% ao mês, que
# a poupança não possui nenhum saldo inicial. Você pode utilizar uma calculadora de juros
# compostos para validar o cálculo do seu algoritmo, por exemplo o site:
# https://www.idinheiro.com.br/calculadoras/calculadora-juros-compostos/

print("Não")

# Solicita o valor do depósito mensal fixo
deposito_mensal = float(input("Digite o valor do depósito mensal (R$): "))
taxa_juros = 0.005  # 0,5% ao mês
saldo_atual = 0.0

print("\nEvolução do saldo mês a mês:")
print("-" * 30)

# Simulação do rendimento ao longo de 24 meses
for mes in range(1, 25):
    # O depósito é feito no início do mês e rende juros
    saldo_atual = (saldo_atual + deposito_mensal) * (1 + taxa_juros)
    print(f"Mês {mes:02d}: R$ {saldo_atual:,.2f}")

print("-" * 30)
print(f"Valor total acumulado após 2 anos: R$ {saldo_atual:,.2f}")
