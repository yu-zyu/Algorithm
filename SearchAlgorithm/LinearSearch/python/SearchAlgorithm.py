def search(data, target):
    for i in range(len(data)): #先頭から順番に探索
        if data[i] == target: #見つかったときにはその位置iを返す
            return i
    return -1 #見つからなかったときは-1を返す


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
print("要素番号{}にデータ{}をみつけました。".format(search(data, target), target))

