import time
s=0
m=0
def timer():
    global s
    global m
    while True:
        print (str(m)+":"+str(s))
        s=s+1
        if(s>=60):
            s=0
            m=m+1
        time.sleep(1)
        creartxt()
        grabartxt(s,m)


#if __name__ == "__main__":

def creartxt(): ## se crea un archivo txt para guardar los puntajes
    nuevo = open('timer.txt','w')
    nuevo.close()
def grabartxt(s,m):
    nuevo = open('timer.txt','a')
    nuevo.write("Tiempo transcurrido: " +str(m)+":"+str(s)+"\n")
    nuevo.close()
timer()
