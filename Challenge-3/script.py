object = {"p" : {"q" : {"r" : "s"}}}
key = "p/q/r"



def objVal(key, object):
    split_key = key.split("/")
    value = object[split_key[0]][split_key[1]][split_key[2]]
    return key, value 



key, value = objVal(key, object)
print("Key is : " + key)
print("Value is : " + value)
