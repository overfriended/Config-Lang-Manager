import lang
import config

def get(key, fp = "config.json"):
  return config.get(key, fp)

def msg(key, fp = "lang.json"):
  if get("use_msg") == True:
    return lang.getphrase(key, fp)
  else:
    print("Using msg is disabled.")

def init():
  print(msg("init"))

init()