# Arr -> Int -> Var -> Arr
def update(a, i, val):
    b = a
    b[i] = val
    return b

# Arr -> Int -> Var
def lookup(a, i):
    return a[i]