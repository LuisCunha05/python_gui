from __future__ import annotations
from typing import Literal
from database import DB
from usuario import Usuario
from livro import Livro

class Biblioteca:
    Acervo: list[Livro] = []

    @staticmethod
    def cadastrar(livro: Livro) -> bool:
        if(livro in Biblioteca.Acervo):
            print("Livro já está cadastrado!")
            return False

        Biblioteca.Acervo.append(livro)

    @staticmethod
    def listar():
        for idx, book in enumerate(Biblioteca.Acervo):
            print(f'Livro {idx}: {book}')
    
    @staticmethod
    def getAtributos(index: int):
        livro = Biblioteca.Acervo[index]

        return f"""
            {livro.titulo},
            {livro.autor},
            {livro.status},
            {livro.codigo},
            {livro.usuario}
        """
    @staticmethod
    def fazerEmprestimo(usuario: Usuario, livro: Livro) -> bool:
        if(len(usuario.livros) == usuario.getMaxEmprestimo()):
            print('O usuário já atingiu o maximo de emprestimos')
            return False
        
        if(livro.status != 'Disponivel'):
            print('O livro não pode ser emprestado!')
            return False
        
        usuario.adicionarLivro(livro.titulo)
        livro.emprestarLivro(usuario)
    @staticmethod
    def fazerDevolucao(usuario: Usuario, livro: Livro) -> bool:
        if(len(usuario.livros) == 0):
            print('O usuário não possui livros para devolver')
            return False
        
        if(livro.status != 'Emprestado'):
            print('O livro não está emprestado!')
            return False
        
        usuario.adicionarLivro(livro)
        livro.devolverLivro()

if __name__ == "__main__":
    pass