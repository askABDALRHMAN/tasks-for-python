


s = "abab"
arr = list(s)

ss = arr[0] + arr[1]  

for i in range(0, len(arr), 2):
    if arr[i] + arr[i+1] != ss:
        r = False
        break
    else:
        r = True
        break

print(r) 
