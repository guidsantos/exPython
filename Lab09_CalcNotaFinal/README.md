# 06/05: Lab09 - Cálculo da Nota Final

Nesta tarefa você deverá calcular a **Nota Final** de uma determinada disciplina prática de um aluno, assim como a sua situação final ("Aprovado por nota", "Reprovado por nota", "Aprovado no exame" ou "Reprovado no exame").

Como **entrada** para o programa, você receberá as **notas dos laboratórios** de um aluno e os **pesos de cada laboratório**.

- Caso a **média ponderada** dos laboratórios seja **maior ou igual** a **5,0** **ou** a **média ponderada** seja **menor** que **2,5**:
    - **Nota Final = média ponderada dos laboratórios**
- Caso a **média ponderada** dos laboratórios seja **maior ou igual** a **2,5** **e** **menor** que **5,0**, você receberá a lista dos laboratórios que irão compor o exame e a nota do aluno nesses laboratórios. A nota final neste caso será dada por:
    - **Nota Final = mínimo{5, (média ponderada dos laboratórios + média ponderada do exame) / 2}**

Caso a **Nota Final** seja **maior ou igual** a **5,0**, o aluno estará **aprovado**. **Caso contrário**, o aluno estará **reprovado**.

O seu programa irá receber um inteiro **N**, seguido por **N** linhas representando as notas obtidas nos laboratórios e por **N** linhas representando os pesos de cada atividade. **Caso o aluno tenha ficado de exame**, o programa deverá receber um inteiro **M**, seguido por **M** linhas representando **quais pesos dos laboratórios serão utilizados no exame** e por **M** linhas indicando a nota de cada laboratório durante o exame.

A **saída** deve informar a média ponderada dos laboratórios, a situação do aluno ("Aprovado por nota", "Reprovado por nota", "Aprovado no exame" ou "Reprovado no exame") e a nota final, apresentadas da seguinte forma:

*Media laboratorios: <Média ponderada dos laboratórios>Situacao: <Situação do aluno>Nota final: <Nota final>*

Tanto a média ponderada dos laboratórios quanto a nota final deverão ser formatadas com um dígito após a vírgula.

Exemplos de entradas e saídas esperadas pelo seu programa:

### **Teste 01**

- **Entrada:**

    ```python
    10
    10.0
    9.0
    8.0
    7.0
    6.0
    5.0
    4.0
    3.0
    2.0
    1.0
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    ```

- **Saída:**

    ```python
    Media laboratorios: 5,5

    Situacao: Aprovado por nota

    Nota final: 5,5
    ```

### **Teste 02**

- **Entrada:**

    ```python
    10
    5.0
    5.0
    8.0
    7.0
    6.0
    5.0
    4.0
    3.0 
    2.0
    1.0
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    2
    3
    4
    10.0
    10.0
    ```

- **Saída:**

    ```python
    Media laboratorios: 4,6
    Situacao: Aprovado no exame
    Nota final: 5,0
    ```

### **Teste 03**

- **Entrada:**

    ```python
    5
    10.0
    6.5
    5.5
    2.0
    1.0
    1
    1
    1
    3
    4
    2
    4
    5
    5.0
    5.0
    ```

- **Saída:**

    ```python
    Media laboratorios: 3,2
    Situacao: Reprovado no exame
    Nota final: 4,1
    ```