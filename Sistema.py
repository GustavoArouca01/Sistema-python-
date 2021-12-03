import os,sqlite3,time,datetime

class visitantes:
    def __init__(self):
        self.nome=""
        self.empresa=""
        self.hora=""
        self.piloto=""

    def cadastrar(self):
        rodando = True
        while rodando:
            print(8*"##" ,8*"##")
            print(8*"##" ,"Cadastrar Visitante", 8*"##")

            self.nome = input("Nome:").strip().upper()
            time.sleep(0.6)
            self.empresa = input("Empresa:").strip().upper()
            time.sleep(0.6)
            hora_e_data = int(time.time())
            self.hora = str(datetime.datetime.fromtimestamp(hora_e_data).strftime("%Y-%m-%d %H:%M"))
            self.Piloto = input("Documento:").strip().upper()
            time.sleep(0.6)
            db = sqlite3.connect("conexao")
            cursor = db.cursor()
            print() 
            print("Cadastro realizado com sucesso") 
            time.sleep(1)

            db.commit()
            adicionar_mais = input("você deseja continuar cadastrando? (s/n)").upper()
            if adicionar_mais =="s":
                continue
            else:
                rodando = False
                db.close()
                print("Voltando para a tela principal.")
                time.sleep(2)
                self.menu




    def procurar(self):
        pass

    def editar(self):
        pass

    def visualizar(self):
        print("-------------------------------------------------")
        print("--------Visualizar visitantes cadastrados--------")
        print("-------------------------------------------------")
        db = sqlite3.connect("conexao")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM visitantes")
        lista = cursor.fetchall()
        for i in lista:
            print(f'{i[0]:<25}{i[1]:<25}{i[2]:<25}{i[3]:<25}{i[4]:<25}')
        print()
        input("Essas são todas as pessoas cadastradas!").upper()
        opcao = input("A) Editar  B) Menu Principal")
        if opcao == "A":
            self.editar()
        elif opcao == "B":
            self.menu()
        else:
             print(" OPÇÃO INCORRETA, SELECIONE UMA OPÇÃO ACIMA!!!")
             self.menu()



    def apagar(self):
        pass

    def sair(self):
        pass


    def menu(self):
        os.system("cls")
        print("Menu de opções")
        print(" 1) Cadastrar  2)Procurar  3)Editar  4)Visualizar  5)Apagar  6)Sair")
        print(f'{"id:":<25}{"Aeronave:":<25}{"Empresa:":<25}{"Hora:":<25}{"Piloto:":<25}')
        db = sqlite3.connect("conexao")
        cursor = db.cursor()
        lista = cursor.fetchall()
        print(lista)
        for i in lista:
            print(f'{i[0]:<25}{i[1]:<25}{i[2]:<25}{i[3]:<25}{i[4]:<25}')

        acao = input ("Digite uma ação de 1 a 6:")

        if acao =='1':
            self.cadastrar()

        elif acao =='2':
            self.procurar()

        elif acao =='3':
            self.editar()

        elif acao =='4':
            self.visualizar()

        elif acao =='5':
            self.apagar()

        elif acao =='6':
            self.sair()

        else:
            print("OPÇÃO INVÁLIDA, DIGITE UM COMANDO DE 1 A 6!!!")
            time.sleep(2) 
            self.menu()




    def janelaprincipal(self):
        os.system("cls")
        if os.path.isfile("conexao"):
            db = sqlite3.connect("conexao")
            print("conectado com sucesso ao banco de dados")
            self.menu()

        else:
            print("O arquivo de conexão não existe")
            time.sleep(3)
            print("Criando arquivo de conexão")
            time.sleep(3)    
            db = sqlite3.connect("conexao")  
            cursor = db.cursor()
            cursor.execute("""CREATE Table if not exist aeronaves
                        (Ide INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL,empresa TEXT NOT NULL,hora TEXT NOT NULL, piloto TEXT NOT NULL)""")
            print("A conexão foi criada com sucesso!")
            time.sleep(3)
            self.menu()            
       
        self.menu()


gerenciamento_visitantes = visitantes()
gerenciamento_visitantes.janelaprincipal()    