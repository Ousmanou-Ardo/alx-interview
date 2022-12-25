from functools import reduce

def pascal_triangle(level, acc = None):
    if not acc: acc = [[1]]
    if level == 1: return acc
    acc.append ( [1] + [a + b for a, b in zip (acc [-1], acc [-1] [1:] ) ] + [1] )
    return pascal_triangle(level - 1, acc)

               
               
