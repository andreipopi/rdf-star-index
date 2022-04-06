
import numpy as np

# Functions
def print_store():
    for triple in store:
        print(triple)

def get(index):
    matching_triples = np.array([])
    matching_triples.shape = (0,3)

    for [s,p,o] in store:
        if(s == index): #here we know that triple[0] is the index but we need to make it general
            matching_triples = np.vstack([matching_triples, [s,p,o]])
    return matching_triples
# End Functions


# Create triple store with fake triples in a foor loop
store = np.array([])
store.shape = (0,3)

print("shape",store.shape)


storeFile = open('store.txt', 'r')
Lines = storeFile.readlines()

print(Lines)
for line in Lines:
    array = eval(line)
    print("array",array)
    
    store = np.vstack([store,  array])


#for i in range(0,100):
#    triple = ["s"+str(i), "p"+str(i), "o"+str(i)]
#    print(triple)
#    store = np.vstack([store, triple])
    

print("sshape after", store.shape)
#print_store()


query = ["s52", "?var1", "?var2"]


#our index is now s -> s52
print(get(query[0]))


# Naive triple extraction 




# Basic Index extraction

# Hexastore

# Vertical Partitioning

#


