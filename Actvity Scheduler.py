def scheduleActivities(a,s,f):
    n = len(f)

    Array=[0]*n
    i = 0
    Array[i]=a[i]
    

    for j in range(n):
        
        if s[j] >= f[i]:
            i = j
            Array[i]=a[j]

    return Array
  
def print_Array(A):
    print ("The following activities are selected")
    for i in range(len(A)):
         if A[i]!=0:
             print(A[i])
  
a = ["Maths","Enslish","Biology","Chemistry","Geography","Music"]
s = [1, 3, 0, 5, 8, 5] 
f = [2, 4, 6, 7, 9, 9]
Array = scheduleActivities(a,s,f)
print_Array(Array)