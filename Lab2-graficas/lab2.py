from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, greyscale, hologram, invertedcolor, randomstatic, unlit, gourad, toon, glow, textureBlend, pinkjelly, toongreyscale, heatmap

width = 960
height = 540

rend = Renderer(width, height)

rend.dirLight = V3(1, 0, 0)

rend.active_texture = Texture("model.bmp")
rend.active_shader = greyscale

rend.glLoadModel("model.obj",
                 translate = V3(-8, -2, -10),
                 scale = V3(2,2,2),
                 rotate = V3(0,0,0))
rend.active_shader = hologram

rend.glLoadModel("model.obj",
                 translate = V3(-4, 3, -10),
                 scale = V3(2,2,2),
                 rotate = V3(0,0,0))

rend.active_shader = invertedcolor

rend.glLoadModel("model.obj",
                 translate = V3(0, 3, -10),
                 scale = V3(2,2,2),
                 rotate = V3(0,0,0))

rend.active_shader = randomstatic

rend.glLoadModel("model.obj",
                 translate = V3(4, -1, -10),
                 scale = V3(2,2,2),
                 rotate = V3(0,0,0))

#rend.active_texture = Texture("models/model.bmp")
#rend.active_shader = gourad
#rend.glLoadModel("models/model.obj",
#                 translate = V3(-4, 0, -10),
#                 scale = V3(3,3,3),
#                 rotate = V3(0,0,0))

#rend.active_shader = toon
#rend.glLoadModel("models/model.obj",
#                 translate = V3(0, 0, -10),
#                 scale = V3(3,3,3),
#                 rotate = V3(0,0,0))

#rend.active_shader = glow
#rend.glLoadModel("models/model.obj",
#                 translate = V3(4, 0, -10),
#                 scale = V3(3,3,3),
#                 rotate = V3(0,0,0))



rend.glFinish("output.bmp")
