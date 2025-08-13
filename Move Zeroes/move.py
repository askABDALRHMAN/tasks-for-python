

nums = [ 0 , 1 , 0 , 3 , 12 ]

i = 0
for i in range(len(nums)):
    if nums[i] == 0:
        nums.append(nums.pop( i ))  
    else:
        i += 1

        # نا احنا بنتشك لو العنصر ده
        #  صفر يبقي هننقله لاخر المصفوفه
        #  ولاو غلط هزودواحد ونشوف الرقم ال بعده


print(nums)
