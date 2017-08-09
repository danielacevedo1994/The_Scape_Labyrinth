from datetime import datetime ,date, time

print("Fecha actual: ", date.today())
print ("Fecha y hora actual: ",datetime.now())
print("Hora actual: ", datetime.now().hour)
print ("Minutos actuales: ", datetime.now().minute)
print("Segundos: ", datetime.now().second)



def creartxt(): ## se crea un archivo txt para guardar los puntajes
    nuevo = open('timer.txt','a')
    nuevo.write("Tiempo transcurrido: " + time.strptime(datetime.now()))
    nuevo.close()

creartxt()
