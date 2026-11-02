for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j:2d}", end=" ")
        #打印完这一条式子，不换行，末尾加一个空格
    print() #内层 j 循环全部跑完，这一行的所有式子都打印完了


