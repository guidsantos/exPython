import random

bd = {'Alunos': {},
      'Materias': {}}


def generateCode(size: int):
    code = ''
    for i in range(size):
        code += str(random.randint(0, 9))
    return code


def createAluno(name: str):
    aluno = {
        'nome': name,
        'NumDisc': 0,
        'notas': {}}
    bd['Alunos'][generateCode(8)] = aluno
    return


def createMateria(grade_name: str):
    new_grade = {
        'nome': grade_name}
    bd['Materias'][generateCode(5)] = new_grade
    return


def addNotaAluno():
    ra_aluno = str(input('Ra aluno: '))
    cod_materia = str(input('Cod Materia: '))
    if cod_materia in bd['Materias']:
        nota = float(input('Digite a nota: '))
        bd['Alunos'][ra_aluno]['notas'][cod_materia] = {
            'nota': f'{nota:.1f}'
        }
        print(bd['Alunos'][ra_aluno])
    else:
        print('Codigo de Materia Não Encontrado')


def execOptions(op: str):
    if op == '1':
        addNotaAluno()
    else:
        print('opção invalida')


createAluno('Guilherme')
createAluno('Gui')
createMateria('Historia')
createMateria('Geografia')

while True:
    try:
        input()
        print()
        print(bd['Alunos'])
        print()
        print(bd['Materias'])
        op = str(input('Digite oque deseja fazer: '))
        if op == 'end':
            break
        execOptions(op)

    except:
        print('Erro')
        continue
