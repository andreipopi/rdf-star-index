
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


def get_index(s,p,o):
    
    if "?" in s and "?" in p and "?" in o: # ? ? ?
        return ""
    if  ("?" not in s) and ("?" not in p) and ("?" in o): # var var ?
        return "sp"
    if  ("?" not in s) and ("?" in p) and ("?" in o): # var ? ?
        return "s"
    if  ("?" in s) and ("?" not in p) and ("?" not in o):# ? var var
        return "po"
    if  ("?" not in s) and ("?" in p) and ("?" not in o):#
        return "os"


def naive_lookup(subj,pred,obj):
    index = get_index(subj,pred,obj)
    matching_triples = np.array([])
    matching_triples.shape = (0,3)

    for [s,p,o] in store:
        if index == "os":
            if o == obj and s== subj:
                matching_triples = np.vstack([matching_triples, [s,p,o]])
        if index == "s":
            if s== subj:
                matching_triples = np.vstack([matching_triples, [s,p,o]])
        if index == "po":
            if p == pred and o== obj:
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


#query = ["Andrei", "?var1", "?var2"]

query = ["?var1", "p31","o31"]

#our index is now s -> s52
#print(get(query[0]))


# Naive triple extraction 

print(naive_lookup(query[0],query[1],query[2]))



# Basic Index extraction

# Hexastore

# Vertical Partitioning

#


