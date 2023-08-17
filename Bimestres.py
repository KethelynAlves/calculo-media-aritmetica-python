nome = input ("Digite o nome do aluno: ")
bim1 = float (input ("DIgite a nota do 1° Bimestre: "))
bim2 = float (input ("DIgite a nota do 2° Bimestre: "))
bim3 = float (input ("DIgite a nota do 3° Bimestre: "))
bim4 = float (input ("DIgite a nota do 4° Bimestre: "))
media = float ((bim1+bim2+bim3+bim4)/4)

print (f"A média do(a) aluno(a) é de: {media}")
if media >=9:
    print(f"O(A) aluno(a) {nome} esta aprovado com louvor!")
elif media >=7:
    print (f"O(A) aluno(a) {nome} esta aprovado.")
elif media <7:
    print(f"O(A) aluno(a) {nome} esta reprovado.")