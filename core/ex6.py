frame = '{} {} {} {} {} {}'
print('\n')
print(frame.format('this', 'will', 'fill', 'in', 'this', 'frame'))
print('\n')
print(frame.format(7, 6, 3, 1, 6, 8))
print('\n')
print(frame.format(frame, frame, frame, frame, frame, frame))
print(frame.format(
    'this is another ',
    'way that you can ',
    'add data to be plugged into ',
    'your empty curly brackets ',
    'you will see this kind formating ',
    'when we do some machine learning and AI! '
))

print(
    'test one',
    'test two',
    'test three'
)

print(""""
test one
    test two
    test three
    """)

shopping_list ="""
time to make a shopping list:
\t** Some protein!
\t*  Maybe get some brownies
\t*  If i have room in the cart i'll get some veggies\n\t*** All done
    """

print(shopping_list)

x,y = (3,5)
print(x)
print(y)



