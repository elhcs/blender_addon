import bpy

class Human3DiffusionPanel(bpy.types.Panel):
    """Creates a Panel in the 3D Viewport for Human 3Diffusion"""
    bl_label = "Human 3Diffusion"
    bl_idname = "VIEW3D_PT_human3diffusion"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Human 3Diffusion"

    def draw(self, context):
        layout = self.layout

        layout.separator()
        layout.label(text="Environment Setup:")
        layout.operator("human3d.setup_environment", text="Setup Environment")

        # Section: Input Image
        layout.label(text="Input Image:")
        layout.operator("human3diffusion.upload_image", text="Upload Image")

        # Section: Inference
        layout.separator()
        layout.label(text="Generate 3D Avatar:")
        layout.operator("human3diffusion.generate_3d", text="Generate 3D Avatar")

        # Section: Mesh Settings
        layout.separator()
        layout.label(text="Mesh Quality:")
        layout.prop(context.scene.human3diffusion_properties, "mesh_quality", text="Quality")
        layout.label(text="Output Directory:")
        layout.prop(context.scene.human3diffusion_properties, "output_directory", text="")

        # Section: Output
        layout.separator()
        layout.label(text="View Results:")
        layout.operator("human3diffusion.view_output", text="Open Output Directory")
