def recursive_function(i):
    if i == 100:
        return  # 종료
    print(i, ' -> ', i+1)
    recursive_function(i+1)
    print(i, ' end')


recursive_function(1)
