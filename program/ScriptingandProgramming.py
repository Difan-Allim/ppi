import bpy
def create_cube():
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(0,0,0))
class CubeCreator:
    def __init__(self, name):
        self.name = name
    
    def create(self):
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(0,0,0))
        bpy.context.object.name = self.name
my_cube = CubeCreator("MyCube")
my_cube.create()
