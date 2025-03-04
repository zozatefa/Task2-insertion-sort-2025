#قائمه تحتوي علي درجات الطلاب grades = [85, 92, 78, 90, 88, 76, 95]



def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  
        j = i - 1
        while j >= 0 and key < arr[j]:  
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  
    return arr

# قائمة درجات الطلاب
grades = [85, 92, 78, 90, 88, 76, 95]
sorted_grades = insertion_sort(grades)

print("الدرجات بعد الفرز:", sorted_grades)
