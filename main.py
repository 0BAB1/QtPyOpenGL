import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
from triangle import Triangle


class OpenGLWidget(QOpenGLWidget):
    def initializeGL(self):
        """called once whaen openGL context is set up"""
        glEnable(GL_DEPTH_TEST) #enable depth testing (objects in front obscurs the ones in the back)
        self.shader = self.createShader("shaders/vertex.txt", "shaders/fragment.txt")
        glUseProgram(self.shader)
        self.triangle = Triangle()

    def paintGL(self):
        """called whenever the widget needs to be redrawn, typically in response to a paint event"""
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #prepare for rendering the next frame.
        
        glUseProgram(self.shader) #best practice : get the right shader
        glBindVertexArray(self.triangle.vao) #we bing the tringale vao as the current one we xwant to get data from
        glDrawArrays(GL_TRIANGLES, 0, self.triangle.vertex_count) # get data from bound vao and draw it

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)

    def createShader(self, vertexFilePath, fragmentFilePath):
        
        with open(vertexFilePath, 'r') as f:
            vertex_src = f.readlines()
        
        with open(fragmentFilePath, 'r') as f:
            fragment_src = f.readlines()

        shader = compileProgram(
            compileShader(vertex_src, GL_VERTEX_SHADER),
            compileShader(fragment_src, GL_FRAGMENT_SHADER)    
        )
        
        return shader
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("PyQt OpenGL Example")

        # Create and set the OpenGL widget as the central widget
        self.opengl_widget = OpenGLWidget(self)
        self.setCentralWidget(self.opengl_widget)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    #exit sequence
    glDeleteProgram(window.opengl_widget.shader)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
