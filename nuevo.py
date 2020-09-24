import numpy.random as ran
llegada= 1   #1er tipo de evento
salida= 0    #2do tipo de evento

tiempo_entre_llegadas= 2 #aprox
tiempo_atencion_medica= 30   #aprox
total_de_pacientes= 500    #poner cantidad de pacientes diarios aprox
pacientes_en_espera=  60   #capacidad de salas de espera

#inicializar 
reloj=0
eventos=[(llegada,ran.exponential(tiempo_entre_llegadas))]  #[lista de tuplas ]
pacientes_en_espera= 100
Box_ocupado=False #box de atención médica desocupado

#declarar variables
pacientes=[pacientes_en_espera]    # guardo la cantidad de pacientes en la sala de espera en todo momento
tiempo=[reloj]   
Box=[Box_ocupado]


for i in range(total_de_pacientes):
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
    elif eventos[0][0] ==salida:
        eventos.pop(0)
        if pacientes_en_espera > 0:
            Box_ocupado=True
            pacientes_en_espera-=1
            eventos.append((salida,reloj + ran.exponential(tiempo_atencion_medica)))
            eventos.sort(key=lambda tup: tup[1])
        else:
            Box_ocupado=False
    tiempo.append(reloj)
    pacientes.append(pacientes_en_espera)
    Box.append(Box_ocupado)

report=open("report.csv","w")
for tiempo, cas, cli in zip(tiempo,Box,pacientes):
   report.write(f"{tiempo},{cas},{cli}\n")
report.close()
print ("LISTO!")

