class MembroUEPA:
    def __init__(self, nome: str, matricula: str, email: str):
        self.nome = nome
        self.matricula = matricula
        self.email = email

    def apresentar(self) -> str:
        return f"Membro UEPA. Nome: {self.nome}, Matrícula: {self.matricula}, Email: {self.email}"

class Aluno(MembroUEPA):
    def __init__(self, nome: str, matricula: str, email: str, curso: str):
        super().__init__(nome, matricula, email)
        self.curso = curso
        self._notas = []
    
    def apresentar(self) -> str:
        return f"Aluno: {self.nome} | Matrícula: {self.matricula} | Curso: {self.curso} | Email: {self.email}"

    def adicionar_nota(self, nota: float) -> None:
        if not isinstance(nota, (int, float)):
            raise ValueError("Nota deve ser numérica.")
        if nota < 0 or nota > 10:
            raise ValueError("Nota deve estar entre 0 e 10.")
        self._notas.append(float(nota))

    def verificar_notas(self) -> str:
        if not self._notas:
            return "Sem notas cadastradas."
        media = sum(self._notas) / len(self._notas)
        situacao = "Aprovado" if media >= 7 else "Em recuperação"
        return f"Notas: {self._notas} | Média: {media:.2f} | Situação: {situacao}"


class Professor(MembroUEPA):
    def __init__(self, nome: str, matricula: str, email: str, departamento: str):
        super().__init__(nome, matricula, email)
        self.departamento = departamento
        self._frequencias = {}

    def apresentar(self) -> str:
        return f"Professor: {self.nome} | Departamento: {self.departamento} | Email: {self.email}"

    def lancar_frequencia(self, matricula_aluno: str, porcentagem: float) -> None:
        if not isinstance(porcentagem, (int, float)):
            raise ValueError("Frequência deve ser numérica.")
        if porcentagem < 0 or porcentagem > 100:
            raise ValueError("Frequência deve estar entre 0 e 100.")
        self._frequencias[matricula_aluno] = float(porcentagem)

    def consultar_frequencia(self, matricula_aluno: str) -> str:
        if matricula_aluno not in self._frequencias:
            return "Sem lançamento de frequência."
        return f"Frequência do aluno {matricula_aluno}: {self._frequencias[matricula_aluno]:.1f}%"

# ...existing code...
if __name__ == "__main__":
    # Teste aluno:
    aluno = Aluno(nome="Ana Silva", matricula="2025A01", email="ana.silva@uepa.br", curso="Engenharia de Software")
    print(aluno.apresentar())
    aluno.adicionar_nota(8.0)
    aluno.adicionar_nota(7.5)
    aluno.adicionar_nota(9.0)
    print(aluno.verificar_notas())

    # Teste professor:
    prof = Professor(nome="Carlos Souza", matricula="P2025X01", email="carlos.souza@uepa.br", departamento="Computação")
    print(prof.apresentar())
    prof.lancar_frequencia(matricula_aluno="2025A01", porcentagem=92.5)
    print(prof.consultar_frequencia("2025A01"))
    print(prof.consultar_frequencia("2025A99"))