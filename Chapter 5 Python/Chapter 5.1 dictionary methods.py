marks = {
    "Paras" : 100,
    "Nainwal" : 95,
    "singh" : 90,
    
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"singh": 94})
print(len(marks))

print(marks.get("chirag")) #print none
print(marks["chirag"]) # returns an error message