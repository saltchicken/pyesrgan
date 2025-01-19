import argparse
from .enhance import run_esrgan

def main():
    parser = argparse.ArgumentParser(description="Simple ESRGAN implementation")
    
    parser.add_argument('-i', '--input', required=True, help='Input image')
    parser.add_argument('-o', '--output', default='resized.png', type=str, help='Output file')
    args = parser.parse_args()
    run_esrgan(args.input, args.output)
