def sort(data):
    for i in range(0, len(data)): #最初から順に整列させていく
        for j in range(i-1, -1, -1): #１番後ろの要素を挿入する場所を探す
            if data[j] > data[j+1]: # 隣り合う要素で前の方が大きい場合
                data[j], data[j+1] = data[j+1], data[j] #要素を入れ替える
            else:
                break #挿入する部分が見つかれば終わり

data = [1, 3, 2, 5, 4, 2, 1]
sort(data)
print(data)


