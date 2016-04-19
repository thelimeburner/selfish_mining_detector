# selfish_mining_detector
Used to study selfish mining.


# Files
- getSimpleBlocks.py ==> This requests blocks for everyday since the start of bitcoin. It will fun forever so stop it when it gets to zero. You shouldn't need to run this.
- opener.py ==> File used to test opening the data file. No need to use or run
- simple_loop_process.dat ==> This holds all of the simple blocks in a file. Can be read by both opener and analyze_data.ipynb
- analyze_data.ipynb ==> Main python notebook. Reads the simple_loop_process.dat. More details inside of notebook
- times_diff.txt ==> This shows data about blocks next to eachother.
- times.txt ==> Holds the time of each block




# Libraries
- blockchainexplorer ==> https://github.com/blockchain/api-v1-client-python/blob/master/docs/blockexplorer.md
