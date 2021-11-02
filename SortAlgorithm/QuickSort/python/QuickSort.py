def sort(data):
    n = len(data)
    pivot = data[n//2] #今回の基準値には、真ん中の値を利用
    left, right, middle = [], [], []
    for i in range(n): 
        if data[i] < pivot: #基準値より小さい場合は、差部分列leftに追加
            left.append(data[i])
        elif data[i] > pivot: #基準値より大きい場合は、右部分列rightに追加
            right.append(data[i])
        else:
            middle.append(data[i]) #基準値と同じ場合には、部分列middleに追加
    if left:
        left = sort(left) #再帰でleftを分割
    if right:
        right = sort(right) #再帰でrightを分割
    return left + middle + right #順番に部分列を結合させて、戻り値にする

data = [1, 3, 2, 5, 4, 2, 1]
data = sort(data)
print(data)



