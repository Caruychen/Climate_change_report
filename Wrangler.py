import re
import os
# Set Functions and parameters
## Extract elements into a list, and parse observations to elements
def extractLines(lst):
    return [el.split() for el in lst]

## Perform multiple 1:1 string replacements using dict
def multipleReplace(dict, text):
  # Create a regular expression  from the dictionary keys
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

  # For each match, look-up corresponding value in dictionary
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)

def makeDirFile(file):
    if not file.endswith('.csv'):
        outname = file + '.csv'
    else:
        outname = file

    parent = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
    outdir = parent + '/Data'

    if not os.path.exists(outdir):
        os.mkdir(outdir)
        print('Created new directory:',outdir)

    return os.path.join(outdir, outname)

def makeOutFile(file):
    if not file.endswith('.png'):
        outname = file + '.png'
    else:
        outname = file

    parent = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
    outdir = parent + '/Outputs'

    if not os.path.exists(outdir):
        os.mkdir(outdir)
        print('Created new directory:',outdir)

    return os.path.join(outdir,outname)
