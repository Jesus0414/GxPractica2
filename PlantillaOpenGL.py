from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

def dibujarPasto():
    glColor3f(0.0,0.8,0.22)
    glBegin(GL_QUADS)
    glVertex3f(-1.0,-0.6,0.0)
    glVertex3f(1.0,-0.6,0.0)
    glVertex3f(1.0,-1.0,0.0)
    glVertex3f(-1.0,-1.0,0.0)
    glEnd()

def dibujarCirculo():
    glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 - 0.7 ,sin(angulo) * 0.15 + 0.7,0.0)
    glEnd()

def dibujarRayosLuz():
    glColor3f(1,0.4,0)
    glBegin(GL_TRIANGLE_STRIP)
    for x in range(90):
        angulo = x 
        glVertex3f(cos(angulo) * 0.2 - 0.7 ,sin(angulo) * 0.2 + 0.7,0.0)
    glEnd()


def dibujarNubes():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.1 - 0.2 ,sin(angulo) * 0.05 + 0.72,0.0)
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 + 0.3 ,sin(angulo) * 0.05 + 0.8,0.0)
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.1 + 0.2 ,sin(angulo) * 0.05 + 0.82,0.0)
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 + 0.6 ,sin(angulo) * 0.05 + 0.5,0.0)
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.1 + 0.4 ,sin(angulo) * 0.05 + 0.52,0.0)
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 - 0.3 ,sin(angulo) * 0.05 + 0.7,0.0)
    glEnd()

def dibujarTecho():
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.5,0.2,0.0)
    glVertex3f(0.0,0.7,0.0)
    glVertex3f(0.5,0.2,0.0)
    glEnd()

def dibujarEstructra():
    glColor3f(1.0,0.8,0.22)
    glBegin(GL_QUADS)
    glVertex3f(-0.4,-0.6,0.0)
    glVertex3f(0.4,-0.6,0.0)
    glVertex3f(0.4,0.3,0.0)
    glVertex3f(-0.4,0.3,0.0)
    glEnd()

def dibujarPuerta():
    glColor3f(0.5,0.5,0.5)
    glBegin(GL_QUADS)
    glVertex3f(-0.1,-0.6,0.0)
    glVertex3f(0.2,-0.6,0.0)
    glVertex3f(0.2,-0.2,0.0)
    glVertex3f(-0.1,-0.2,0.0)
    glEnd()

def dibujarPicaporte():
    glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 + 0.13 ,sin(angulo) * 0.04 - 0.4,0.0)
    glEnd()

def dibujarVentana():
    glColor3f(0.2,0.9,1.0)
    glBegin(GL_QUADS)
    glVertex3f(0.0,-0.1,0.0)
    glVertex3f(0.3,-0.1,0.0)
    glVertex3f(0.3,0.1,0.0)
    glVertex3f(0.0,0.1,0.0)

    glEnd()

def dibujarMarcos():
    glColor3f(1,0,0)
    glBegin(GL_QUADS)
    glVertex3f(-0.01,-0.11,0.0)
    glVertex3f(0.31,-0.11,0.0)
    glVertex3f(0.31,0.11,0.0)
    glVertex3f(-0.01,0.11,0.0)
    glEnd()

def dibujarMarcosint():
    glColor3f(1,0,0)
    glBegin(GL_QUADS)
    glVertex3f(0.14,-0.11,0.0)
    glVertex3f(0.16,-0.11,0.0)
    glVertex3f(0.16,0.11,0.0)
    glVertex3f(0.14,0.11,0.0)
    glEnd()

    glColor3f(1,0,0)
    glBegin(GL_QUADS)
    glVertex3f(-0.01,-0.0085,0.0)
    glVertex3f(0.31,-0.0085,0.0)
    glVertex3f(0.31,0.0085,0.0)
    glVertex3f(-0.01,0.0085,0.0)
    glEnd()

def dibujarArbol():
    glColor3f(0.7,0.3,0.1)
    glBegin(GL_QUADS)
    glVertex3f(-0.7,-0.6,0.0)
    glVertex3f(-0.5,-0.6,0.0)
    glVertex3f(-0.5,-0.2,0.0)
    glVertex3f(-0.7,-0.2,0.0)
    glEnd()

    glColor3f(0,1,0.5)
    glBegin(GL_POLYGON)                     
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 - 0.6 ,sin(angulo) * 0.15 - 0.15,0.0)
    glEnd()

    glColor3f(0,1,0.5)
    glBegin(GL_POLYGON)                     
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.68 ,sin(angulo) * 0.15 - 0.1,0.0)
    glEnd()

    glColor3f(0,1,0.5)
    glBegin(GL_POLYGON)                     
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 - 0.6 ,sin(angulo) * 0.15 + 0.07 ,0.0)
    glEnd()
    

def dibujar():
    #rutinas de dibujo
    dibujarPasto()
    dibujarRayosLuz()
    dibujarCirculo()
    dibujarEstructra()
    dibujarTecho()
    dibujarPuerta()
    dibujarPicaporte()
    dibujarMarcos()
    dibujarVentana()
    dibujarMarcosint()
    dibujarNubes()
    dibujarArbol()

def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(600,600,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,600,600)
        #Establece color de borrado
        glClearColor(0.2,0.78,1.0,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()