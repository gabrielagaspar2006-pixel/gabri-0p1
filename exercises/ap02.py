import sys
sys.stdout.reconfigure (encoding="utf-8")
# comentario
'''
comentario de varias linhas
'''

nome = 'Luis A. Gomes'
print(f"Olá " + nome)

print(f"Olá {nome}, \nbem-vindo!")

# receber dados de utilizador
uc = input(f"Olá {nome}, escreve o nome de uma disciplina:")

print("Olá {Maria},  \nbem-vindo a {universidade}")

print("nome é do tipo:" + type (nome)._name_)