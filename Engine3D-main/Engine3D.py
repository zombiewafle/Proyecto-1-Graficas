# Programa principal
from gl import Renderer, V3
from obj import Texture
from shaders import *

import random

width = 500
height = 500

rend = Renderer(width, height)

modelPos = V3(0, 0, -5)
rend.glLookAt(modelPos, V3(0, 0, 0))

rend.directional_light = V3(0,0,1)

rend.background = Texture('fondo.bmp')

rend.glClearBackground()

#Se aplica la textura y luego el efecto de estatica
rend.active_texture = Texture('textures/woodTower.bmp')
rend.active_texture2 = Texture('textures/woodTowerNormal.bmp')
rend.active_shader = static

rend.glLoadModel("models/watchtower.obj",
                 translate = V3(0, -4, -10),
                 scale = V3(0.5,0.5,0.5),
                 rotate = V3(0, 80, 0) )

#rend.active_texture = Texture('textures/watchTower.bmp')
#rend.active_texture2 = Texture('textures/watchTowerNormal.bmp')
#rend.active_shader = flat

#Arboles en la parte frontal
rend.active_shader = thermal
rend.glLoadModel("models/Sequoia_1.obj",
                 translate = V3(-5, -4, -10),
                 scale = V3(0.04,0.04,0.04),
                 rotate = V3(0, 80, 0) )

rend.glLoadModel("models/Sequoia_1.obj",
                 translate = V3(5, -4, -10),
                 scale = V3(0.04,0.04,0.04),
                 rotate = V3(0, 80, 0) )

rend.active_shader = static
rend.glLoadModel("models/Sequoia_2.obj",
                 translate = V3(3, -4, -10),
                 scale = V3(0.04,0.04,0.04),
                 rotate = V3(0, 80, 0) )

rend.glLoadModel("models/Sequoia_2.obj",
                 translate = V3(-3, -4, -10),
                 scale = V3(0.02,0.02,0.02),
                 rotate = V3(0, 80, 0) )

#Arboles en la parte trasera

rend.active_shader = inverseColors
rend.glLoadModel("models/Sequoia_2.obj",
                 translate = V3(1.5, -4, -15),
                 scale = V3(0.04,0.04,0.04),
                 rotate = V3(0, 80, 0) )


rend.glLoadModel("models/Sequoia_2.obj",
                 translate = V3(-1.5, -4, -15),
                 scale = V3(0.02,0.02,0.02),
                 rotate = V3(0, 80, 0) )

rend.glLoadModel("models/Sequoia_2.obj",
                 translate = V3(-2.5, -4, -15),
                 scale = V3(0.02,0.02,0.02),
                 rotate = V3(0, 80, 0) )

#Personaje
rend.active_shader = glow
rend.glLoadModel("models/character.obj",
                 translate = V3(0,-5,-9),
                 scale = V3(0.01,0.01,0.01),
                 rotate = V3(0, -150, 0) )     

#Cielo
rend.active_shader = wire
rend.glLoadModel("models/moon.obj",
                 translate = V3(-4, 4,-10),
                 scale = V3(0.5,0.5,0.5),
                 rotate = V3(0, -0, 0) )

rend.glFinish("output.bmp")
