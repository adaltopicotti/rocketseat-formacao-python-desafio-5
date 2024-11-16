from abc import ABC, abstractmethod


class Exame(ABC):
    @abstractmethod
    def verifica_condicoes(self) -> bool:
        pass


class ExameSangue(Exame):
    def verifica_condicoes(self) -> bool:
        print("Verificando condições para Exame de Sangue")
        # Para fins de exemplo, retornará true
        return True


class ExameRaioX(Exame):
    def verifica_condicoes(self) -> bool:
        print("Verificando condições para Exame Raio X")
        # Para fins de exemplo, retornará true
        return True


class AprovaExame:
    def aprovar_solicitacao_exame(self, exame: Exame):
        if exame.verifica_condicoes():
            print("Exame aprovado")
        else:
            print("Exame reprovado")


# Exemplo de uso:
exame_sangue = ExameSangue()
exame_raio_x = ExameRaioX()

aprovador = AprovaExame()
aprovador.aprovar_solicitacao_exame(exame_sangue)
aprovador.aprovar_solicitacao_exame(exame_raio_x)
