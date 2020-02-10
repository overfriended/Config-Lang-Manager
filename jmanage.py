import json

def read(path = "config.json"):
  with open(path, 'r') as out:
    data = json.load(out)

    return data

def append(key, value, path = "config.json"):
  data = read(path)

  with open(path, 'w') as out:
    data[key] = value

    json.dump(data, out)

def write(value = {}, path = "config.json"):
  data = read(path)

  with open(path, 'w') as out:
    json.dump(value, out)

def remove(key, path = "config.json"):
  data = read(path)

  with open(path, 'w') as out:
    if len(data) == 1:
      write({}, path)
    else:
      del data[key]
    
    json.dump(data, out)
    
