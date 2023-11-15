N=input()

col=["", "a","b","c","d","e", "f","g","h"]
row=[0, 1, 2, 3, 4, 5, 6, 7, 8]

c=N[0]
r=N[1]

answer=0

for i in range(len(col)):
    if c==col[i]:
        c_index=i


r_index=int(r)

if c_index+2>0 and c_index+2<=8 and r_index-1>0 and r_index-1<=8:
    answer+=1
if c_index+2>0 and c_index+2<=8 and r_index+1>0 and r_index+1<=8:
    answer+=1
if c_index-2>0 and c_index-2<=8 and r_index-1>0 and r_index-1<=8:
    answer+=1
if c_index-2>0 and c_index-2<=8 and r_index+1>0 and r_index+1<=8:
    answer+=1
if c_index+1>0 and c_index+1<=8 and r_index-2>0 and r_index-2<=8:
    answer+=1
if c_index-1>0 and c_index-1<=8 and r_index-2>0 and r_index-2<=8:
    answer+=1
if c_index+1>0 and c_index+1<=8 and r_index+2>0 and r_index+2<=8:
    answer+=1
if c_index-1>0 and c_index-1<=8 and r_index+2>0 and r_index+2<=8:
    answer+=1

print(answer)