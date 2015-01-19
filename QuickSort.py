
def middle_value(input):
  index = round(len(input) /2) -1
  return input[index]

def sort(input):
  if len(input) <= 1:
    return input
  else:
    middle = middle_value(input)
    lower = [item for item in input if item <  middle]
    pivot = [item for item in input if item == middle]
    upper = [item for item in input if item >  middle]
    return lower + pivot + upper

