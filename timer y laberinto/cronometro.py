#definir las variables globales
import simplegui

counter = 0
points = 0
tries = 0
running = False

def format(t):
    D = str(t%10)
    t //= 10
    C = str(t%10)
    t //= 10
    B = str(t % 6)
    t //= 6
    A = str(t % 10)
    
    return A + ':' + B + C + '.' + D
    
# definimos los eventos por botones; "Iniciar", "Detener", "Reinicio"
def start_handler():
    global running
    running = True
    timer.start()

def stop_handler():
    global running, tries, points
    
    timer.stop()
    
    if running:
        tries += 1
        
        if counter % 10 == 0:
            points += 1
    
    running = False
    
def reset_handler():
    stop_handler()
    global running, tries, points, counter
    runnig = False
    tries = 0
    points = 0
    counter = 0

# definir un evento manejado por tiempo
def tick():
    global counter
    counter += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(str(points) + '/' + str(tries),
                    (225, 30), 30, 'Green')
    canvas.draw_text(format(counter), (75, 160), 60, 'Red')
 

# creacion del frame
frame = simplegui.create_frame('Stopwatch!!', 300, 300)
timer = simplegui.create_timer(100, tick)

# registrar los eventos handlers
frame.add_button('Iniciar', start_handler)
frame.add_button('Detener', stop_handler)
frame.add_button('Reiniciar', reset_handler)
frame.set_draw_handler(draw)

# inicializar el frame
frame.start()
