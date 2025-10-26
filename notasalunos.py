class Aluno:
    def __init__(self, aluno, notas):
        self.aluno = aluno
        self.notas = notas
    
    def __str__(self):
        return f"Aluno: {self.aluno}, Notas: {self.notas}"
    
aluno1 = Aluno("João", [4.6, 7.5, 9.0])
aluno2 = Aluno("Marcos", [6.0, 10, 7.6])
aluno3 = Aluno("Marilia", [7.0, 9.5, 5.8])
aluno4 = Aluno("Ana", [3.0, 6.5, 7.0])
    
print(aluno1)
print(aluno2)
print(aluno3)
print(aluno4)

media = sum(aluno1.notas) / len(aluno1.notas)
if media >= 7:
    print(f"{aluno1.aluno} está aprovado com média {media}")
    
media = sum(aluno2.notas) / len(aluno2.notas)
if media >= 7:
    print(f"{aluno2.aluno} está aprovado com média {media}")
    
    