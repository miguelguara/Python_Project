#importando CSV
import csv

lista = ['Miguel','F','12345679','abc@gmail.com']

#acessando cvs
with open('dados.csv','a+',newline='') as file:
    escrever = csv.writer(file)