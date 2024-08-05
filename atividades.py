# ATIVIDADE 1 #

'''
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

soma = nota1 + nota2

print(f"A soma de {nota1} e {nota2} é: {soma}")
'''

# ATIVIDADE 2 #

'''
def cadastro_de_usuario():

    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")
    telefone = input("Digite o seu telefone: ")
    email = input("Digite o seu e-mail: ")

    print("\nDados cadastrados:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Telefone: {telefone}")
    print(f"E-mail: {email}")

cadastro_de_usuario()
'''

# ATIVIDADE 3 #

'''
def cadastrar_informacao_produto():

    nome = input("Digite o nome do produto: ")
    codigo = input("Digite o código do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço do produto: "))

    valor_total = quantidade * preco

    print("\nInformações do produto cadastrado:")
    print(f"Nome: {nome}")
    print(f"Código: {codigo}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço: R${preco}")
    print(f"Valor total da compra: R${valor_total}")

cadastrar_informacao_produto()
'''

# ATIVIDADE 4 #

'''
def converter_centimetros_em_metros():

    centimetros = float(input("Digite o valor em centímetros: "))
    metros = centimetros / 100
    print(f"{centimetros} centimetros é igual a {metros} metros")

converter_centimetros_em_metros()
'''

# ATIVIDADE 5 #

'''
def calcular_area_de_um__quadrado_retangulo():

    comprimento = float(input("Digite o comprimento: "))
    largura = float(input("Digite a largura: "))

    area = comprimento * largura

    print(f"A área do quadrado/retângulo é: {area} unidades quadradas")

calcular_area_de_um__quadrado_retangulo()
'''