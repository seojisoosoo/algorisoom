N=input()
N_arr=list(map(int, input().split()))
M=input()
M_arr=list(map(int, input().split()))

for m in M_arr:
    if m in N_arr:
        print("yes", end=" ")
    else:
        print("no", end=" ")
print('\n')