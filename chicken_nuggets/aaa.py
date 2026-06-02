import os
x = int(input("Digite sua idade: "))
print("você tem " + str(x) + " anos")
older = x >=18
if older:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
from datetime import date
y = date.today().year
print("Você naceu em " + str(y-x))
#test