import random

bd = {'Alunos': {},
      'Materias': {}}


def showAlunos():
    print(f'|{"Alunos":^50}|')
    print(f'-'*52)

    for ra in bd['Alunos']:
        print('')
        aluno = bd['Alunos'][ra]
        keys_aluno = list(aluno.keys())
        notas_head = f'{"Código":^8}|{"Nota":^6}|' * len(aluno[keys_aluno[2]])
        nome = aluno[keys_aluno[0]]
        x = len(nome)+6
        print(
            f'{"RA":^10}| {"Nome":^{x}}| {"NumDisc":^10}|{notas_head}', end='')
        print()
        print(
            f'{ra:^10}  {nome:^{x}}{" "*4}{aluno[keys_aluno[1]]:<10}', end='')
        for cod_mat in aluno[keys_aluno[2]]:
            nota = list(aluno[keys_aluno[2]][cod_mat].values())[0]
            print(f'{cod_mat:^8}{nota:^6}{" "*2}', end='')
        print()


def showMaterias():
    print()
    print(bd['Materias'])
    return


def generateCode(size: int):
    code = ''
    for i in range(size):
        code += str(random.randint(0, 9))
    return code


def createAluno(name: str):
    ra = generateCode(8)
    aluno = {
        'nome': name,
        'NumDisc': 0,
        'notas': {}}
    bd['Alunos'][ra] = aluno
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
        bd['Alunos'][ra_aluno]['NumDisc'] = len(
            bd['Alunos'][ra_aluno]['notas'].values())
        print(bd['Alunos'][ra_aluno])
    else:
        print('Codigo de Materia Não Encontrado')


def removeNotaAluno():
    ra_aluno = str(input('Ra aluno: '))
    cod_materia = str(input('Cod Materia: '))
    if cod_materia in bd['Alunos'][ra_aluno]['notas']:
        bd['Alunos'][ra_aluno]['notas'].pop(cod_materia)
        print(bd['Alunos'][ra_aluno])
    else:
        print('Codigo da Materia não encontrado')


def execOptions(op: str = 1):
    if op == '1':
        addNotaAluno()
    elif op == '2':
        removeNotaAluno()
    else:
        print('opção invalida')


createAluno('Guilherme Domingos dos Santos')
createAluno('Gui')
createMateria('Historia')
createMateria('Geografia')
createMateria('Geografia')
createMateria('Geografia')
while True:
    try:
        showAlunos()
        showMaterias()
        op = str(input('Digite oque deseja fazer: '))
        if op == 'end':
            break
        execOptions(op)

    except:
        print('Erro')
        break

# showAlunos()
