import subprocess, argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Simple ESRGAN implementation")
    
    parser.add_argument('-i', '--input', required=True, help='Input image')
    parser.add_argument('-o', '--output', default='__', type=str, help='Output file')
    args = parser.parse_args()
    run_esrgan(args.input, args.output)
    
    
    
def run_esrgan(input, output='__'):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    executable_path = os.path.join(current_directory, 'esrgan/realesrgan-ncnn-vulkan.exe')
    if output is not '__':
        parameters = ['-i', input, '-o', output, '-n', 'x4']
    else:
        parameters = ['-i', input, '-o', 'resized_' + input, '-n', 'x4']
        
    subprocess.run([executable_path] + parameters)
    
    
if __name__ == "__main__":
    main()