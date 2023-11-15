N, M=map(int, input().split())
R, C, nav=map(int, input().split())
board=[]

for i in range(N):
    board.append(list(map(int, input().split())))

answer=1
navigate=1 # 4보다 크면 break

if nav==0:
    nav=3
elif nav==1:
    nav=0
elif nav==2:
    nav=1
elif nav==3:
    nav==2

while True:
    # 네가지 방향 다 갔는데도 노답이면 break 
    if navigate>4:break;
    if nav==0:
        if board[R][C-1]==1:
            navigate+=1
            nav=3
        else:
            R=R
            C=C-1
            board[R][C-1]=1
            answer+=1
            navigate=0
    elif nav==1:
        if board[R+1][C]==1:
            navigate+=1
            nav=0
        else:
            R=R+1
            C=C
            board[R+1][C]=1
            answer+=1     
            navigate=0 
    elif nav==2:
        if board[R][C+1]==1:
            navigate+=1
            nav=1
        else:
            R=R
            C=C+1
            board[R][C+1]=1
            answer+=1
            navigate=0
    elif nav==3:
        if board[R-1][C]==1:
            navigate+=1
            nav=2
        else:
            R=R-1
            C=C
            board[R-1][C]=1
            answer+=1
            navigate=0
   
     
print(answer)


# N, M=map(int, input().split())
# R, C, nav=map(int, input().split())
# board=[]

# for i in range(N):
#     board.append(list(map(int, input().split())))

# answer=1
# navigate=1 # 4보다 크면 break

# while True:

