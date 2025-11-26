class CDs:
    def __init__(self, titulo, ano, ehDuplo=False, ehColetania=False):
        self.titulo = titulo
        self.ano = ano
        self.ehDuplo = ehDuplo
        self.ehColetania = ehColetania
        self.musicas = []
        self.musicos = []
        
        def cadastrar(self):
            print(f"CD {self.titulo} cadastrado com sucesso!")
            
        def adicionar_musica(self, musica):
            self.musicas.append(musica)
            musica.cds.append(self)
            
        def adicionar_musico(self, musico):
            self.musicos.append(musico)
            musico.cds.append(self)
            
        def listarCDS_musica(musica, lista_cds):
            cds_da_musica = []
            for cd in lista_cds:
                if musica in cd.musicas:
                    cds_da_musica.append(cd)
            
        def listarCDS_musico(musico, lista_cds):
            cds_do_musico = []
            for cd in lista_cds:
                if musico in cd.musicos:
                    cds_do_musico.append(cd)
            return cds_do_musico 
            
        def listarMusicas(self):
            print(self.musicas)
            
        def listarMusicos(self):
            print(self.musicos)
            
class Musico:
    def __init__(self, nome, ehSolo=True):
        self.nome = nome
        self.ehSolo = ehSolo
    
    def cadastrar(self):
        print(f"Músico {self.nome} cadastrado com sucesso!")
        self.cds = []
        
class Musica:
    def __init__(self, nome, tempoFaixa):
        self.nome = nome
        self.tempoFaixa = tempoFaixa
        self.cds = []
        
    def cadastrar(self):
        print("Música {self.nome} cadastrada com sucesso!")
        
    def cadastrar(self):
        print(f"Música {self.titulo} cadastrada com sucesso!")
        
# Criando Músicos
roberto_carlos = Musico("Roberto Carlos", True)
tim_maia = Musico("Tim Maia", True)
print(roberto_carlos.nome)



#criando musicas:
musica1 = Musica("Música 1", 3.40)
musica2 = Musica("Música 2", 2.57)
musica3 = Musica("Música 3", 3.15)

#criando cds:

cd1 = CDs("As Melhores do Roberto Carlos", 1995, True)
cd2 = CDs("Tim Maia - Aústico", 1997, False)

# configurando relaçoes:
cd1.adicionar_musica(musica1)
cd2.adicionar_musica(musica2)
cd1.adicionar_musico(roberto_carlos)
cd2.adicionar_musico(tim_maia)
print("\nListagem:\n")
cd1.listar_musicas()
cd2.listar_musicas()
cd1.listar_musicos()
cd2.listar_musicos()


