import tempfile
import os
import subprocess
from PIL import Image

def run_esrgan(input, output, scale=2, resolution=None):
    # TODO make sure scale is not negative or ridiculous
    with tempfile.TemporaryDirectory() as temp_dir:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        executable_path = os.path.join(current_directory, 'esrgan/realesrgan-ncnn-vulkan.exe')
        parameters = ['-i', input, '-o', temp_dir + '/tmp.png', '-n', 'x4']
            
        subprocess.run([executable_path] + parameters)
        image = Image.open(temp_dir + '/tmp.png')
        width, height = image.size
        if resolution:
            new_width = resolution[0]
            new_height = resolution[1]
        else:
            new_width = int(width / (4 / scale))
            new_height = int(height / (4 / scale))
        resized_image = image.resize((new_width, new_height))
        resized_image.save(output)
