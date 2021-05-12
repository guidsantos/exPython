def readStudent():
    students = []
    print('Insira os nomes e notas dos alunos')
    while True:
        try:
            studentInfo = []
            studentName = str(
                input('Digite o nome do Aluno (Para finalizar insira end): '))
            if studentName == 'end':
                break
            studentInfo.append(studentName)
            studentGrade = float(input('Digite a nota do Aluno: '))
            studentInfo.append(f'{studentGrade:.1f}')
            students.append(studentInfo)
        except:
            print('Inseriu uma informação inválida tente novamente')
            continue
    return students


def calcAverage(students: list):
    try:
        grades = []
        gradesSum = 0
        for student in students:
            grades.append(float(student[1]))
        for grade in grades:
            gradesSum += grade
        averageGrade = gradesSum/len(grades)
        return averageGrade
    except:
        print('Erro Informações invalidas')
        return


def showStudentsAboveAverage(averageGrade: float, students: list):
    try:
        print('Alunos com notas iguais ou acima da média')
        print(f'Média da sala = {averageGrade:.1f}\n')
        for student in students:
            if float(student[1]) >= averageGrade:
                print(f'Nome: {student[0]}  Nota: {student[1]}')
    except:
        print('Erro Informação invalida')


print()
studentsList = readStudent()
averageGrade = calcAverage(studentsList)
print()
showStudentsAboveAverage(averageGrade, studentsList)
print()
