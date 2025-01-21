bl_info = {
    "name": "Human 3Diffusion Addon",
    "description": "Generate 3D avatars from 2D images using Human 3Diffusion.",
    "author": "El Houssaine CHAHBOPUN",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Tools > Human 3Diffusion",
    "category": "3D View",
}

import bpy

from .properties import Human3DiffusionProperties
from .ui import Human3DiffusionPanel
from .operators import UploadImageOperator, Generate3DOperator, ViewOutputOperator


def register():
    bpy.utils.register_class(Human3DiffusionProperties)
    bpy.types.Scene.human3diffusion_properties = bpy.props.PointerProperty(type=Human3DiffusionProperties)

    bpy.utils.register_class(Human3DiffusionPanel)
    bpy.utils.register_class(UploadImageOperator)
    bpy.utils.register_class(Generate3DOperator)
    bpy.utils.register_class(ViewOutputOperator)


def unregister():
    del bpy.types.Scene.human3diffusion_properties
    bpy.utils.unregister_class(Human3DiffusionProperties)

    bpy.utils.unregister_class(Human3DiffusionPanel)
    bpy.utils.unregister_class(UploadImageOperator)
    bpy.utils.unregister_class(Generate3DOperator)
    bpy.utils.unregister_class(ViewOutputOperator)


if __name__ == "__main__":
    register()