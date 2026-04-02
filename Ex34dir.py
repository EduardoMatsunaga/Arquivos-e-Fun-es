import os

global valor, dir, arq, arquivo
valor: int = 0
dir: str = ''
arq: str = ''
arquivo: str = ''


def main():
    global dir, valor
    cont: int = 0
    result: int = 0

    dir = '/tmp/exercicios'
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)

    valor = int(input('Digite um número para obter a tabuada:'))
    for cont in range (1,11):
        result = valor * cont
        print(f'{valor} x {cont} = {result}')
        grava(cont, result)

def grava(cont, result):
    global dir, arq
    dir = '/tmp/exercicios'
    arq = 'ex34.txt'
    file = '' 
    tipo = '' 
    enc = ''
    linha = ''
    linha = str(result) + '\n'
    tipo = 'w'
    file = dir + arq
    enc = 'utf-8'
    if (os.path.exists(file)):
        tipo = 'a'
    with open (file,tipo,encoding=enc) as f:
        f.write(linha)

def mult(vlr, tab):
    res = vlr * tab
    return res
    

if __name__ == '__main__':
    main()