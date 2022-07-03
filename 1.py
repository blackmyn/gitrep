def minelem(arr): #функция нахождения минимального элемента
    max_ = arr[0]
    for ele in arr:
        if ele < max_:
           max_ = ele
    return max_ 
i = 0
newmin =0
count = 0
a = []
n = int(input("Please, input your size of array"))  # считываем количество элемент в списке
for i in range(n):
    new_element = int(input("Input your element"))  # считываем очередной элемент
    a.append(new_element)
    count = count+1
print(a)
min = minelem(a)
print("Min. element of array:")
print(min)
if (count < 6):
    print("Size of your array is less than 6. Program can't work in this case")
    print("Try again with size > 6")
elif (count >= 6):
    newmin = (min**2) + min
    a.remove(min)
    a.insert(5,newmin)
    print("Your changed array:")
    print(a)
print("hell yea")
print("edit")
