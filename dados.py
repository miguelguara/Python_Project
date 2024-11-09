#importando CSV
import csv

lista = ['Rodolfo','F','12345679','abc@gmail.com','Rua aleatória']

def Adicionar_dados(i):
    #acessando cvs
    with open('dados.csv','a+',newline='') as file:
        escrever = csv.writer(file)
        escrever.writerow(i)


# função ver dados
def ver_dados():
    dados = []
    #acessando cvs
    with open('dados.csv') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
           dados.append(linha) 
    return dados

#função tirar dados
def Tirar_dados(i):
    
    def adicionar_novalista(j):
         with open('dados.csv','w',newline='') as file:
            escrever = csv.writer(file)
            escrever.writerows(j)
            ver_dados()


    
    
    nova_lisa = []
    telefone = i 
    with open('dados.csv','r') as file:
        ler_csv = csv.reader(file)
        
        for linha in ler_csv:
            nova_lisa.append(linha)
            for campo in linha:
                if campo == telefone:
                    nova_lisa.remove(linha)
                    
    adicionar_novalista(nova_lisa)

# atualizar dados
def Atualizar_dados(i):
    
    def adicionar_novalista(j):
         with open('dados.csv','w',newline='') as file:
            escrever = csv.writer(file)
            escrever.writerows(j)
            ver_dados()

    
    nova_lisa = []
    telefone = i[0] 
    with open('dados.csv','r') as file:
        ler_csv = csv.reader(file)
        
        for linha in ler_csv:
            nova_lisa.append(linha)
            for campo in linha:
                if campo == telefone:
                    nome = i[1]
                    sexo = i[2]
                    phone = i[3]
                    email = i[4]
                    rua = i[5]
                    
                    dados = [nome,sexo,phone,email,rua]
                    
                    index = nova_lisa.index(linha)
                    nova_lisa[index] = dados
                    
    adicionar_novalista(nova_lisa)
    
    
    
def pesquisar_dados(i):
    dados = []
    telefone = i
    #acessando cvs
    with open('dados.csv') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            for campo in linha:
                if campo == telefone:
                  dados.append(linha)       
    return dados