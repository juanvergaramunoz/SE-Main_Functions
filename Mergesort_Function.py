
# coding: utf-8

# In[1]:

###################################
####### MergeSort Function ########
###################################


####################################
### Time complexity: O(N*log(N)) ###  --> N comparisons for log(N) steps
####################################
#INPUT: Unordered Array
#OUTPUT: Ordered Array
def mergesort(array):
    
    #We check the length of the array: if EMPTY --> ERROR // if length == 1 --> we return the array as it is
    n = len(array)
    if n == 0:
        print("ERROR - NON-VALID ARRAY")
        return []
    elif n == 1:
        return array
    
    #We divide the array in to halves
    half = int(n/2)
    left_array = mergesort(array[0:half])
    right_array = mergesort(array[half:n])
    
    #We iterate over both halves and we get the array sorted
    i = 0
    n_i = len(left_array)
    j = 0
    n_j = len(right_array)
    final_array = []
    while i < n_i and j < n_j:
        if left_array[i] < right_array[j]:
            final_array.append(left_array[i])
            i += 1
        else:
            final_array.append(right_array[j])
            j += 1
    
    #We add the remaining part from the half that still has any elements left
    if i == n_i and j < n_j:
        final_array += right_array[j:n_j]
    elif j == n_j and i < n_i:
        final_array += left_array[i:n_i]
    else:
        print("ERROR in MERGESORT ALGORITHM --- ARRAYS OUT OF RANGE")
    
    #We return the final array
    return final_array

        

