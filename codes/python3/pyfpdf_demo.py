# python3

# https://pyfpdf.readthedocs.io/en/latest/
# https://github.com/reingart/pyfpdf

# PNG, GIF and JPG support (including transparency and alpha channel)

from fpdf import FPDF

import sys

output_file = sys.argv[1]
input_list = []
total = 779
for i in range(total):
    # img = 'screenshots/%d.png' % (i + 1)
    img = 'screenshots/%d.png' % (i + 1)
    input_list.append(img)

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.set_margins(0, 0, 0)
# imagelist is the list with all image filenames
pdf.add_page()
for i in range(len(input_list)):
    # pdf.add_page()
    print('processing %d' % (i + 1))
    pdf.image(input_list[i], w=pdf.fw_pt, h=pdf.fh_pt, type='PNG')

print('output pdf, please wait...')
pdf.output(output_file)
pdf.close()
