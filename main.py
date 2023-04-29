from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='PNG to JPG console converter')
parser.add_argument("--input", type=str, help='File for convert')
parser.add_argument("--output", type=str, help='Output file')
args = parser.parse_args()
_in = args.input
_out = args.output

im = Image.open(_in)
rgb_im = im.convert('RGB')
rgb_im.save(_out)
