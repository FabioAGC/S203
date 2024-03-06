class Filme:
    def __init__(self, titulo, ano_lancamento, diretor, genero, duracao):
        self.titulo = titulo
        self.ano_lancamento = ano_lancamento
        self.diretor = diretor
        self.genero = genero
        self.duracao = duracao

class CatalogoFilmes:
    def __init__(self):
        self.filmes = []

    def adicionar_filme(self, filme):
        self.filmes.append(filme)

    def listar_filmes(self, filtro=None, ordenacao=None):
        lista_filtrada = self.filmes

        if filtro:
            if isinstance(filtro, int):
                lista_filtrada = [filme for filme in lista_filtrada if filme.ano_lancamento == filtro]
            elif isinstance(filtro, str):
                lista_filtrada = [filme for filme in lista_filtrada if filme.diretor == filtro or
                                                                        filme.genero == filtro]

        if ordenacao:
            lista_filtrada.sort(key=lambda x: getattr(x, ordenacao))

        for filme in lista_filtrada:
            print(f"Título: {filme.titulo}, Ano de Lançamento: {filme.ano_lancamento}, Diretor: {filme.diretor}, Gênero: {filme.genero}, Duração: {filme.duracao} minutos")

# Exemplo de uso
catalogo = CatalogoFilmes()

filme1 = Filme("Stalker", 1979, "Andrei Tarkovsky", "Drama", 161)
filme2 = Filme("Senhor dos Anéis: O Retorno do Rei", 2003, "Peter Jackson", "Fantasia", 201)
filme3 = Filme("Fallen Angels", 1995, "Wong Kar-wai", "Drama", 96)

catalogo.adicionar_filme(filme1)
catalogo.adicionar_filme(filme2)
catalogo.adicionar_filme(filme3)

print("Listagem de todos os filmes:")
catalogo.listar_filmes()

print("\nListagem de filmes do diretor Peter Jackson:")
catalogo.listar_filmes(filtro="Peter Jackson")

print("\nListagem de filmes lançados em 1995:")
catalogo.listar_filmes(filtro=1995)

print("\nListagem de filmes de Drama:")
catalogo.listar_filmes(filtro="Drama")