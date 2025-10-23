#printing each character in a list

a=["shoaib","Ali","Sam"]
for i in a: #shoaib
    for j in i: #s h o a i b
     print(j)


#unpacking dictionary using while loop

data = {
    "name": "Shoaib",
    "age": 22,
    "role": "Data Engineer"
}

data_to_list = list(data.items()) 
i = 0
while i < len(data_to_list):
    k, v = data_to_list[i]
    print(k, "=", v)
    i += 1


#bubble sort on a list
arr = [34,13,53,24,67,43,23]

n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:  
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted list:", arr)
