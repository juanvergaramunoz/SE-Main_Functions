# Software Engineering - Main Functions --> juanvergaramunoz


** Project: Main Functions
** Creator: juanvergaramunoz
** Year: 2018


## Description

This Software Engineering repository includes general classes that deal with Hash Tables, Heaps, Trees,...

The target of this project is to provide a set of useful tools to be used by whoever is interested

**This project has the following CLASSES:**

1) "LinkedList_Class.py" has the "linkedList" Class -- FUNCTIONS:

       - __init__(self, ID, data, prev_elem = None, next_elem = None)
       
       - insertNewElem(self, ID, data)
       
       - insertElem(self, ID, data)
       
       - deleteElem(self, ID)
       
       - retrieveElem(self, ID)
 
 

2) "HashTable_Class.py" has the "hashTable" Class -- FUNCTIONS:
       
       - __init__(self, num_options, function = phoneFunction)
       
       - hashFunc(self, value)
       
       - insertElem(self, element, id_val)
       
       - getElem(self, id_val)
       
       - deleteElem(self, id_val)
 
 

3) "indexingWords-DictionaryTree_Class&Function.py" the "dictTree" Class -- FUNCTIONS:
       
       - __init__(self, parent = None, letter = None, index = None, word = None)
       
       - insertWord(self,word,index)
       
       - checkWord(self,word)
       
       - getPositionalTree(text,target)
 


**This project has the following FUNCTIONS:**

1) "Mergesort_Function.py" the "mergesort" Function -- mergesort(array)

    - This function sorts in ascending order a list of numbers   << N * log(N) >>

2) "indexingWords-DictionaryTree_Class&Function.py" has the "getPositionalTree" Function -- getPositionalTree(text,target)

    - This function uses the dictTree CLASS to create a TREE with all words in a text, and their index position in the text. Then, it takes each target word, and returns at what position in the initial text those words have appeared (complete words only)

3) "checkSubset_Function.py" has the "checkSubset" Function -- checkSubset(greater_set, subset)

    - Checks if List of Elements "B" (subset) is a subset from List of Elements "A" (greater_set)

