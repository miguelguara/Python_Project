from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from dados import *

co0 = "#f0f3f5" 
co1 = "#f0f3f5"  
co2 = "#feffff" 
co3 = "#38576b"  
co4 = "#403d3d"  
co5 = "#6f9fbd" 
co6 = "#ef5350"  
co7 = "#93cd95"  

janela = Tk()
janela.title("Software Inclusão de idosos")
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
janela.geometry("600x550")
janela.configure(background=co2)
janela.resizable(width=TRUE,height=TRUE)

style = Style(janela)
style.theme_use("clam")

frame_cima = Frame(janela,width=500,height=50,bg=co3,relief="flat")
frame_cima.grid(row=0,column=0,pady=1,padx=0,sticky=NSEW)

frame_baixo = Frame(janela,width=500,height=190,bg=co1,relief="flat")
frame_baixo.grid(row=1,column=0,pady=1,padx=0,sticky=NSEW)

frame_tabela = Frame(janela,width=500,height=248,bg=co2,relief="flat")
frame_tabela.grid(row=2,column=0,columnspan=2,padx=10,pady=30,sticky=NW)

#configurando a parte de cima

l_nome = Label(frame_cima,text='Registro de Clientes',font=('arial 20 bold'),bg=co3,fg=co1)
l_nome.pack(fill=BOTH,expand=TRUE)
l_nome.place(x=5,y=5)


l_linha = Label(frame_cima,text='',width=500,anchor=NE,font=('arial 1'),bg=co2,fg=co1)
l_linha.place(x=0,y=46)


global tree

def mostrar_dados():

     global tree
     #configurando frame tabela
     Cab_lista = ['Nome','Sexo','Telefone','e-mail','Endereço']
     dados = ver_dados()

     tree = ttk.Treeview(frame_tabela,selectmode="extended",columns=Cab_lista,show="headings")

     #barra de rolagem
     vbr = ttk.Scrollbar(frame_tabela,orient="vertical",command=tree.yview)
     hbr = ttk.Scrollbar(frame_tabela,orient="horizontal",command=tree.xview)

     tree.configure(yscrollcommand=vbr.set,xscrollcommand=hbr.set)

     tree.grid(column=0,row=0,sticky='nsew')
     vbr.grid(column=1,row=0,sticky='ns')
     hbr.grid(column=0,row=1,sticky='ew')

     hd = ["nw","nw","nw","nw","nw"]
     h=[120,50,80,120,200]
     n=0

     tree.heading(0,text='Nome',anchor=NW)
     tree.heading(1,text='Sexo',anchor=NW)
     tree.heading(2,text='Telefone',anchor=NW)
     tree.heading(3,text='Email',anchor=NW)
     tree.heading(4,text='Endereço',anchor=NW)

     tree.column(0,width=120,anchor='nw')
     tree.column(1,width=50,anchor='nw')
     tree.column(2,width=100,anchor='nw')
     tree.column(0,width=120,anchor=hd[0])


     for item in dados:
          tree.insert('','end',values=item)
          
mostrar_dados()

#funcao de inserir
def inserir():
     nome = en_nome.get()
     sexo = c_sexo.get()
     tel = en_Telefone.get()
     email = en_Email.get()
     rua = en_Endereco.get()
     dados = [nome,sexo,tel,email,rua]
     
     if nome =='' or sexo =='' or tel== '' or email == '' or rua =='':
      messagebox.showwarning('Dados','PREENCHA TODOS OS DADOS')
     else:
          Adicionar_dados(dados)
          messagebox.showinfo('Dados','OS DADOS FORAM ADICIONADOS COM SUCESSO')
          
          en_nome.delete(0,'end')
          c_sexo.delete(0,'end')
          en_Telefone.delete(0,'end')
          en_Email.delete(0,'end')
          en_Endereco.delete(0,'end')
          mostrar_dados() 

def atualizar():
   
     try:
          treev_dados = tree.focus()
          treev_dicionario = tree.item(treev_dados)
          tree_lista = treev_dicionario['values']
          
          nome = tree_lista[0]
          sexo = tree_lista[1]
          tel = str(tree_lista[2])
          email = tree_lista[3]
          rua = tree_lista[4]
          
          en_nome.insert(0,nome)
          c_sexo.insert(0,sexo)
          en_Telefone.insert(0,tel)
          en_Email.insert(0,email)
          en_Endereco.insert(0,rua)
          
          def confirmar():
               nome = en_nome.get()
               sexo = c_sexo.get()
               tel_novo = en_Telefone.get()
               email = en_Email.get()
               rua = en_Endereco.get()
               dados = [tel,nome,sexo,tel_novo,email,rua]
               
               Atualizar_dados(dados)
               
             
               messagebox.showinfo('Dados','OS DADOS FORAM ATUALIZADOS COM SUCESSO')
                    
               en_nome.delete(0,'end')
               c_sexo.delete(0,'end')
               en_Telefone.delete(0,'end')
               en_Email.delete(0,'end')
               en_Endereco.delete(0,'end')
               
               b_con.destroy()
               mostrar_dados()  

          b_con = Button(frame_baixo,command=confirmar,text='Confirmar',width=10,font=('ivy 8 bold'),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
          b_con.place(x=300,y=100)
          
     except:
          messagebox.showwarning('Dados','POR FAVOR SELECIONE UMA INFORMAÇÃO DA TABELA')

def remover():
     try:
          treev_dados = tree.focus()
          treev_dicionario = tree.item(treev_dados)
          tree_lista = treev_dicionario['values']
          
          tel = str(tree_lista[2])
          
          Tirar_dados(tel)
          
          messagebox.showinfo('Dados','OS DADOS FORAM DELETADOS COM SUCESSO')
          
          for widget in frame_tabela.winfo_children():
               widget.destroy()
               
          mostrar_dados()
          
     except:
          messagebox.showwarning('Dados','POR FAVOR SELECIONE UMA INFORMAÇÃO DA TABELA')

def procurar():
    tel = en_procurar.get()
    dados = pesquisar_dados(tel)
    tree.delete(*tree.get_children())
    
    for item in dados:
         tree.insert('','end',values=item)
         
    en_procurar.delete(0,'end')
     
#configurando o formulário
l_nome = Label(frame_baixo,text='Nome *',anchor=NW,font=('ivy 15'),bg=co1,fg=co4)
l_nome.place(x=10,y=15)
en_nome = Entry(frame_baixo,width=25,justify='left',font=('',10),highlightthickness=1)
en_nome.place(x=110,y=20)


l_sexo = Label(frame_baixo,text='Sexo *',anchor=NW,font=('ivy 15'),bg=co1,fg=co4)
l_sexo.place(x=10,y=50)
c_sexo = Combobox(frame_baixo,width=27)
c_sexo['value'] = ('','F','M','Outro')
c_sexo.place(x=110,y=50)

l_Telefone = Label(frame_baixo,text='Telefone*',anchor=NW,font=('ivy 15 '),bg=co1,fg=co4)
l_Telefone.place(x=5,y=80)
en_Telefone = Entry(frame_baixo,width=25,justify='left',font=('',10),highlightthickness=1)
en_Telefone.place(x=110,y=80)

l_Email = Label(frame_baixo,text='E-mail*',anchor=NW,font=('ivy 15'),bg=co1,fg=co4)
l_Email.place(x=10,y=110)
en_Email = Entry(frame_baixo,width=25,justify='left',relief="sunken",font=('',10),highlightthickness=1)
en_Email.place(x=110,y=110)

l_Endereco = Label(frame_baixo,text='Endereço*',anchor=NW,font=('ivy 15'),bg=co1,fg=co4)
l_Endereco.place(x=10,y=140)
en_Endereco = Entry(frame_baixo,width=25,justify='left',relief="sunken",font=('',10),highlightthickness=1)
en_Endereco.place(x=110,y=145)

b_procurar = Button(frame_baixo,command=procurar,text='procurar',font=('ivy 8 bold'),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_procurar.place(x=300,y=20)
en_procurar = Entry(frame_baixo,width=16,justify='left',font=('',11),highlightthickness=1)
en_procurar.place(x=360,y=20)

b_Olhar = Button(frame_baixo,command=mostrar_dados,text='Ver dados',width=10,font=('ivy 8 bold'),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_Olhar.place(x=300,y=50)

b_Adicionar = Button(frame_baixo,command=inserir,text='Adicionar',width=10,font=('ivy 8 bold'),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_Adicionar.place(x=410,y=50)

b_Atualizar = Button(frame_baixo,command=atualizar,text='Atualizar',width=10,font=('ivy 8 bold'),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_Atualizar.place(x=410,y=80)

b_Deletar = Button(frame_baixo,command=remover,text='Deletar',width=10,font=('ivy 8 bold'),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_Deletar.place(x=410,y=110)


          
mostrar_dados()

janela.mainloop()
