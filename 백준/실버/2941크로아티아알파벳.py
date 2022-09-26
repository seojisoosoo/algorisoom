import sys
input = sys.stdin.readline
setting = []

N = input().strip()

# alpabet = ["c=", "c-" "dz=", "d-", "lj", "nj", "s=", "z="]
# num = [0, 0, 0, 0, 0, 0, 0, 0]
result = 0

for i in range(len(N)):
    if N[i] == "c":
        if i+1 < len(N):
            if N[i+1] == "-":
                setting.append(2)
            elif N[i+1] == "=":
                setting.append(2)
            else:
                result += 1
    elif N[i] == "d":
        if i+2 < len(N) and N[i+1] == "z" and N[i+2] == "=":
            setting.append(3)

        elif i+1 < len(N) and N[i+1] == "-":
            setting.append(2)
        else:
            result += 1
    elif N[i] == "l":
        if i+1 < len(N):
            if N[i+1] == "j":
                setting.append(2)
            else:
                result += 1
    elif N[i] == "n":
        if i+1 < len(N):
            if N[i+1] == "j":
                setting.append(2)
            else:
                result += 1
    elif N[i] == "s":
        if i+1 < len(N):
            if N[i+1] == "=":
                setting.append(2)
            else:
                result += 1
    elif N[i] == "z":
        if i+1 < len(N) and 0 <= (i-1):
            if N[i+1] == "=" and N[i-1] != "d":
                setting.append(2)
            elif N[i+1] == "=" and N[i+1] == "d":
                result = result
            else:
                result += 1
        if i+1 < len(N) and i == 0:
            if N[i+1] == "=":
                setting.append(2)
            else:
                result += 1

x = 0
for i in range(len(setting)):
    x += setting[i]
# print(setting)
result = len(N)-x+len(setting)
print(result)
