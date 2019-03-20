import re

exampleLine = 'prices xom 91.43-91.44/vz50-50.01/s 7.23-7.24'

regEx = re.findall('\w{1,3}\s?\d{1,2}\.?\d{0,2}-\d{1,2}\.?\d{0,2}', exampleLine)

print(regEx)

# \w{1,3}
# \s?
# \d{1,2}
# \.?
# \d{0,2}
# -
# \d{1,2}
# \.?
# \d{0,2}

'''
identifiers:

\d any number
\D anything but a number
\s space
\S anything but a space
\w letters
\W anything but letters
. any letter except new line
\b word word word
\n new line
\t tab
\f form feed
\r carriage return
\. 


modifiers:
\d{1, 5} 44 545 5555 4324235 but not 8988
+ matches 1 or more
? matches 0 or 1
* 0 or more
$ matches end of a string
^ matches beginning of a string
| matches or a|b
[] range of variants
{x} this amount of the preceding code

escape is required for 
. + * [] $ ^ () {} | \ 


samples:

quantitative
quantatative
quant[ia]tative

[a-zA-Z]
[1-3]
'''