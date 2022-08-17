# Estefania Elvira 
# Ejercicio 4
# Fecha 08/08/22



from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, gourad

# Dimensiones
width = 960
height = 540

# Instancia del renderer
rend = Renderer(width, height)

rend.active_shader = flat
rend.active_texture = Texture("model.bmp")

rend.glLoadModel("FinalBaseMesh.obj",
                 translate = V3(width/2, height/2, 0),
                 rotate = V3(0, 180, 0),
                 scale= V3(15, 15, 15))

# Salida
rend.glFinish("nada.bmp")

