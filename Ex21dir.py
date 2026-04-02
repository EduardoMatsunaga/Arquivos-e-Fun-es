import os

global nome, nota1, nota2, nota3, nota4, valor_media, dir, arq
nome: str = ''
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0
dir: str = '/tmp/exercicios'
arq: str = 'ex21.txt'

def med(n1,n2,n3,n4):
    media = float((n1 + n2 + n3 + n4) / 4)
    return media

def entrada():
    global nome, nota1,nota2,nota3,nota4,valor_media
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    nota4 = float(input('Digite a quarta nota: '))
    valor_media = med(nota1,nota2,nota3,nota4)
    print(f"A média de {nome} foi: {valor_media}")
    cadastro(nome, nota1,nota2,nota3,nota4,valor_media)
    return valor_media

def cadastro(nome,nota1,nota2,nota3,nota4,valor_media):
    global dir, arq
    linha: str = ''
    dir = '/tmp/exercicios'
    arq = 'ex21.txt'
    linha = nome + ':' + str(nota1) + ';' + str(nota2) + ';' + str(nota3) + ';' + str(nota4) + ';' + str(valor_media) + '\n'
    escrevaArq(dir,arq,linha)

def escrevaArq(dir,arq,linha):
    file: str = ''
    tipo: str = ''
    enc: str = ''
    tipo = 'w'
    file = dir + arq
    enc = 'utf-8'
    if os.path.exists(file):
        tipo = 'a'
    with open(file,tipo,enconding = enc) as f:
        f.write(linha)
    
def main():
    global dir
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)
    for cont in range(1,6):
        entrada()

if __name__ == '__main__':
    main()