





for id,s in sArr:

    #print("subject", s)
    for subj,pred,obj in store:
        if s == subj:
            #print(subj, s)
            #list of objects
            predArr = np.array([])

            for subject,predicate,object in store: 
                if s == subject and pred == predicate:
                    #print(subject, predicate)
                    objArr = np.array([])
                    for su,pr,ob in store:
                        if object not in objArr:
                            objArr = np.append(objArr, object)

                    print("objArray", objArr)
            
                    #predArr = np.append(predArr, objArr)

                    #if predicate not in predArr:
                    predArr = np.append(predicate, [objArr])

            #print(predArr)
    print("------------")
          

            # [pred1 , [3,54,2]]


for id, subject in sArr:

    predArr = np.array([])
    for s,p,o in store:

        if subject == s: 

            if p not in predArr:

                objArr = np.array([])
                for s1,p1,o1 in store:
                    if s1 == s and p1 == p and (o1 not in objArr):
                        objArr = np.append(objArr, o1)
                predArr = np.hstack([p, objArr])
            
                
            predArr = np.vstack([predArr])

        print(predArr)


# Create triple store with fake triples in a foor loop
#for i in range(0,100):
#    triple = ["s"+str(i), "p"+str(i), "o"+str(i)]
#    print(triple)
#    store = np.vstack([store, triple])
#print_store()


def get_access_pattern(s,p,o):
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
    index = get_access_pattern(subj,pred,obj)
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


# Naive triple extraction 
#print(naive_lookup(query[0],query[1],query[2]))