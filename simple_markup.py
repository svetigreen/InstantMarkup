import sys, re
from util import *

if len(sys.argv) > 1:
    output_file = sys.argv[1]
else:
    output_file = 'test_output.html'

with open(output_file, 'w', encoding='utf-8') as f:
    f.write('<html><head><title>World Wide Spam</title><body>')

    title = True

    for block in blocks(sys.stdin):
        block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
        if title:
            f.write('<h1>')
            f.write(block)
            f.write('</h1>')
            title = False
        else:
            f.write('<p>')
            f.write(block)
            f.write('</p>')

    f.write('</body></html>')
