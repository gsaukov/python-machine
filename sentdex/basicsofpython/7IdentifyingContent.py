from __future__ import division
import re


goodParagraphExample = open('ActualParagraphExample.php', 'r').read()
badParagraphExample = open('LotsOfHtml.php', 'r').read()

def doRatio(varToUse):
    allChars = len(re.findall('.', varToUse))
    allWordChars = len(re.findall('\w', varToUse))

    theRatio = allWordChars/allChars
    if theRatio > .77:
        print('hey this looks like a real paragraph')
    else:
        print('yuck, this looks bad')

doRatio(goodParagraphExample)

doRatio(badParagraphExample)