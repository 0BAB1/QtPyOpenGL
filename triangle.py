import sys
from OpenGL.GL import *
import numpy as np

class Triangle:
    
    def __init__(self):
        #x y z r g b
        self.vertices = (
            -1, -1, 0, 1, 0, 0,
            1, -1, 0, 0, 1, 0,
            0, 1, 0, 0, 0, 1
        )
        
        self.vertices = np.array(self.vertices, dtype=np.float32)
        self.vertex_count = 3
        
        #set up va and vbo. vbo in vao
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        
        # describe vbo content
        glEnableVertexAttribArray(0) # location = 0
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0)) #pos
        glEnableVertexAttribArray(1) # location = 1
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12)) #color
        
    def destroy(self):
        """free the memory !"""
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))