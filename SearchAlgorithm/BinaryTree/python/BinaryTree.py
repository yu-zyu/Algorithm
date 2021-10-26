def search(data, target):
    start, end = 0, len(data)-1 #探索するデータの始点startと終点endを設定
    while start <= end: #探索するデータがある間は繰り返す
        i = (start + end) // 2 #真ん中のデータをiとする
        if data[i] == target: #見つかったときにはその位置iを返す
            return i
        elif data[i] < target: #targetの値の方が大きい場合は後のグループを探索
            start = i + 1
        else:
            end =i - 1
            
    return -1 #見つからないときは-1を返す

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 3
print("要素番号{}にデータ{}をみつけました。".format(search(data, target), target))

