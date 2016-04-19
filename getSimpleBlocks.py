from blockchain import blockexplorer
import time
import pickle
import datetime
dbFile = "simple_loop.dat"
current_milli_time = lambda: int(round(time.time() * 1000))
counter = 0

def save(blockchains):
    global counter
    counter += len(blockchains)
    with open(dbFile,"ab+") as f:
        for value in blockchains:
            pickle.dump(value,f)




blocks = blockexplorer.get_blocks(time = current_milli_time())
print blocks[len(blocks)-1].hash
print blocks[len(blocks)-1].height
print blocks[len(blocks)-1].time
print blocks[len(blocks)-1].main_chain




#def getBlocks(timestamp):
#    try:
#        blocks = blockexplorer.get_blocks(time = timestamp)
#        save(blocks)
#        print len(blocks)
#        print "last know "+str(timestamp)
#        getBlocks(timestamp-86400000)
#    except Exception as e:
#        print e
#        getBlocks(timestamp-86400000)
#
def getBlocks(timestamp):
    while timestamp > 0:
        try:
            blocks = blockexplorer.get_blocks(time = timestamp)
            save(blocks)
            print len(blocks)
            print "last know "+str(timestamp)
        except Exception as e:
            print e
            
        timestamp = timestamp-86400000


getBlocks(1461018878025)

#prev = datetime.date.today()- datetime.timedelta(1)
#sample = int(prev.strftime("%s"))
#print sample - datetime.timedelta(1)
