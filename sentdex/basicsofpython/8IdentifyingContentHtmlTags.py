from __future__ import division
import re


goodParagraphExample = open('ActualParagraphExample.php', 'r').read()
badParagraphExample = open('LotsOfHtml.php', 'r').read()

def countStuff(varToUse):
    typicalHtml = ('<div',
                   '</div>',
                   'class=',
                   '<img',
                   'hreflang',
                   'width=',
                   'height=')

    htmlCount = 0

    split = varToUse.split()
    totalVal = len(split)
    for item in split:
        for word in typicalHtml:
            if word in item:
                htmlCount += 1

    print('total number of tags is: ', htmlCount, ' rate: ', htmlCount/totalVal)

    if htmlCount/totalVal > .05:
        print('it is not a text')
    else:
        print('this looks like text')

countStuff(goodParagraphExample)
print('==========================================')
countStuff(badParagraphExample)