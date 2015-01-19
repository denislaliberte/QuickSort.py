
def sort(input):
  if len(input) <= 1:
    return input
  else:
    middle_index = middle(input)
    lower = [item for item in input if item < input[middle_index]]
    pivot = [item for item in input if item == input[middle_index]]
    upper = [item for item in input if item > input[middle_index]]
    return lower + pivot + upper

def middle(input):
  return round(len(input) /2) -1
