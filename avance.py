import numpy.random as ran
llegada= 1
salida= 0

tiempo_entre_llegadas=     #aprox
tiempo_atencion_medica=     #aprox
total_de_pacientes=      #poner cantidad de pacientes diarios aprox
pacientes_en_espera=      #capacidad de salas de espera

#inicializar 
reloj=0
eventos=[(llegada,ran.exponential(tiempo_entre_llegadas))]
pacientes_en_espera=
Box_ocupado=False #box de atención médica

#declarar variables
pacientes=[pacientes_en_espera]
tiempo=[reloj]
Box=[Box_ocupado]


for paciente in range(total_de_pacientes):
    reloj= eventos[0][1]
    if eventos[0][0]==llegada:
        eventos.pop(0)
        eventos.append((llegada,reloj + ran.exponential(tiempo_atencion_medica)))
        pacientes_en_espera+=1
        if Box_ocupado==False:
            pacientes_en_espera-=1
            Box_ocupado=True
            eventos.append((salida,reloj + ran.exponential(tiempo_atencion_medica)))
        eventos.sort(key=lambda tup: tup[1])
    elif eventos[0][0] ==llegada:
        eventos.pop(0)
        if pacientes_en_espera > 0:
            Box_ocupado=True
            pacientes_en_espera-=1
            eventos.append((llegada,reloj + ran.exponential(tiempo_atencion_medica)))
            eventos.sort(key=lambda tup: tup[1])
        else:
            Box_ocupado=False
    tiempo.append(reloj)
    pacientes.append(pacientes_en_espera)
    Box.append(Box_ocupado)

report
report=open("report.csv","w")
for tiempo, cas, cli in zip(tiempo,box,pacientes):
   report.write(f"{tiempo},{cas},{cli}+\n")
report.close()
<<<<<<< HEAD


#PROBANDO
=======
jsdjksad
>>>>>>> fd0d099e84fb17dc09c7b3a7c7f150c831ed273c
