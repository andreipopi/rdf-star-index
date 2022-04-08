
import numpy as np

# Functions


# creates a list of all subjects, a list of all predicates, and a list of all objects
def initialise(sArr, pArr, oArr):
    objectsFile = open('objects.txt', 'r')
    Lines = objectsFile.readlines()
    index = 0
    for obj in Lines:
        obj = obj.rstrip("\n")
        oArr = np.vstack([oArr, [index, obj]])
        index += 1
    
    subjectsFile = open('subjects.txt', 'r')
    Lines = subjectsFile.readlines()
    index = 0
    for subj in Lines:
        subj = subj.rstrip("\n")
        sArr = np.vstack([sArr, [index, subj]])
        index += 1

    propFile = open('properties.txt', 'r')
    Lines = propFile.readlines()
    index = 0
    for prop in Lines:
        prop = prop.rstrip("\n")
        pArr = np.vstack([pArr, [index, prop]])
        index += 1
    return sArr, pArr, oArr


def print_store():
    for triple in store:
        print(triple)

def read_store():
    return

def get_index(s,p,o):
    if ("?" in s) and ("?" in p) and ("?" in o): # ? ? ?
        return ""
    if ("?" not in s) and ("?" not in p) and ("?" in o): # var var ?
        return "sp"
    if ("?" not in s) and ("?" in p) and ("?" in o): # var ? ?
        return "s"
    if ("?" in s) and ("?" not in p) and ("?" not in o):# ? var var
        return "po"
    if ("?" not in s) and ("?" in p) and ("?" not in o):#
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

def lookup_on_spo(subj, pred, obj):
    
    #assume spo for var ? ? 
    index = get_index(subj, pred, obj)
    matching_triples = np.array([])
    matching_triples.shape = (0,3)

    for p in spoIndex[subj]:
        for obj in spoIndex[subj][p]:
            matching_triples = np.vstack([matching_triples, [subj,p,obj]])

    return matching_triples

def lookup_on_pso(subj, pred, obj):
    matching_triples = np.array([])
    matching_triples.shape = (0,3)

    for subj in psoIndex[pred]:
        for obj in psoIndex[pred][subj]:
            matching_triples = np.vstack([matching_triples, [subj,pred,obj]])
    return matching_triples


# End Functions


# create triple store from file 
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

print("sshape after", store.shape)

# Create triple store with fake triples in a foor loop
#for i in range(0,100):
#    triple = ["s"+str(i), "p"+str(i), "o"+str(i)]
#    print(triple)
#    store = np.vstack([store, triple])
#print_store()


sArr = np.array([])
sArr.shape = (0,2)
pArr = np.array([])
pArr.shape = (0,2)
oArr = np.array([])
oArr.shape = (0,2)

sArr, pArr, oArr = initialise(sArr, pArr, oArr)

print(sArr)
print(pArr)
print(oArr)

    # spo         
    # [Andrei, [ [p29,[0,1]], 
    #            [p31,[4]]
    #           ]]

####### spo index #####
spoIndex = {}
for id, subject in sArr:
    predArr = {}

    for s,p,o in store:
        if subject == s:
            if p not in predArr:
                objArr = np.array([])

                for s1,p1,o1 in store:
                    if s == s1 and p1 == p and o1 not in objArr:
                        objArr = np.append(objArr,o1) # this should be optimised to store the index of the object so then objects shared from spo and pso
                predArr[p] = objArr
                print(objArr)
    spoIndex[subject] = predArr


#### pso Index ####
psoIndex = {}
for id, property in pArr:
    subjArr = {}

    for s,p,o in store:
        if property == p:
            if s not in subjArr:
                objArr = np.array([])

                for s1,p1,o1 in store:
                    if s == s1 and p1 == p and o1 not in objArr:
                        objArr = np.append(objArr,o1) # this should be optimised to store the index of the object so then objects shared from spo and pso
                subjArr[s] = objArr
                print(objArr)
    psoIndex[property] = subjArr

print("psoIndex",psoIndex)

psoMpa = np.array([])

sopMap = np.array([])
ospMap = np.array([])

pos = np.array([])
ops = np.array([])

query0 = ["Andrei", "?var1", "?var2"]

#print(lookup_on_spo("Andrei","?var1","o31"))

query1 = ["?var1", "p31","o31"]
print(lookup_on_pso("?var1", "p31", "o31"))

query2 = ["?var1", "p31","?var2"]

#our index is now s -> s52
#print(get(query[0]))

# Naive triple extraction 
#print(naive_lookup(query[0],query[1],query[2]))

# Basic Index extraction

# Hexastore



# sop, 
# osp, 
# pso, 
# spo, 

# pos, 
# ops.



# Vertical Partitioning

#


