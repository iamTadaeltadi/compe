class Solution:
    
 

def select(self, arr, i):
    minindx=i
    for j in range(i+1,len(arr)):
        if arr[minindx]>arr[j]:
            minindx=j
    return minindx
           
   
def selectionSort(self, arr,n):
         #code here
    for i in range(n-1):
        minindx=self.select(arr,i)
        arr[minindx],arr[i]=arr[i],arr[minindx]
