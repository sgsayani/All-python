counts=dict()
names=['sayani','sonali','sayani','kakali','kakali']
for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)