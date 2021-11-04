from typing import List

# Util function to verify if a list is sorted. List is expected to be homogenuos and can check for list of strings or list of numbers
def is_list_sorted(input:List):
    list = [x.lower() if type(x) is str else x for x in input]
    return list == sorted(list)

# Util function to covert a list of complex number (string in the format 1k instead of 1000 etc) into number list
def sanitize_unit_list_to_number_list(input:List[str]) -> List[float]:
    unit_map = {'k':1000, 'm':1000000, 'b':1000000000}
    sanitzed_list = [float(x)  if x[-1].lower() not in unit_map.keys() else float(x[:-1])*unit_map[x[-1].lower()] for x in input]
    return sanitzed_list

# Util function to convert list of complexities (low/medium/high) to a number representation
def sanitize_complexity_list_to_number_list(input:List[str]) -> List[int]:
    complexity_map = {'low':0,'medium':1,'high':2}
    sanitized_list = [complexity_map[x.lower()] for x in input]
    return sanitized_list