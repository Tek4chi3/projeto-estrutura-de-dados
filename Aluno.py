class Aluno:
    média=[]
    @classmethod
    def nome(self,nome):
        print(f"Seu nome é {nome}")

    @classmethod
    def notas(self,nota1,nota2,nota3):
        print(f"Suas três notas são: {nota1}, {nota2} e {nota3}")
        média_def=(nota1+nota2+nota3)/3
        print(f"Dessa forma, sua média é {média_def:.2f}")
        self.média.append(média_def)


    @classmethod
    def aprovação(cls):
        if sum(cls.média)<7:
            print("O aluno foi reprovado")
        else:
            print("O aluno foi aprovado")


Aluno.nome("Vítor")
Aluno.notas(8,9,4)
Aluno.aprovação()
