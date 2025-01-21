import bpy
import os
import subprocess
from .properties import Human3DiffusionProperties


class UploadImageOperator(bpy.types.Operator):
    """Upload an input image for processing"""
    bl_idname = "human3diffusion.upload_image"
    bl_label = "Upload Image"

    def execute(self, context):
        self.report({"INFO"}, "Image uploaded successfully!")
        return {"FINISHED"}



class Generate3DOperator(bpy.types.Operator):
    """Generate a 3D avatar from the input image"""
    bl_idname = "human3diffusion.generate_3d"
    bl_label = "Generate 3D Avatar"

    def execute(self, context):
        props = context.scene.human3diffusion_properties

        # Define paths
        base_dir = bpy.app.tempdir
        test_imgs_dir = os.path.join(base_dir, "human3diffusion_test_imgs")
        output_dir = os.path.join(base_dir, "human3diffusion_output")
        checkpoints_dir = os.path.join(os.path.dirname(__file__), "checkpoints")

        # Ensure directories exist
        os.makedirs(test_imgs_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)

        # Path to Blender's Python executable
        blender_python = "/Applications/Blender.app/Contents/Resources/4.3/python/bin/python3.11"
        infer_script = os.path.join(os.path.dirname(__file__), "human3diffusion/infer.py")

        try:
            # Run subprocess
            result = subprocess.run(
                [
                    blender_python, infer_script,
                    "--test_imgs", test_imgs_dir,
                    "--output", output_dir,
                    "--checkpoints", checkpoints_dir,
                ],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            # Log output for debugging
            print("Subprocess Output:\n", result.stdout)
            print("Subprocess Error:\n", result.stderr)

        except subprocess.CalledProcessError as e:
            self.report({"ERROR"}, f"Subprocess failed with error: {e.stderr}")
            return {"CANCELLED"}

        except FileNotFoundError:
            self.report({"ERROR"}, "Blender's Python executable not found.")
            return {"CANCELLED"}

        # Verify and import the generated mesh
        mesh_file = os.path.join(output_dir, "mesh.obj")
        if os.path.exists(mesh_file):
            bpy.ops.import_scene.obj(filepath=mesh_file)
            self.report({"INFO"}, "3D Avatar Generated and Imported!")
        else:
            self.report({"ERROR"}, "Mesh file not found in output directory.")
            return {"CANCELLED"}

        return {"FINISHED"}
    
class ViewOutputOperator(bpy.types.Operator):
    """Open the output directory to view results"""
    bl_idname = "human3diffusion.view_output"
    bl_label = "View Output"

    def execute(self, context):
        props = context.scene.human3diffusion_properties
        output_dir = bpy.path.abspath(props.output_directory)

        if os.path.exists(output_dir):
            bpy.ops.wm.url_open(url=f"file://{output_dir}")
            self.report({"INFO"}, f"Opened output directory: {output_dir}")
        else:
            self.report({"ERROR"}, f"Output directory does not exist: {output_dir}")
            return {"CANCELLED"}

        return {"FINISHED"}