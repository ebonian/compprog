def reverse(d: dict):
  d_keys = list(d.keys())
  d_values = list(d.values())

  new_dict = {}

  for i in range(len(d_keys)):
    new_dict[d_values[i]] = d_keys[i]

  return new_dict

def keys(d: dict, v: int):
  new_list = []

  for key in d:
    value = d[key]
    if (value == v) : new_list.append(key)

  return new_list

exec(input().strip())