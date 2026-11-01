#Sistema de Análise de Notas dos Alunos

1. O que o programa faz?

O programa permite cadastrar o nome e a nota de vários alunos, calculando automaticamente os resultados da turma.

Após finalizar o cadastro, ele apresenta:

Nome e nota de cada aluno.

Quantidade total de alunos.

Média geral da turma.

Maior e menor nota, identificando os respectivos alunos.

Porcentagem e quantidade de alunos aprovados.

Quantidade de alunos em recuperação.

Quantidade de alunos reprovados.

A classificação é feita de acordo com as seguintes regras:

Aprovado: nota maior ou igual a 7.

Recuperação: nota maior ou igual a 5 e menor que 7.

Reprovado: nota menor que 5.

2. Como executar o programa?

É necessário ter o Python instalado no computador.

Salve o código em um arquivo chamado notas_alunos.py.

Abra o terminal na pasta onde o arquivo foi salvo.

Execute o seguinte comando:

python notas_alunos.py

3. Exemplo de entrada e saída

Entrada

Digite o nome do aluno: Ana
Digite a nota do aluno(0 a 10): 8
Deseja continuar? (sim/nao): sim

Digite o nome do aluno: Pedro
Digite a nota do aluno(0 a 10): 6
Deseja continuar? (sim/nao): sim

Digite o nome do aluno: Maria
Digite a nota do aluno(0 a 10): 4
Deseja continuar? (sim/nao): nao

Saída

Aluno(a): Ana. Nota: 8.00
Aluno(a): Pedro. Nota: 6.00
Aluno(a): Maria. Nota: 4.00

Total de alunos: 3
A media da turma foi: 6.00
A maior nota foi: 8.00, do aluno: Ana
A menor nota foi: 4.00, do aluno: Maria
A porcentagem de aprovados foi: 33.33%
A quantidade de alunos aprovados foi: 1
A quantidade de alunos em recuperação foi: 1
A quantidade de alunos reprovados foi: 1

4. O que eu aprendi?

Com o desenvolvimento desse programa, pratiquei conceitos importantes da linguagem Python, principalmente:

Listas: para armazenar os nomes e as notas dos alunos.

Estrutura de repetição (while): para permitir o cadastro de vários alunos.

Estruturas condicionais (if, elif e else): para classificar os alunos de acordo com suas notas.

Contadores: para acompanhar a quantidade de aprovados, alunos em recuperação e reprovados.

Funções nativas: como len(), sum(), max() e min(), para realizar cálculos e obter informações.

Índices e posições: para identificar qual aluno obteve a maior e a menor nota.

Laço for e função zip(): para percorrer duas listas ao mesmo tempo e apresentar os resultados.

Formatação de números: utilizando :.2f para exibir as notas e médias com duas casas decimais.

O principal aprendizado foi conseguir juntar esses conceitos para desenvolver um programa que recebe informações, realiza cálculos e apresenta resultados de forma automática.
