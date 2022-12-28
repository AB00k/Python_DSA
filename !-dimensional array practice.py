from array import *
arr1=array('i',[1,2,3,4,5]) #create an array
for i in arr1:              #traverse an array
    print(i)
print(arr1[4])      #access individual elements through indexes
arr1.append(6)      #it will insert value at the end
print(arr1)
arr1.insert(0,7)      #used to insert value at specific indes of an array
print(arr1)
arr2=array('i',[7,8,9,10])
arr1.extend(arr2)           #used to extend the array or concatinate the array
print(arr1)
lst=[11,12,13]
arr1.fromlist(lst)         #used to add array with list or can say concatinate
print(arr1)
arr1.remove(7)
print(arr1)                #used to remove element from an array time complexity is o(n) as it has to move all elements to the left
arr1.pop()                 #used to remove last element time complexity o(1)
print(arr1)
print(arr1.index(9))             #used to find index of any number
arr1.reverse()                   #used to reverse array
print(arr1)
print(arr1.buffer_info())        #used to find buffer info
print(arr1.count(5))             #used to count the occurance of specific element
#strng=arr1.tostring()            #convert an array to string
#ints=array('i')
#ints.fromstring(strng)          #convert it back to array
print(arr1.tolist())             #used to convert array to list
arr1.reverse()
print(arr1[0:10])                #slice elements from an array




