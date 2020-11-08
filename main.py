from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def conecta_base():
    conexao = MongoClient("mongodb://admin:admin@localhost:27017/")
    try:
        conexao.admin.command('ismaster')
        print("\nSistema  conectou na base\n")
        base = conexao['prova']
        tabela = base['musica']
    except ConnectionFailure:
        print("Sistema não conectou na base")
    return tabela

def insere_valor(album):
    musica = {}
    print(50 * "-" + "\n" + "Prova N2 - Atividade 2")
    print(50 * "-" + "\n" + "Cadastro de música base MongoDB" + "\n" + 50 * "-")
    nome = input("Nome da música : ")
    musica['nome'] = nome
    autor = input("Nome do autor música : ")
    musica['autor'] = autor
    genero = input("Nome do gênero música : ")
    musica['genero'] = genero
    album.insert_one(musica)
    print("Musica {} do autor {}(gênero {}) foi adicionado ao MongoDB.".format(nome, autor, genero))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    base = conecta_base()
    insere_valor(base)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
