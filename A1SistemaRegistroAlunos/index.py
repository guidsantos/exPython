import os

# Feito Por:
# GUILHERME DOMINGOS DOS SANTOS
# JOÃO MARCOS RANUZZI RIBEIRO


def showOptions(menu: str = 'menu'):
    if menu == 'menu':
        print()
        print('Menu')
        print('-'*20)
        print('1 - Adicionar Alunos')
        print('2 - Modificar Nota')
        print('3 - Excluir um Aluno')
        print('4 - Relatórios')
        print('0 - Fechar programa')
        print('-'*20)
    elif menu == 'report':
        print()
        print('Relatórios')
        print('1 - Imprimir Dados de um Aluno')
        print('2 - Lista de Todos os Alunos')
        print('3 - Voltar ao Menu Principal')
        print('0 - Fechar o Programa')


def showStudent(student: list, op='all'):
    if op == 'all':
        print(f'\nRA: {student[0]} Nome: {student[1]}  Nota: {student[2]}')
    elif op == 'grade':
        print(f'Nota: {student[2]}')


def showAllStudents(students: list):
    try:
        print('\nLista de Alunos')
        for student in students:
            showStudent(student)
        input('\nPressione Enter para voltar ao menu')
        os.system('cls')
    except:
        print('Erro Informação inválida')


def showStudentGradeByRA(RA: str, students: list):
    studentExists = False
    for student in students:
        if student[0] == RA:
            studentExists = True
            indexStudent = students.index(student)
    if studentExists == True:
        showStudent(students[indexStudent], op='grade')
    elif studentExists == False:
        print('O Aluno não foi encontrado')


def readStudent(students: list):
    running = True
    print('\nInsira os nomes e notas dos alunos')
    while True:
        try:
            print(
                '--Para finalizar o Cadastro de Alunos digite end no RA--\n')
            studentInfo = []
            while True:
                validRA = True
                studentRA = str(input('Digite o RA: '))
                if studentRA == 'end':
                    print('Cadastro de alunos Concluído')
                    os.system('cls')
                    running = False
                    break
                elif studentRA != '':
                    for student in students:
                        if student[0] == studentRA:
                            os.system('cls')
                            print(
                                '--Para finalizar o Cadastro de Alunos digite end no RA--\n')
                            print('Este RA já existe tente novamente')
                            validRA = False
                            break
                    if validRA == True:
                        studentInfo.append(studentRA)
                        break
                    elif validRA == False:
                        continue
                else:
                    os.system('cls')
                    print(
                        '--Para finalizar o Cadastro de Alunos digite end no RA--\n')
                    print('Digite um RA válido')
                    continue
            if running == False:
                break
            studentName = str(input('Digite o nome do Aluno: '))
            studentInfo.append(studentName)
            studentGrade = float(input('Digite a nota do Aluno: '))
            os.system('cls')
            studentInfo.append(f'{studentGrade:.1f}')
            students.append(studentInfo)
        except:
            print('Inseriu uma informação inválida tente novamente')
            continue
    return students


def editStudentName(RA: str, students: list):
    studentExists = False
    for student in students:
        if student[0] == RA:
            studentExists = True
            indexStudent = students.index(student)

    if studentExists == True:
        showStudent(students[indexStudent])
        confirmacao = str(input('Deseja alterar o nome deste Aluno (s/n): '))
        if confirmacao == 's':
            students[indexStudent][1] = str(input('\nDigite o novo Nome:'))
            os.system('cls')
            showStudent(students[indexStudent])
        else:
            os.system('cls')
    elif studentExists == False:
        print('Aluno não encontrado')


def editStudentGrade(RA: str, students: list):
    studentExists = False
    for student in students:
        if student[0] == RA:
            studentExists = True
            indexStudent = students.index(student)
    if studentExists == True:
        showStudent(students[indexStudent])
        confirmacao = str(input('Deseja alterar a Nota deste Aluno (s/n): '))
        if confirmacao == 's':
            newGrade = float(input('\nDigite a nova Nota:'))
            students[indexStudent][2] = f'{newGrade:.1f}'
            os.system('cls')
            showStudent(students[indexStudent])
        else:
            os.system('cls')
    elif studentExists == False:
        print('Aluno não encontrado')


def executeOptions(option: str, students: list):
    if option == '1':
        RA = str(input('Digite o RA do Aluno que deseja visualizar a nota: '))
        showStudentGradeByRA(RA, students)
    elif option == '2':
        RA = str(input('Digite o RA do Aluno que seja alterar: '))
        editStudentGrade(RA, students)
    elif option == '3':
        RA = str(input('Digite o RA do Aluno que seja alterar: '))
        editStudentName(RA, students)
    elif option == '':
        showAllStudents(students)
    elif option == '5':
        readStudent(students)


os.system('cls')
print()
studentsList = []
# readStudent(studentsList)
print()
menu = 'menu'
while True:
    # try:
    showOptions(menu)
    op = str(input('Insira o que deseja fazer: '))
    if op == '0':
        os.system('cls')
        print('\nPrograma Encerrado')
        break
    elif menu == 'menu' and op == '4':
        menu = 'report'
    print(menu)
    os.system('cls')
    # executeOptions(op, studentsList)

    # except:
    #     print('Informação invalida')
    #     continue
