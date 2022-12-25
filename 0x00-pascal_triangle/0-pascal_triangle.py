def pascal_triangle(n): 
    tree = [[]] #first row is always just 1
    for x in range(1, n): #for every other row:
        if n <= 0:
         tree = [[]]
         return tree
        else:
         m = [1] #it always starts with 1
         for y in range(1, x): #for all the others:
            m.append(tree[x-1][y-1] + tree[x-1][y]) #work out what the number is
         m.append(1) #it always ends in 1
         tree.append(m) #add the row on
    return tree

               
               
