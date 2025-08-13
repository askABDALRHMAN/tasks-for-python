



nums = [ 1 , 2 , 2 , 3 ]  # مثال

increasing = True
decreasing = True

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        increasing = False
    if nums[i] < nums[i + 1]:
        decreasing = False

# هنا احنا هنتشك تصاعدي او
#  تنازلي لو الرقم الاول اكبر من الرقم
#  التاني يبقي كد تنازلي وهيكون القيمه
#  التصاعديه غلط و العكس هيكوتن صح
#  ونفس الكلام بردو علي التنازلي   


if increasing == True or decreasing == True:
    
    print(True)

else:

    print(False)
