import jmanage

def add(name, value, fp = "config.json"):
  jmanage.append(name, value, fp)

def remove(name, fp = "config.json"):
  jmanage.remove(name, fp)

def clear(fp = "config.json"):
  jmanage.write({}, fp)

def get(name, fp = "config.json"):
  data = jmanage.read(fp)
  
  if data.get(name):
    return data[name]
  else:
    print("\nWARNING: " + name + " doesn't exist! This will default to true instead.\n")

    for x in data:
      print(x)

    return True

def exists(name, fp = "config.json"):
  if get(name, fp) == None:
    return False
  else:
    return True