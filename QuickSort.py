
def pivot_value(input):
  index = round(len(input) /2) -1
  return input[index]

def sort(input):
  if len(input) <= 1:
    return input
  else:
    pivot = pivot_value(input)
    lower = [item for item in input if item <   pivot ]
    pivots = [item for item in input if item == pivot ]
    upper = [item for item in input if item >   pivot ]
    return sort(lower) + pivots + sort(upper)
