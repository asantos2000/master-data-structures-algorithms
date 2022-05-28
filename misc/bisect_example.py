# Source https://docs.python.org/3/library/bisect.html
# Require Python 3.10+

from collections import namedtuple
from operator import attrgetter
from bisect import bisect, insort, bisect_left, bisect_right
from pprint import pprint

# Example 1
Movie = namedtuple('Movie', ('name', 'released', 'director'))

movies = [
    Movie('Jaws', 1975, 'Speilberg'),
    Movie('Titanic', 1997, 'Cameron'),
    Movie('The Birds', 1963, 'Hitchcock'),
    Movie('Aliens', 1986, 'Scott')
]

# Find the first movie released on or after 1960
by_year = attrgetter('released')
movies.sort(key=by_year)
movies[bisect(movies, 1960, key=by_year)]
Movie(name='The Birds', released=1963, director='Hitchcock')

# Insert a movie while maintaining sort order
romance = Movie('Love Story', 1970, 'Hiller')
insort(movies, romance, key=by_year)
pprint(movies)

# Exmple 2
def grade(score, breakpoints = None, grades='FDCBA'):
    if breakpoints is None:
        breakpoints = [60, 70, 80, 90]
    i = bisect(breakpoints, score)
    return grades[i]

pprint([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

# Example 3
data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
data.sort(key=lambda r: r[1])       # Or use operator.itemgetter(1).
keys = [r[1] for r in data]   
pprint(data)
pprint(keys)
pprint(data[bisect_left(keys, 0)])
pprint(data[bisect_left(keys, 1)])
pprint(data[bisect_left(keys, 5)])
pprint(data[bisect_left(keys, 8)])
