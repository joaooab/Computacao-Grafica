from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# GLfloat angle, fAspect
ASPECTO, ANGULO = (0, 0)
x_ini, y_ini, bot = (0, 0, 0)
obsX, obsY, obsZ, rotX, rotY = (0, 0, 0, 0, 0)
obsX_ini, obsY_ini, obsZ_ini, rotX_ini, rotY_ini = (0, 0, 0, 0, 0)
escalaX, escalaY, escalaZ = (0, 0, 0)

SENS_ROT = 10.0
SENS_OBS = 10.0
SENS_TRANS = 10.0

def Desenha():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix()
    glColor3f(0.9, 0.9, 0.9)
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 300.0, 0.0)
    glEnd()

    glPopMatrix()

    glPushMatrix()
    glColor3f(0.9, 0.9, 0.9)
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(300.0, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.9, 0.9, 0.9)
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 300.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    glTranslatef(20.0, 0.0, 0.0)
    glutSolidSphere(1, 50, 50)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.0, 1.0, 0.0)
    glTranslatef(0.0, 20.0, 0.0)
    glutSolidSphere(1, 50, 50)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.0, 0.0, 1.0)
    glTranslatef(0.0, 0.0, 20.0)
    glutSolidSphere(1, 50, 50)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.0, 1.0, 1.0)
    glTranslatef(0.0, 20.0, 20.0)
    glutSolidSphere(1, 50, 50)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1.0, 1.0, 0.0)
    glTranslatef(20.0, 20.0, 0.0)
    glutSolidSphere(1, 50, 50)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1.0, 0.0, 1.0)
    glTranslatef(20.0, 0.0, 20.0)
    glutSolidSphere(1, 50, 50)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glTranslatef(20.0, 20.0, 20.0)
    glutSolidSphere(1, 50, 50)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.0, 0.0, 0.0)
    glutSolidSphere(1, 50, 50)
    glPopMatrix()

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glPushMatrix()
    glColor4f(0.99, 0.99, 0.99, 0.099)
    glBegin(GL_QUADS)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(20.0, 0.0, 0.0)
    glVertex3f(20.0, 20.0, 0.0)
    glVertex3f(0.0, 20.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glColor4f(0.99, 0.99, 0.99, 0.099)
    glBegin(GL_QUADS)
    glVertex3f(0.0, 0.0, 20.0)
    glVertex3f(20.0, 0.0, 20.0)
    glVertex3f(20.0, 20.0, 20.0)
    glVertex3f(0.0, 20.0, 20.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glColor4f(0.99, 0.99, 0.99, 0.099)
    glBegin(GL_QUADS)
    glVertex3f(0.0, 20.0, 0.0)
    glVertex3f(20.0, 20.0, 0.0)
    glVertex3f(20.0, 20.0, 20.0)
    glVertex3f(0.0, 20.0, 20.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glColor4f(0.99, 0.99, 0.99, 0.099)
    glBegin(GL_QUADS)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(20.0, 0.0, 0.0)
    glVertex3f(20.0, 0.0, 20.0)
    glVertex3f(0.0, 0.0, 20.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glColor4f(0.99, 0.99, 0.99, 0.099)
    glBegin(GL_QUADS)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 20.0, 0.0)
    glVertex3f(0.0, 20.0, 20.0)
    glVertex3f(0.0, 0.0, 20.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glColor4f(0.99, 0.99, 0.99, 0.099)
    glBegin(GL_QUADS)
    glVertex3f(20.0, 0.0, 0.0)
    glVertex3f(20.0, 20.0, 0.0)
    glVertex3f(20.0, 20.0, 20.0)
    glVertex3f(20.0, 0.0, 20.0)
    glEnd()
    glPopMatrix()

    glutSwapBuffers()

    pass


def Inicializa():
    luzAmbiente = [0.2, 0.2, 0.2, 1.0]
    luzDifusa = [0.7, 0.7, 0.7, 1.0]  # Cor
    luzEspecular = [1.0, 1.0, 1.0, 1.0]  # Brilho
    posicaoLuz = [0.0, 20.0, 20.0, 1.0]

    # Capacidade de brilho do material
    especularidade = [1.0, 1.0, 1.0, 1.0]
    especMaterial = 60

    # Especifica que a cor de fundo da janela será preta
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Habilita modelo de colorização de Gouraud
    glShadeModel(GL_SMOOTH)

    # Define a refletância do material
    glMaterialfv(GL_FRONT, GL_SPECULAR, especularidade)

    # Define a concentração do brilho
    glMateriali(GL_FRONT, GL_SHININESS, especMaterial)

    # Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)

    # Define os parâmetros da luz de número 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa)
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular)
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz)

    # Habilita a definição da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL)
    # Habilita o uso de iluminação
    glEnable(GL_LIGHTING)
    # Habilita a luz de número 0
    glEnable(GL_LIGHT0)
    # Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST)

    # angle=45
    ANGULO = 45
    rotX = rotY = 0
    obsX = obsY = 0
    obsZ = 60  # Voltar para 10
    escalaX = escalaY = escalaZ = 1

    pass


# Função usada para especificar o volume de visualização
def EspecificaParametrosVisualizacao():  # equivalente ao posiciona observador{
    # Especifica sistema de coordenadas de projeção
    glMatrixMode(GL_PROJECTION)
    # Inicializa sistema de coordenadas de projeção
    glLoadIdentity()

    # Especifica a projeção perspectiva
    # gluPerspective(angle,fAspect,0.4,500)
    gluPerspective(ANGULO, ASPECTO, 0.4, 500)

    # Especifica sistema de coordenadas do modelo
    glMatrixMode(GL_MODELVIEW)
    # Inicializa sistema de coordenadas do modelo
    glLoadIdentity()

    # Especifica posição do observador e do alvo
    # gluLookAt(0,80,200, 0,0,0, 0,1,0)
    # gluLookAt(obsX, obsY, obsZ, 0,0,0, 0,1,0)
    glTranslatef(-obsX, -obsY, -obsZ)  # Translata a cÃ¢mera para essas variaveis*/
    glRotatef(rotX, 1, 0, 0)  # Rotacionar a camera para essas coordenadas*/
    glRotatef(rotY, 0, 1, 0)
    pass


# Função callback chamada quando o tamanho da janela é alterado
def AlteraTamanhoJanela(w, h):

    # Para previnir uma divisão por zero
    if (h == 0):
        h = 1

    # Especifica o tamanho da viewport
    glViewport(0, 0, w, h)

    # Calcula a correção de aspecto
    # fAspect = (GLfloat)w/(GLfloat)h
    ASPECTO = w / h

    EspecificaParametrosVisualizacao()
    pass

# Função callback chamada para gerenciar eventos do mouse
def GerenciaMouse(button, state, x, y):
    # if (button == GLUT_LEFT_BUTTON)
    # 	if (state == GLUT_DOWN) {  # Zoom-in
    # 		if (angle >= 10) angle -= 5
    # 	}
    # if (button == GLUT_RIGHT_BUTTON)
    # 	if (state == GLUT_DOWN) {  # Zoom-out
    # 		if (angle <= 130) angle += 5
    # 	}
    if (state == GLUT_DOWN):
        x_ini = x
        y_ini = y
        obsX_ini = obsX
        obsY_ini = obsY
        obsZ_ini = obsZ
        rotX_ini = rotX
        rotY_ini = rotY
        bot = button
    else:
        bot = -1
    EspecificaParametrosVisualizacao()
    glutPostRedisplay()
    pass


def motion(x, y):
    if (bot == GLUT_LEFT_BUTTON):
        # Rotação
        deltaX = x_ini - x
        deltaY = y_ini - y
        rotX = rotX_ini - deltaY / SENS_ROT
        rotY = rotY_ini - deltaX / SENS_ROT
    elif (bot == GLUT_RIGHT_BUTTON):  # Zoom
        deltaZ = y_ini - y
        obsZ = obsZ_ini + deltaZ / SENS_OBS
    elif (bot == GLUT_MIDDLE_BUTTON):  # Correr
        deltaX = x_ini - x
        deltaY = y_ini - y
        obsX = obsX_ini + deltaX / SENS_TRANS
        obsY = obsY_ini + deltaY / SENS_TRANS
    EspecificaParametrosVisualizacao()
    glutPostRedisplay()
    pass


# Programa Principal
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Teste")
    glutDisplayFunc(Desenha)
    glutReshapeFunc(AlteraTamanhoJanela)
    glutMouseFunc(GerenciaMouse)
    glutMotionFunc(motion)
    Inicializa()
    glutMainLoop()
    pass

main()