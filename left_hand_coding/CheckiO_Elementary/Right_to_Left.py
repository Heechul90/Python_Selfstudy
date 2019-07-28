### Right_to_Left


def right_to_left(phrases):
    return (','.join(phrases)).replace('right', 'left')

right_to_left(('left', 'right', 'welcome'))
right_to_left(('bright', 'aright', 'ok'))
right_to_left(('brightness wright',))
right_to_left(('enough', 'jokes'))
