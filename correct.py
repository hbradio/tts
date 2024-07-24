import re
from autocorrect import Speller
spell = Speller()

with open('output/output_7.txt') as f:
    text = f.read()
    text = text.replace('- \n', '')
    text = text.replace('-\n', '')
    text = text.replace('^s', '\'s')
    text = text.replace('^', '')
    text = spell(text)
    text = re.sub(r'THE EDUCATION OF CHILDREN', '', text, flags=re.IGNORECASE)
    with open('output/output_7_corrected.txt', 'w') as fout:
        fout.write(text)