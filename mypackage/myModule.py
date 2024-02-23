def top_n (items, n):
    """Return top n items in array in descending order 
    
    Args:
        items (array): list or array-like object
        n (int): number of items to be returned
        
    Return: 
        array: top n items, desc order
        
    Egs:
        >>>top_n([8,3,2,7,4], 3)
        [8,7,4]  
    """
    for i in range(n): # keep sorting until we have top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]: # if this is bigger than the next item...
                items[j], items[j+1] = items[j+1], items[j] # swap the two 

    # get last two items
    top_n = items[-n:]

    # return in descending order
    return top_n[::-1]