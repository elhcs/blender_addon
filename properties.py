import bpy

class Human3DiffusionProperties(bpy.types.PropertyGroup):
    """Properties for Human 3Diffusion"""
    mesh_quality: bpy.props.EnumProperty(
        name="Mesh Quality",
        description="Quality level for the generated mesh",
        items=[
            ("low", "Low", "Generate a low-quality mesh (faster)"),
            ("medium", "Medium", "Generate a medium-quality mesh"),
            ("high", "High", "Generate a high-quality mesh (slower)"),
        ],
        default="high",
    )
    output_directory: bpy.props.StringProperty(
        name="Output Directory",
        description="Directory to save generated outputs",
        default="//output",
        subtype="DIR_PATH",
    )