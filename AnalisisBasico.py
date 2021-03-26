# -*- coding: utf-8 -*-
"""
@author: Ricardo Alonso
"""

#Declaración de Datos

a1 = ["Pedro", "Economía", "Economía I", 10]
a2 = ["Pedro", "Economía", "Cálculo I", 9]
a3 = ["Pedro", "Economía", "Problemas I", 8]
a4 = ["Pedro", "Economía", "Problemas II", 6]
a5 = ["Pedro", "Economía", "Álgebra I", 7]
a6 = ["Pedro", "Economía", "Contabilidad I", 9]
a7 = ["Pedro", "Economía", "Minería de Datos", 8]
a8 = ["Cecilia", "Contabilidad", "Ideas I", 6]
a9 = ["Cecilia", "Contabilidad", "Ideas II", 8]
a10 = ["Cecilia", "Contabilidad", "Contabilidad I", 9]
a11 = ["Cecilia", "Contabilidad", "Cálculo I", 6]
a12 = ["Cecilia", "Contabilidad", "Cálculo II", 9]
a13 = ["Irma", "Computación", "Cálculo I", 10]
a14 = ["Irma", "Computación", "Álgebra I", 10]
a15 = ["Irma", "Computación", "Cálculo II", 10]
datos = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15]

#Ordenamiento de Datos

Alumnos = []
Carreras = {}
Calificaciones = {}
nombre = datos[0][0]

for i in range(len(datos)):
    nombre = datos[i][0]
    if Alumnos.count(nombre) == 0:
        Alumnos.append(nombre)
        Carreras[nombre] = datos[i][1]
        califs = [[datos[i][2]],[datos[i][3]]]
        Calificaciones[nombre] = califs
    else:
        califs = Calificaciones.get(nombre)
        califs[0].append(datos[i][2])
        califs[1].append(datos[i][3])
        Calificaciones.update({nombre: califs})
    
#Ejercicios

print("#1 Las matérias que han cursado los alumnos")
for i in range(len(Alumnos)):
    print(Alumnos[i] + ":")
    for j in Calificaciones.get(Alumnos[i])[0]:
        print("\t" + j)
        
print("\n#2 Materia con la calificación más alta para cada alumno")
def Max(l):
    Max = []
    max = 0
    for i in range(len(l[1])):
        if l[1][i] > max:
            max = l[1][i]
            Max.clear()
            Max.append(l[0][i])
        elif l[1][i] == max:
            Max.append(l[0][i])
    return Max
        
for i in range(len(Alumnos)):
    print("\t" + Alumnos[i] + ": " + ", ".join(Max(Calificaciones[Alumnos[i]])))
    
print("\n#3 El nombre del alumno que ha cursado más materias")
MA = Alumnos[0]
for i in range(len(Alumnos)):
    if len(Calificaciones[Alumnos[i]][0]) > len(Calificaciones[MA][0]):
        MA = Alumnos[i]
print("\t" + MA)

print("\n#4 El nombre del alumno que ha cursado menos materias")
PA = Alumnos[0]
for i in range(len(Alumnos)):
    if len(Calificaciones[Alumnos[i]][0]) < len(Calificaciones[PA][0]):
        PA = Alumnos[i]
print("\t" + PA)

print("\n#5 Promedio para cada una de las materias")
Materias = [[],[],[]]
for i in range(len(Alumnos)):
    for j in range(len(Calificaciones[Alumnos[i]][0])):
        if Materias[0].count(Calificaciones[Alumnos[i]][0][j]) == 0:
            Materias[0].append(Calificaciones[Alumnos[i]][0][j])
            Materias[1].append(Calificaciones[Alumnos[i]][1][j])
            Materias[2].append(1)
        else:
            k = Materias[0].index(Calificaciones[Alumnos[i]][0][j])
            Materias[1][k] = Materias[1][k] + Calificaciones[Alumnos[i]][1][j]
            Materias[2][k] = Materias[2][k]+1

for i in range(len(Materias[0])):
    print("\t" + Materias[0][i] + ": %2.1f"%(Materias[1][i]/Materias[2][i]))
        
print("\n#6  El nombre de la materia que mejor promedio tiene")
MM = Materias[0][0]
MP = Materias[1][0]/Materias[2][0]
for i in range(len(Materias[0])):
    if Materias[1][i]/Materias[2][i] > MP:
        MM = Materias[0][i]
        MP = Materias[1][i]/Materias[2][i]
print("\t" + MM)

print("\n#7  El nombre de la materia que peor promedio tiene")
PM = Materias[0][0]
PP = Materias[1][0]/Materias[2][0]
for i in range(len(Materias[0])):
    if Materias[1][i]/Materias[2][i] < PP:
        PM = Materias[0][i]
        PP = Materias[1][i]/Materias[2][i]
print("\t" + PM)

print("\n#8  La materia más cursada")
MMC = Materias[0][0]
NA = Materias[2][0]
for i in range(len(Materias[0])):
    if Materias[2][i] > NA:
        MMC = Materias[0][i]
        NA = Materias[2][i]
print("\t" + MMC)

print("\n#9 La materia menos cursada")
MmC = Materias[0][0]
NA = Materias[2][0]
for i in range(len(Materias[0])):
    if Materias[2][i] < NA:
        MmC = Materias[0][i]
        NA = Materias[2][i]
print("\t" + MmC)

print("\n#10 Los nombres de los alumnos")
for i in range(len(Alumnos)):
    print("\t" + Alumnos[i])
    
      
print("\n#1.Extra Las materias que han curasdo en común")
MC = set(Calificaciones[Alumnos[0]][0])
for i in range(len(Alumnos)):
    MC = MC & set(Calificaciones[Alumnos[i]][0])
print("\t" + ", ".join(MC))
