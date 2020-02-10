import jmanage

def addphrase(name, value, fp = "lang.json"):
  jmanage.append(name, value, fp)

def removephrase(name, fp = "lang.json"):
  jmanage.remove(name, fp)

def clear(fp = "lang.json"):
  jmanage.write({}, fp)

def getphrase(name, fp = "lang.json"):
  data = jmanage.read(fp)

  if data.get(name):
    return data[name]
  else:
    print(name + " doesn't exist!")
    return None

def exists(name, fp = "lang.json"):
  if getphrase(name, fp) == None:
    return False
  else:
    return True
