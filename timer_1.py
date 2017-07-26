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


if __name__ == "__main__":
    timer()
