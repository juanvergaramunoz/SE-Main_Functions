
# coding: utf-8

# In[1]:

#########################################
####### General HASH TABLE CLASS ########
#########################################

# Includes a contact class: X.name, X.number, X.address --> The number is the one that provides the main identifier

####### FUNCTIONS FOR THIS CLASS #######
#
# - __init__: Generates the hash string with the desired length || An specific hash function can be included as well
#
# - hashFunc: Generates the hash number (adjusted to the string length) based on the identifier given by the function selected above
#
# - insertElem: Allows to insert the element desired (identifier string must be given as well)
#
# - getElem: Given the string identifier returns all the contact data for the correspondent element
#
# - deleteElem: Deletes the element with the ID provided
#


#WE USE THE LINKED LIST CLASS TO MANAGE COLLISIONS
from LinkedList_Class import linkedList



##---------------------------------##
## Aux HASH NUM Generator Function ##
##---------------------------------##
#
# We define a default basic function for generating a hash identifier
#
# INPUT: Number given as a STRING
# OUTPUT: HASH NUM (all digits added together)
def phoneFunction(number):
    identifier = 0
    for digit in number:
        identifier += int(digit)
    return identifier



#######################################
######## Main HASHTABLE CLASS #########
#######################################
class hashTable:
    #INPUT: 1) Number of elements for the Hash Array (which will define the max value of the HASH Num)
    #       2) Desired Hash Function to generate the Hash Num from the Unique Identifier (such as a telephone number)
    #          - If not given, a default function adds the digits from the Unique Identifiers (that must be passed as a STRING)
    def __init__(self, num_options, function = phoneFunction):
        self.opt = num_options
        self.array = [None]*self.opt
        self.func = function
    
    #INPUT: Numerical Identifier ('Unique' number)
    #OUTPUT: Hash number (for the sel.array)
    def hashFunc(self, value):
        val = self.func(value)
        hash_num = val%self.opt
        
        return hash_num
    
    
    #INPUTS: 1) Element (a class)
    #        2) Unique numerical identifier
    #OUTPUT: Bool --> TRUE __ if insertion correct | FALSE __ if there is a problem during insertion
    def insertElem(self, element, id_val):
        hash_num = self.hashFunc(id_val)
        
        if self.array[hash_num] == None:
            self.array[hash_num] = linkedList(id_val,element)
            return True
        else:
            aux_linkedlist = self.array[hash_num]
            aux_linkedlist.insertNewElem(id_val,element)
            return True
    
    
    #INPUT: Unique numerical identifier (from element desired)
    #OUTPUT: Element desired
    def getElem(self, id_val):
        hash_num = self.hashFunc(id_val)
        
        if self.array[hash_num] == None:
            return False
        else:
            aux_linkedlist = self.array[hash_num]
            aux_data = aux_linkedlist.retrieveElem(id_val)
            return aux_data
        
    
    #INPUT: Unique numerical identifier (from element desired)
    #OUTPUT: Bool --> TRUE __ if deletion correct | FALSE __ if there is a problem during deletion
    def deleteElem(self, id_val):
        hash_num = self.hashFunc(id_val)
        
        if self.array[hash_num] == None:
            return False
        else:
            aux_linkedlist = self.array[hash_num]
            new_list = aux_linkedlist.deleteElem(id_val)
            if new_list != False:
                self.array[hash_num] = new_list
                return True
            else:
                return False


        

