
# coding: utf-8

# In[1]:

#####################################
####### checkSubset FUNCTION ########
#####################################


from HashTable_Class import hashTable


#############################
### Time complexity: O(M) ###
#############################
#INPUT: String
#OUTPUT: Corresponding Hash_Identifier ==> Hash_Num = Hash_Identifier % hash_table_size
def hashFunction(elem):
#Gets String and Returns Array INDEX
    key = 0

    prev_char = ""
    for new_char in elem:
        if prev_char == "":
            prev_char = new_char
        else:
            key += ord(prev_char)*125 + ord(new_char)
            prev_char = ""

    if prev_char != "":
        key += ord(prev_char)

    return key


####################################
### Time complexity: O(N*log(N)) ###  --> N insertions with log(N) duration each
####################################
#INPUT: 1) Main SET "A"
#       2) SUBSET "B" to be checked
#OUTPUT: 1) Bool --> TRUE __ if "B" (second list) is a subset from "A" | FALSE __ otherwise
#        2) Empty array if "B" is a subset from "A" | List of tupples: [(ELEMENT_Z, times_Z_is_in_"B"_BUT_not_in_"A") ...]
# Complete the checkMagazine function below.
def checkSubset(greater_set, subset):
    
    hashedElems = hashTable(250,hashFunction)
    
    ### Time complexity: O(N*log(N)) ###
    for elem in subset:
        val = hashedElems.getElem(elem)
        if val:
            hashedElems.insertElem(val+1,elem)
        else:
            hashedElems.insertElem(1,elem)
    
    ### Time complexity: O(N*log(N)) ###
    for elem in greater_set:
        val = hashedElems.getElem(elem)
        if val:
            if val > 1:
                hashedElems.insertElem(val-1,elem)
            else:
                hashedElems.deleteElem(elem)
        
    #print("MAIN CHECK MAGAZINE <<----->> ELEM ccM has VALUE : ",hashedElems.lookupElement("ccM"))
    
    elemNotMatched = False
    ErrorElem_List = []
    for elem in subset:
        elemNotMatched = hashedElems.getElem(elem)
        if elemNotMatched:
            ErrorElem_List.append((elem,elemNotMatched))
            hashedElems.deleteElem(elem)
    
    if len(ErrorElem_List):
        ### IF WE WANTED TO PRINT MESSAGES WITH ELEMENTS IN SUBSET NOT FOUND IN MAIN SET ###
        #print("\ncheckSubset FUNCTION: Second list is not a SUBSET from first list")
        #for elem in ErrorElem_List:
        #    print("Problematic elem: '",elem[0],"'; that lacks ",elem[1]," match(es)")
        
        return False,ErrorElem_List
    else:
        return True,[]


        

