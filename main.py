from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='PNG to JPG console converter')
parser.add_argument('-i', '--input', type=str, required=True, help='File for convert')
parser.add_argument('-o', '--output', type=str, required=True, help='Output file')
args = parser.parse_args()
_in = args.input
_out = args.output

try:
    im = Image.open(_in)
    rgb_im = im.convert('RGB')
    rgb_im.save(_out)
    im.close()
except Exception as error:
    print(error)
