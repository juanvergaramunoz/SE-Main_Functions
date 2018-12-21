
# coding: utf-8

# In[1]:

##################################################################
####### General indexingWords-Dictionary CLASS & FUNCTION ########
##################################################################

####### FUNCTIONS FOR THE dictTree CLASS #######
#
# - __init__: Generates a node for each letter || From the moment a letter from a word is not found (in "insertWord), the __init__ function starts calling itself to create each of the nodes for the rest of the letters, and relates each child letter to the correspondent parent letter (and viceversa).
#
# - insertWord: Takes a word, follows the tree letter by letter until a letter is not on the branch, and it creates a new branch starting from the last existent letter
#
# - checkWord: Takes a word, checks if it exists in the tree, returns the NODES found
#

####### getPositionalTree FUNCTION #######
#
# This function uses the dictTree CLASS to create a TREE with all words in a text, and their index position in the text. Then, it takes each target word, and returns at what position in the initial text those words have appeared (complete words only)
#
# - It receives a text and a list of "target words". Returns a list of lists: For each "target word" the funcion returns a list of indices where that word was found in the text. If that word does not exist in the text, it returns FALSE.
#



######################################
######## Main dictTree CLASS #########
######################################
class dictTree:
    #############################
    ### Time complexity: O(M) ###  --->  For M being the length of the word
    #############################
    #INPUT: 1) The node who is parent for the new letter
    #       2) The letter for that node
    #       3) The index for the new word being inserted (it is passed until the last letter is reached)
    #       4) The remaining part of the word remaining behind the current letter
    def __init__(self, parent = None, letter = None, index = None, word = None):
        
        self.letter = letter
        self.parent = parent
        #self.node stores all elements encountered with that path
        self.node = []
        #self.branches store the children for each parent node
        self.branches = []
        
        if index != None and letter != None:
            if word == None:
                self.node.append(index)
            else:
                if len(word) > 1:
                    self.branches.append(dictTree(self,word[0],index,word[1:len(word)]))
                elif len(word) == 1:
                    self.branches.append(dictTree(self,word[0],index))
    
    
    ####################################
    ### Time complexity: O(M*log(N)) ###  --->  M = length of the word || N = # of words already inserted
    ####################################                                   -> As it has to check the children node after node
    #INPUT: 1) The word to be inserted
    #       2) The index (its position in the text) for the new word being inserted
    def insertWord(self,word,index):
        
        if len(word) < 1:
            raise ValueError("'dictTree' class, 'insertWord' function ---> Word length is not valid!")
        
        aux_parent = self
        
        n = len(word)
        found = False
        for elem in self.branches:
            if elem.letter == word[0]:
                if len(word) == 1:
                    found = True
                    elem.node.append(index)
                    break
                else:
                    found = True
                    elem.insertWord(word[1:n],index)
                    break
        
        if not found:
            if n > 1:
                self.branches.append(dictTree(aux_parent,word[0],index,word[1:n]))
            else:
                self.branches.append(dictTree(aux_parent,word[0],index))
    
    
    ####################################
    ### Time complexity: O(M*log(N)) ###  --->  M = length of the word || N = # of words inserted
    ####################################                                   -> As it has to check the children node after node
    #INPUT: 1) The word to be inserted
    #       2) The index (its position in the text) for the new word being inserted
    #OUTPUT: A list of positions where the word had been found in the text || "None" otherwise
    def checkWord(self,word):
        
        if len(word) < 1:
            raise ValueError("'dictTree' class, 'checkWord' function ---> Element without length is not allowed")
        
        n = len(word)
        index = None
        for elem in self.branches:
            if elem.letter == word[0]:
                if len(word) == 1:
                    index = elem.node
                    break
                else:
                    index = elem.checkWord(word[1:n])
                    break
        
        if index:
            return index
        else:
            return None



#############################################
######## getPositionalTree FUNCTION #########
#############################################
###--------------------------------###
### Time complexity: O(N*M*log(N)) ### --> N = # of words in text || M = # length of word
###--------------------------------###
#
#INPUT: 1) The TEXT whose words position are of interest
#       2) The target words whose position we want to extract from the tree
#OUTPUT: A list of lists: For each "target word" the funcion returns a list of indices where that word was found in the text. If that word does not exist in the text, it returns FALSE.
def getPositionalTree(text,target):
    
    ### Time complexity: O(1) ###
    if len(text) < 1:
        raise ValueError("'getPositionalTree' function ---> Text length is not valid!")
        return None
    if len(target) < 1:
        raise ValueError("'getPositionalTree' function ---> Targets are not defined (len == 0)!")
        return None
    
    dictionaryTree = dictTree()
    
    n = len(text)
    i = 0
    aux_word = []
    ### Time complexity: O(L*M*log(N)) ### --> N = # of words in text || M = # length of word
    while i < n:
        if text[i] != " " and text[i] != "." and text[i] != ",":
            aux_word.append(text[i])
        else:
            if len(aux_word) > 0:
                aux_word = "".join(aux_word)
                dictionaryTree.insertWord(aux_word,i-len(aux_word))
                aux_word = []
            else:
                aux_word = []
        i += 1
    
    if len(aux_word) > 0:
        aux_word = "".join(aux_word)
        dictionaryTree.insertWord(aux_word,i-len(aux_word))
    
    
    ### Time complexity: O(T*M*log(N)) ### --> T = # of target words || M = # length of word || N = # of words in text
    indices = []
    for elem in target:
        aux_index = dictionaryTree.checkWord(elem)
        if aux_index != None:
            indices.append(aux_index)
        else:
            indices.append(False)
    
    return indices

