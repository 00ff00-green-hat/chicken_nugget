# 1 - Implemente um programa com um cadastro de idades de 6 alunos utilizando lista. O
# programa deve solicitar as idades dos 6 alunos. Após informar todas as idades, deve-se
# apresentar apenas as idades que forem maiores ou iguais a 16.
a=int(input("Aluno 1:"))
b=int(input("Aluno 2:"))
c=int(input("Aluno 3:"))
d=int(input("Aluno 4:"))
e=int(input("Aluno 5:"))
f=int(input("Aluno 6:"))
alunos = [a, b, c, d, e, f]
for i in (0, 6):
    if alunos[i]>=16:
        print(alunos[i])