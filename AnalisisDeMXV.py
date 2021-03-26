# -*- coding: utf-8 -*-
"""
@author: Ricardo Alonso
"""

#Lector y escritor de archivos

import csv
excel = open("MXvideos.csv", mode='r', encoding="'iso-8859-1'")
txt = open("174759resultados.txt", mode='w')
reader = csv.reader(excel, delimiter=',')

#Clase Video

class Video:
    fecha = ""
    titulo = ""
    canal= ""
    vistas = 0
    likes = 0
    dislikes = 0
    comentarios = 0
    
    def __init__(self, id):
        self.id = id
        
    def __str__(self):
        s = self.id 
        s = s + " :- " + self.titulo
        s = s +"\n\t" + self.fecha
        s = s + "   " + self.canal
        s = s + "   " + str(self.likes)
        s = s + "   " + str(self.dislikes)
        return s
     
#Guardado de Datos
        
videos = []
for i in reader:
    if(i[0]=="video_id"):
        continue
    v = Video(i[0])
    v.titulo = i[2]
    v.canal = i[3]
    v.fecha = i[5][:10]
    v.vistas = int(i[7])
    v.likes = int(i[8])
    v.dislikes = int(i[9])
    v.comentarios = int(i[10])

    videos.append(v)
           
#Ejercicios
    
txt.writelines("#1 Video con más likes")
VML = videos[0]
ML = VML.likes
for i in range(len(videos)):
    if videos[i].likes > ML:
        VML = videos[i]
        ML = VML.likes
txt.writelines("\n\t" + str(VML))

txt.writelines("\n\n#2 Video con más dislikes")
VMD = videos[0]
MD = VMD.likes
for i in range(len(videos)):
    if videos[i].dislikes > MD:
        VMD = videos[i]
        MD = VMD.likes
txt.writelines("\n\t" + str(VMD))

txt.writelines("\n\n#3 Video con menos likes")
VML = videos[0]
ML = VML.likes
for i in range(len(videos)):
    if videos[i].likes < ML:
        VML = videos[i]
        ML = VML.likes
txt.writelines("\n\n\t" + str(VML))

txt.writelines("\n\n#4 Video con menos dislikes")
VMD = videos[0]
MD = VMD.likes
for i in range(len(videos)):
    if videos[i].dislikes < MD:
        VMD = videos[i]
        MD = VMD.likes
txt.writelines("\n\n\t" + str(VMD))

txt.writelines("\n\n#5 Videos con Trump en el título")
Trump = []
for i in range(len(videos)):
    if "Trump" in videos[i].titulo:
        Trump.append(videos[i].titulo)
txt.writelines("\n\n" + "\n\t-".join(Trump))

txt.writelines("\n\n#6 Numero de videos con Disney en el título")
Disney = 0
for i in range(len(videos)):
    if "Disney" in videos[i].titulo:
        Disney = Disney + 1
txt.writelines("\n\n\t" + str(Disney))

txt.writelines("\n\n#6 Número de comentarios de videos con Telenovela en el título")
Telenovela = 0
for i in range(len(videos)):
    if "Telenovela" in videos[i].titulo:
        Telenovela = Telenovela + videos[i].comentarios
txt.writelines("\n\n\t" + str(Telenovela))

    
txt.flush()
txt.close()
excel.close()
