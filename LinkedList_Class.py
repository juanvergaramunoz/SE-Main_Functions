
# coding: utf-8

# In[1]:

#########################################
####### General LINKED LIST CLASS #######
#########################################

####### FUNCTIONS FOR THIS CLASS #######
#
# - __init__: Generates the First element of the Linked List
#
# - insertNewElem: Allows to insert the element desired, ID and Data attached are required elements //Data could be s class, a string, a list,...
#
# - deleteElem: Erases the first element that matches the ID given
#
# - retrieveElem: Gives the data stored for the first element that matches the ID given
#
class linkedList:
    def __init__(self, ID, data, prev_elem = None, next_elem = None):
        self.ID = ID
        self.data = data
        self.prev = prev_elem
        self.next = next_elem
    
    
    #INPUT: 1) Unique numerical identifier (from element desired)
    #       2) Whatever data related to the given ID (it can be a string, a list, a class,...)
    #OUTPUT: Element desired
    def insertNewElem(self, ID, data):
        
        current = self
        while current.next != None:
            current = self.next
        
        new = linkedList(ID, data, current)
        current.next = new
        
        return True
    
    
    #INPUT: Unique numerical identifier (from element desired)
    #OUTPUT: The initial element of the new LinkedList with the changes made | FALSE __ if there is a problem during deletion
    def deleteElem(self, ID):
        
        current = self
        while current.next != None:
            if current.ID == ID:
                if self.prev != None:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    return self
                else:
                    self = current.next
                    self.prev = None
                    return self
            
            current = current.next
        
        
        if current.ID == ID:
            if self.prev != None:
                current.prev.next = None
                return self
            else:
                self = None
                return self
        else:
            return False
    
    
    #INPUT: Unique numerical identifier (from element desired)
    #OUTPUT: The data stored for the identifier requested
    def retrieveElem(self, ID):
        
        current = self
        while current.next != None:
            if current.ID == ID:
                return current.data
            
            current = current.next
        
        
        if current.ID == ID:
            return current.data
        else:
            return False
    
    
        

