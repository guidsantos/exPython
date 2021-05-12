Atividade - Eleição

Descrição do problema:

 

O TRT informatizou as eleições para prefeito. Escreva um programa que:

 

Inicialmente leia NumEleitores, o número de eleitores esperados para uma determinada seção eleitoral. Encerrado esse procedimento a urna é aberta e inicia-se o processo de votação.
Disponibilize uma tela ao eleitor, mostrando os candidatos, onde deve ser lido o código do seu candidato. Por exemplo:
Código	Candidato
11	João
45	Maria
0	branco
Se for digitado um código diferente desses será considerado Voto Nulo.

Quando todos os eleitores destinados para a seção já tiverem votado, o programa deve imprimir uma mensagem informando que a eleição está encerrada.
A eleição também pode ser encerrada pelo presidente da seção. Para isso o presidente deverá digitar o valor 1234 como voto para o código do candidato da tela anterior (Vamos adotar que só o presidente da seção eleitoral sabe disso). O Presidente da seção deve confirmar o encerramento da seção através de senha (Considere a senha 3571). Caso a senha seja digitada errada repetir a leitura da senha até que a senha esteja correta.
 

Após encerrada a eleição, o programa deve exibir na tela:

-O total de votos esperados na seção;
-Total e porcentagem de votos efetivamente depositados na urna eletrônica;
-Totalização de votos para cada um dos candidatos, bem como o total de votos nulos e brancos.