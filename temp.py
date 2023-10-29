lister = [["a", 1], ["b", 2]]
print(lister)
newLister = sum(list(map(lambda x: x[1], lister)))
print(newLister)
