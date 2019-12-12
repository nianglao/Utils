# python3

# https://pyfpdf.readthedocs.io/en/latest/
# https://github.com/reingart/pyfpdf

# PNG, GIF and JPG support (including transparency and alpha channel)

from fpdf import FPDF

import sys

output_file = sys.argv[1]
input_list = []
for i in range(779):
    img = 'screenshots/%d.png' % (i + 1)
    input_list.append(img)

pdf = FPDF()
# imagelist is the list with all image filenames
pdf.add_page()
for i in range(len(input_list)):
    # pdf.add_page()
    print('processing %d' % i)
    pdf.image(input_list[i])
pdf.output(output_file)
