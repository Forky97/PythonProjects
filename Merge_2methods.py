#############################   Speed = O(n * LogN)  ################################################

def  merge (lst):
    if len(lst)<2:
        return lst
    mid = len(lst)//2
    left = merge(lst[mid:])
    right = merge(lst[:mid])

    return sorter(left,right)

def sorter(left,right):
    i,j,lst=0,0,[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            lst.append(left[i])
            i+=1
        else:
            lst.append(right[j])
            j+=1
    if i<j:
        lst.extend(left[i:])
    else:lst.extend(right[j:])

    return lst

######################################################################################################





###################  O(n*logN) - better casses , O(n) - worst  ###############

def fast_sort(lst):
    if len(lst)<2:
        return lst
    elem=lst[0]
    left = [i for i in lst if i < elem]
    mid = [i for i in lst if i == elem]
    right = [i for i in lst if i > elem]

    return fast_sort(left)+mid+fast_sort(right)

print(fast_sort([5,2,1,6,2,4,7,8,1]))

######################################################################################################