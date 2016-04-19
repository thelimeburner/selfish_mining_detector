import pickle
from blockchain import blockexplorer

dbFile = "simple_loop_process.dat"
timeFile = "times.txt"
blockchains = []

with open(dbFile,"rb") as f:
    for _ in range(407908):
        try:
            blockchains.append(pickle.load(f))
        except:
            break

print len(blockchains)



with open(timeFile,"w") as f:
    for value in blockchains:
        f.write(str(value.time)+"\n")
