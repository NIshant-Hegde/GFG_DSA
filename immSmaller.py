def immediateSmaller(self,arr,n,x):
        #return required ans
        
        #Find a smaller element than x
        for ele in arr:
            if ele <= x:
                break
        
        immSmallest = ele
        distance = x - immSmallest
        
        flag = 0
        
        for i in range(1, len(arr)):
            if arr[i] < x:
                flag = 1     #-> Minimum exists
                if (x - arr[i]) == 0:
                    return arr[i]
                
                if (x - arr[i]) < distance:
                    immSmallest = arr[i]
                    distance = x - immSmallest
        
        if flag:
            return immSmallest
        else:
            return -1