# 11 – Faça um programa para controlar o caixa de uma cantina. Seu programa deve
# solicitar ao usuário o código do produto pedido e a quantidade comprada. Suponha que
# para cada compra, apenas um tipo de produto possa ser comprado. O programa deve ser
# interrompido caso o usuário digite 0. Para cada compra, seu programa deve exibir na tela
# o nome do produto comprado e o valor total da compra. Ao final do programa, deve exibir
# o valor total acumulado no caixa. Utilize a seguinte tabela de produtos como referência:
# Código Produto Valor
# 1 Suco R$ 6,00
# 2 Pão de queijo R$ 3,00
# 3 Pastel R$ 7,00
# 4 Salada de frutas R$ 9,00
# 5 Café com leite R$ 3,50
# 6 Cappuccino R$ 4,50
# 7 Iogurte R$ 6,50
# 8 Água R$ 2,50
import sys
p=int(input("Digite o codigo do produto: "))
q=int(input("Digite a quantidade do produto: "))
if q==0:
    sys.exit()
elif p==1:
    v=6*q
    print("")
elif p==2:
    v=3*q
elif p==3:
    v=7*q
elif p==4:
    v=9*q
elif p==5:
    v=3.5*q
elif p==6:
    v=4.5*q
elif p==7:
    v=6.5*q
elif p==8:
    v=2.5*q    

