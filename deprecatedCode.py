





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
