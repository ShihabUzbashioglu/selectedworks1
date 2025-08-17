from rembg import remove
from PIL import image

input_path = 'clgot.jpeg'
output_path = ' clgot.png'

inp = image.open(input_path)
output = remove(inp)

output.save(output_path)
image.open("clgot.png")