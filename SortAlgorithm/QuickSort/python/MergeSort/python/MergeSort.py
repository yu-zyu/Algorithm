def sort(data):
    if len(data) <= 1: #長さが１以下の場合は分割できないので終了
        return data

    # 分割操作
    mid = len(data) // 2 #真ん中を計算
    left = sort(data[:mid]) #再帰で前半を分割してleftに
    right = sort(data[mid:]) #再帰で後半を分割してrightに

    # 結合操作
    merge, l, r = [], 0, 0 # margeに結合
    while l < len(left) and r < len(right): # leftとrightの両方に要素がある場合
        if left[l] <= right[r]: #左側<=右側の場合
            merge.append(left[l]) #左側をmergeに加える
            l += 1
        else: # 左側＞右側の場合
            merge.append(right[r]) #右側をmergeに加える
            r += 1
    if l < len(left): #左側が余った場合に残りを追加
        merge.extend(left[l:])
    elif r < len(right): #右側が余った場合に残りを追加
        merge.extend(right[r:])
    return merge

data = [1, 3, 2, 5, 4, 2, 1]
data = sort(data)
print(data)

