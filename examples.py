#!/usr/bin/python3
"""
Ridiculous mathy methods for
inventing an integer for e.g.
array element retrieval!


>>> import sys; sys.path.append('lib')
>>> from mathcessor import M

Gets an integer, as you'd expect.
>>> M.square_root_of_forty_nine
7

Beware of zero-based indexing on sequences. Seventh item is not index 7!
>>> l =  ['kitties', 'puppies', 'piggies', 'cowwies', 'donkies', 'sheepies', 'chickies', 'bears']

Index 7 gets eighth item.
>>> l[M.square_root_of_forty_nine]
'bears'

>>> l[M.cube_root_of_twenty_seven]
'cowwies'

>>> l[M.factorial_three]
'chickies'

>>> M.twelve
12

>>> l[M.two_squared]
'donkies'

>>> M.seventeen_decillion_eight_hundred_nonillion_quadrillion_four_hundred_million_twenty_seven_thousand_nineteen_cubed
5639752000000000000000000380233682099880000000000008545154290663407677400000064012969996051357782247859


"""

import doctest
doctest.testmod()
