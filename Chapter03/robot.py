import os
import bpy

version = bpy.app.version
assert version[0] == 2 and version[1] == 80, \
    f"This script is developed for Blender version 2.80. Currently running: {version[0]}.{version[1]}.{version[2]}"

def clean_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
def draw_base_plate():

    # cubes for cutting sides of base plate    
    bpy.ops.mesh.primitive_cube_add(size=0.05, location=(0.175,0,0.09))
    bpy.ops.mesh.primitive_cube_add(size=0.05, location=(-0.175,0,0.09))

    # base plate
    bpy.ops.mesh.primitive_cylinder_add(radius=0.15,depth=0.005, location=(0,0,0.09))
    
    # boolean difference modifier from first cube
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Cube"]
    bpy.ops.object.modifier_apply(modifier="Boolean")

    # booleab difference modifier from second cube
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Cube.001"]
    bpy.ops.object.modifier_apply(modifier="Boolean")

    # deselect cylinder and delete cubes
    bpy.ops.object.select_pattern(pattern="Cube")
    bpy.ops.object.select_pattern(pattern="Cube.001")
    bpy.data.objects['Cylinder'].select_set(state=False)
    bpy.ops.object.delete(use_global=False)
    

def draw_motors_and_wheels():
    # first Wheel
    bpy.ops.mesh.primitive_cylinder_add(radius=0.045,depth=0.01, location=(0,0,0.07))
    # rotate
    bpy.context.object.rotation_euler[1] = 1.5708
    # transalation
    bpy.context.object.location[0] = 0.135

    # second wheel
    bpy.ops.mesh.primitive_cylinder_add(radius=0.045,depth=0.01, location=(0,0,0.07))
    # rotate
    bpy.context.object.rotation_euler[1] = 1.5708
    # transalation
    bpy.context.object.location[0] = -0.135

    # motors
    bpy.ops.mesh.primitive_cylinder_add(radius=0.018,depth=0.06, location=(0.075,0,0.075))
    bpy.context.object.rotation_euler[1] = 1.5708
    
    bpy.ops.mesh.primitive_cylinder_add(radius=0.018,depth=0.06, location=(-0.075,0,0.075))
    bpy.context.object.rotation_euler[1] = 1.5708

    # motor shaft
    bpy.ops.mesh.primitive_cylinder_add(radius=0.006,depth=0.04, location=(0.12,0,0.075))
    bpy.context.object.rotation_euler[1] = 1.5708
    
    bpy.ops.mesh.primitive_cylinder_add(radius=0.006,depth=0.04, location=(-0.12,0,0.075))
    bpy.context.object.rotation_euler[1] = 1.5708
    
    # Caster Wheel
    bpy.ops.mesh.primitive_cylinder_add(radius=0.015,depth=0.05, location=(0,0.125,0.065))
    bpy.ops.mesh.primitive_cylinder_add(radius=0.015,depth=0.05, location=(0,-0.125,0.065))
    
    # Kinect
    bpy.ops.mesh.primitive_cube_add(size=0.04, location=(0,0,0.26))    
    
# middle plate
def draw_middle_plate():
    bpy.ops.mesh.primitive_cylinder_add(radius=0.15,depth=0.005, location=(0,0,0.22))

# top plate
def draw_top_plate():
    bpy.ops.mesh.primitive_cylinder_add(radius=0.15,depth=0.005, location=(0,0,0.37))


# support tubes
def draw_support_tubes():
    
    # Cylinders
    bpy.ops.mesh.primitive_cylinder_add(radius=0.007,depth=0.30, location=(0.09,0.09,0.23))
    bpy.ops.mesh.primitive_cylinder_add(radius=0.007,depth=0.30, location=(-0.09,0.09,0.23))
    bpy.ops.mesh.primitive_cylinder_add(radius=0.007,depth=0.30, location=(-0.09,-0.09,0.23))
    bpy.ops.mesh.primitive_cylinder_add(radius=0.007,depth=0.30, location=(0.09,-0.09,0.23))

# Exporting  STL    
def save_to_stl():
    bpy.ops.object.select_all(action='SELECT')
    stl_filepath = os.path.expanduser("~/Desktop/robot.stl")
    bpy.ops.export_mesh.stl(check_existing=True,
        filepath=stl_filepath, filter_glob="*.stl", ascii=False, use_mesh_modifiers=True, axis_forward='Y', axis_up='Z', global_scale=1.0)
  

if __name__ == "__main__":
    clean_scene()
    draw_base_plate()
    draw_motors_and_wheels()
    draw_middle_plate()
    draw_top_plate()
    draw_support_tubes()
    save_to_stl()
