
import numpy as np

# Functions
# creates 3 lists of all available: subjects, predicates, objects
def initialise(sArr, pArr, oArr):
    objectsFile = open('files/objects.txt', 'r')
    Lines = objectsFile.readlines()
    index = 0
    for obj in Lines:
        obj = obj.rstrip("\n")
        oArr = np.vstack([oArr, [index, obj]])
        index += 1
    
    subjectsFile = open('files/subjects.txt', 'r')
    Lines = subjectsFile.readlines()
    index = 0
    for subj in Lines:
        subj = subj.rstrip("\n")
        sArr = np.vstack([sArr, [index, subj]])
        index += 1

    propFile = open('files/properties.txt', 'r')
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

def lookup_on_spo(subj, pred, obj):
    matching_triples = np.array([])
    matching_triples.shape = (0,3)
    for p in spoIndex[subj]:
        if p == pred:#what if pred contains ?
            for obj in spoIndex[subj][p]:
             matching_triples = np.vstack([matching_triples, [subj,p,obj]])
    return matching_triples

def lookup_on_pso(subj, pred, obj):
    matching_triples = np.array([])
    matching_triples.shape = (0,3)
    for s in psoIndex[pred]:
        if s == subj: #what if s contains ?
            for obj in psoIndex[pred][s]:
                matching_triples = np.vstack([matching_triples, [s,pred,obj]])
    return matching_triples

def lookup_on_sop(subj, pred, obj):
    matching_triples = np.array([])
    matching_triples.shape = (0,3)
    for o in sopIndex[subj]:
        if o == obj: #  what if o contains ?
            for p in sopIndex[subj][o]:
                matching_triples = np.vstack([matching_triples, [subj,p,o]])
    return matching_triples

def lookup_on_osp(subj, pred, obj):
    matching_triples = np.array([])
    matching_triples.shape = (0,3)

    if "?" not in subj:
        for s in ospIndex[obj]:
            if s == subj: #  what if s contains ?
                for p in ospIndex[obj][s]:
                    matching_triples = np.vstack([matching_triples, [s,p,o]])
    else:
        for s in ospIndex[obj]:
                for p in ospIndex[obj][s]:
                    matching_triples = np.vstack([matching_triples, [s,p,o]])

    return matching_triples
# End Functions

# create triple store from file 
store = np.array([])
store.shape = (0,3)
storeFile = open('files/store.txt', 'r')
Lines = storeFile.readlines()
for line in Lines:
    array = eval(line)
    store = np.vstack([store,  array])

sArr = np.array([])
sArr.shape = (0,2)
pArr = np.array([])
pArr.shape = (0,2)
oArr = np.array([])
oArr.shape = (0,2)

# 
sArr, pArr, oArr = initialise(sArr, pArr, oArr)

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
    spoIndex[subject] = predArr
print(spoIndex)

#### pso Index ####
psoIndex = {}
for id, property in pArr:
    subjArr = {}
    for s,p,o in store:
        if property == p:
            if s not in subjArr:
                objArr = np.array([])
                for s1,p1,o1 in store:
                    if s == s1 and p1 == property and o1 not in objArr:
                        objArr = np.append(objArr,o1) # this should be optimised to store the index of the object so then objects shared from spo and pso
                subjArr[s] = objArr
    psoIndex[property] = subjArr

#### sop Index ####
sopIndex = {}
for id, subject in sArr:
    objArr = {}
    for s,p,o in store:
        if subject == s:
            if o not in objArr:
                propArr = np.array([])
                for s1,p1,o1 in store:
                    if (s == s1) and (o1 == o) and (p1 not in propArr) and (p1 in pArr):
                        propArr = np.append(propArr,p1)
                objArr[o] = propArr
    sopIndex[subject] = objArr

#### osp Index ####
ospIndex = {}
for id, object in oArr:
    subjArr = {}
    for s,p,o in store:
        if object == o:
            if s not in subjArr:
                propArr = np.array([])
                for s1,p1,o1 in store:
                    if (s == s1) and (o1 == o) and (p1 not in propArr):
                        propArr = np.append(propArr,p1)
                subjArr[s] = propArr
    ospIndex[object] = subjArr

print(ospIndex)

## POS index ##
posIndex = {}
for id, property in pArr:
    objArr = {}
    for s,p,o in store:
        if property == p: #if p matches the property we are currently building the index for
            if o not in objArr:
                subjArr = np.array([])
                for s1, p1, o1 in store:
                    if (p == p1) and (o == o1) and (s1 not in subjArr):
                        subjArr = np.append(subjArr, s1)
                objArr[o] = subjArr
    posIndex[property] = objArr            
print(posIndex)    

## ops index ##
opsIndex = {}
for id, object in oArr:
    propArr = {}
    for s,p,o in store: 
        if object == o:
            if p not in propArr:
                subjArr = np.array([])
                for s1,p1,o1 in store:
                    if (o1 == o) and (p1 == p) and (s1 not in subjArr):
                        subjArr = np.append(subjArr, s1)
                propArr[p] = subjArr
    opsIndex[object] = propArr
print("opsIndex",opsIndex)



print(lookup_on_spo("Pallino","p31","?var4"))  #SPO    s p ?

print(lookup_on_pso("Andrei", "p31", "?var1")) #PSO   s p ?

print(lookup_on_sop("Marco", "?var", "o60"))   #SOP     s ? o

print(lookup_on_osp("Pallino", "?var", "o60")) #OSP     s ? o

#ops = np.array([])
#OPS      ? p o
                                                      

# access patterns
# spo
# ? ? ?
# s ? ? 
# s p ?
# s p o

# pos
# ? p ?
# ? p o

# osp
# ? ? o 
# s ? o





# todo
# finish all indexes
# create a general method to create all of them
# how to 