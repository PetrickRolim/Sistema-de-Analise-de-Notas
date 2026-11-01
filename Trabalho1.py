aluno = []
notas = []
aprovados = 0
recuperacao = 0
reprovados = 0

while True:
    nome = input("Digite o nome do aluno: ")
    nota_digitada = float(input("Digite a nota do aluno(0 a 10): "))
    aluno.append(nome)
    notas.append(nota_digitada)

    if nota_digitada >= 7:
        aprovados += 1
    elif nota_digitada >= 5:
        recuperacao += 1
    else:
        reprovados += 1

    continuar = input("Deseja continuar? (sim/nao): ").strip().lower()

    if continuar == "nao":
        break   

alunos = len(aluno)
media_da_turma = sum(notas) / alunos
maior_nota = max(notas)
menor_nota = min(notas)
posicao_maior_nota = notas.index(maior_nota)
aluno_maior_nota = aluno[posicao_maior_nota]
posicao_menor_nota = notas.index(menor_nota)
aluno_menor_nota = aluno[posicao_menor_nota]
porcentagem_aprovados = (aprovados / alunos) * 100
for aluno_nome, nota in zip(aluno, notas):
    print(f"Aluno(a): {aluno_nome}. Nota: {nota:.2f}")
print(f"Total de alunos: {alunos}")
print(f"A media da turma foi: {media_da_turma:.2f}")
print(f"A maior nota foi: {maior_nota:.2f}, do aluno: {aluno_maior_nota}")
print(f"A menor nota foi: {menor_nota:.2f}, do aluno: {aluno_menor_nota}")
print(f"A porcentagem de aprovados foi: {porcentagem_aprovados:.2f}%")
print(f"A quantidade de alunos aprovados foi: {aprovados}")
print(f"A quantidade de alunos em recuperação foi: {recuperacao}")
print(f"A quantidade de alunos reprovados foi: {reprovados}")
