def scheduleActivities(subject_array,star,final):
    length_of_Array = len(final)

    Array=[0]*length_of_Array
    i = 0
    Array[i]=subject_array[i]
    
    for j in range(length_of_Array):
        if star[j] >= final[i]:
            i = j
            Array[i]=subject_array[j]

    return Array
  
def print_Array(A):
    print ("The following activities are selected")
    for i in range(len(A)):
         if A[i]!=0:
             print(A[i])
  
subject_array = ["Maths","Enslish","Biology","Chemistry","Geography","Music"]
star = [1, 3, 0, 5, 8, 5] 
final = [2, 4, 6, 7, 9, 9]
Array = scheduleActivities(subject_array,star,final)
print_Array(Array)

print("Without any Doubt Python has taken me to a level of ignoring previous structured Languages I've learned so far")

for i in range(5):
    print("Accept the Change")