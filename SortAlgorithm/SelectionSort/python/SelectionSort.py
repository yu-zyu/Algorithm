def sort(data):
    for i in range(0, len(data)-1): #最初から順に整列させていく
        min_i = i #最小値の位置をmin_iに求める
        for j in range(i+1, len(data)): #最小値を探すループ
            if data[min_i] > data[j]: #より小さい値があれば、最小値を置き換える
                min_i = j
            data[min_i], data[i] = data[i], data[min_i] #最小値の場所と要素を入れ替える

data = [1, 3, 2, 5, 4, 2, 1]
sort(data)
print(data)


